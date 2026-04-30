#!/usr/bin/env python3
"""
Generate EODHD Documentation Postman Collection from OpenAPI path YAMLs + folder config.

Usage:
    cd ~/Projects/EODHD-openapi
    python3 scripts/generate-postman.py

Inputs:
    paths/*.yaml              — OpenAPI endpoint definitions
    scripts/postman-config.yaml — folder mapping + request variants

Output:
    dist/eodhd-documentation.postman_collection.json
"""

import json
import os
import sys
import uuid
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
PATHS_DIR = ROOT / "paths"
CONFIG_FILE = ROOT / "scripts" / "postman-config.yaml"
OUTPUT_FILE = ROOT / "dist" / "eodhd-documentation.postman_collection.json"


def load_openapi_paths() -> dict:
    """Load all non-marketplace path YAML files and return dict[path_str] -> parsed YAML."""
    endpoints = {}
    for f in sorted(PATHS_DIR.glob("*.yaml")):
        if f.name.startswith("mp_"):
            continue
        with open(f) as fh:
            data = yaml.safe_load(fh)
        if data:
            for path_key, path_val in data.items():
                endpoints[path_key] = path_val
    return endpoints


def load_config() -> dict:
    """Load the postman-config.yaml."""
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)


def build_description_from_endpoint(ep: dict) -> str:
    """Build a Markdown request description from OpenAPI endpoint data."""
    get = ep.get("get", {})
    summary = get.get("summary", "")
    description = get.get("description", "")

    parts = []
    if summary:
        parts.append(f"# {summary}\n")
    if description:
        parts.append(f"{description}\n")

    # Parameters table
    params = get.get("parameters", [])
    query_params = [p for p in params if p.get("in") == "query" and p.get("name") != "api_token"]
    if query_params:
        parts.append("## Parameters\n")
        parts.append("| Parameter | Required | Description |")
        parts.append("|-----------|----------|-------------|")
        for p in query_params:
            req = "Yes" if p.get("required") else "No"
            desc = p.get("description", "")
            schema = p.get("schema", {})
            enum_vals = schema.get("enum")
            default_val = schema.get("default")
            extras = []
            if enum_vals:
                extras.append(f"Values: `{'`, `'.join(str(v) for v in enum_vals)}`")
            if default_val is not None:
                extras.append(f"Default: `{default_val}`")
            if extras:
                desc += " — " + "; ".join(extras)
            parts.append(f"| `{p['name']}` | {req} | {desc} |")
        parts.append("")

    return "\n".join(parts)


def build_param_list(ep: dict, variant: dict) -> list:
    """Build Postman query parameter list from OpenAPI params + variant overrides."""
    get = ep.get("get", {})
    params = get.get("parameters", [])
    query_overrides = variant.get("query_overrides", {})

    result = []

    # Always add api_token first
    result.append({
        "key": "api_token",
        "value": "{{api_token}}",
        "description": "API token for authentication.",
        "disabled": False,
    })

    # Add all query params from OpenAPI
    seen = {"api_token"}
    for p in params:
        if p.get("in") != "query" or p["name"] == "api_token":
            continue
        name = p["name"]
        seen.add(name)
        schema = p.get("schema", {})
        desc = p.get("description", "")
        enum_vals = schema.get("enum")
        default_val = schema.get("default")

        extras = []
        if enum_vals:
            extras.append(f"Values: {', '.join(str(v) for v in enum_vals)}")
        if default_val is not None:
            extras.append(f"Default: {default_val}")
        if extras:
            desc += " | " + "; ".join(extras)

        # Determine value and enabled/disabled
        if name in query_overrides:
            value = str(query_overrides[name])
            disabled = False
        elif p.get("required"):
            value = str(default_val) if default_val is not None else ""
            disabled = False
        else:
            # Use example or default or first enum value
            example = schema.get("example")
            if example is not None:
                value = str(example)
            elif default_val is not None:
                value = str(default_val)
            elif enum_vals:
                value = str(enum_vals[0])
            else:
                value = ""
            disabled = True  # Optional params disabled by default unless in variant

        result.append({
            "key": name,
            "value": value,
            "description": desc,
            "disabled": disabled,
        })

    # Add any query_overrides not already in OpenAPI params (edge cases)
    for name, value in query_overrides.items():
        if name not in seen:
            result.append({
                "key": name,
                "value": str(value),
                "description": "",
                "disabled": False,
            })

    return result


def build_url(path: str, variant: dict) -> dict:
    """Build Postman URL object."""
    path_params = variant.get("path_params", {})

    # Replace path params
    resolved_path = path
    for param_name, param_value in path_params.items():
        resolved_path = resolved_path.replace(f"{{{param_name}}}", str(param_value))

    # Split path into segments
    raw = resolved_path.lstrip("/")
    path_parts = raw.split("/") if raw else []

    url = {
        "raw": "{{api_url}}" + resolved_path,
        "host": ["{{api_url}}"],
        "path": path_parts,
    }

    return url


def build_request_item(ep: dict, variant: dict, path: str) -> dict:
    """Build a single Postman request item."""
    name = variant["name"]
    url_obj = build_url(path, variant)
    query_params = build_param_list(ep, variant)
    description = build_description_from_endpoint(ep)

    # Add query to url
    url_obj["query"] = query_params

    request_obj = {
        "method": "GET",
        "header": [
            {"key": "Accept", "value": "application/json"}
        ],
        "url": url_obj,
        "description": description,
    }

    # Build example responses
    responses = build_example_responses(ep, request_obj)

    item = {
        "name": name,
        "request": request_obj,
        "response": responses,
    }

    return item


def build_example_responses(ep: dict, request_obj: dict) -> list:
    """Extract example responses from OpenAPI endpoint."""
    get = ep.get("get", {})
    responses = get.get("responses", {})
    result = []

    resp_200 = responses.get("200", {})
    content = resp_200.get("content", {})
    json_content = content.get("application/json", {})

    # Build originalRequest (copy of the request for the response)
    original_request = {
        "method": request_obj["method"],
        "header": request_obj["header"],
        "body": {"mode": "raw", "raw": ""},
        "url": request_obj["url"],
    }

    # Try examples (plural) first, then example (singular)
    examples = json_content.get("examples", {})
    example = json_content.get("example")

    if examples:
        for ex_name, ex_data in examples.items():
            body = json.dumps(ex_data.get("value", {}), indent=2)
            result.append({
                "name": ex_data.get("summary", ex_name),
                "originalRequest": original_request,
                "status": "OK",
                "code": 200,
                "_postman_previewlanguage": "json",
                "header": [
                    {"key": "Content-Type", "value": "application/json"}
                ],
                "cookie": [],
                "responseTime": None,
                "body": body,
            })
    elif example is not None:
        body = json.dumps(example, indent=2)
        result.append({
            "name": "Success Response",
            "originalRequest": original_request,
            "status": "OK",
            "code": 200,
            "_postman_previewlanguage": "json",
            "header": [
                {"key": "Content-Type", "value": "application/json"}
            ],
            "cookie": [],
            "responseTime": None,
            "body": body,
        })

    return result


def generate_collection() -> dict:
    """Generate the full Postman v2.1 collection."""
    endpoints = load_openapi_paths()
    config = load_config()

    collection_config = config.get("collection", {})
    variables_config = config.get("variables", {})
    folders_config = config.get("folders", [])

    # Build folders
    items = []
    total_requests = 0

    for folder in folders_config:
        folder_name = folder["name"]
        folder_desc = folder.get("description", "")
        folder_items = []

        # Process OpenAPI-backed endpoints
        for ep_config in folder.get("endpoints", []):
            path = ep_config["path"]
            ep_data = endpoints.get(path)

            if not ep_data:
                print(f"  WARNING: Endpoint '{path}' not found in OpenAPI paths, skipping.", file=sys.stderr)
                continue

            for variant in ep_config.get("variants", []):
                item = build_request_item(ep_data, variant, path)
                folder_items.append(item)
                total_requests += 1

        # Process manual items (e.g., WebSocket docs)
        for manual in folder.get("manual_items", []):
            manual_item = {
                "name": manual["name"],
                "request": {
                    "method": manual.get("method", "GET"),
                    "header": manual.get("header", []),
                    "url": {
                        "raw": manual.get("url", ""),
                        "host": [manual.get("url", "").split("?")[0]],
                        "path": [],
                    },
                    "description": manual.get("description", ""),
                },
                "response": [],
            }
            # Add example responses if provided
            for ex in manual.get("examples", []):
                manual_item["response"].append({
                    "name": ex.get("name", "Example"),
                    "originalRequest": manual_item["request"],
                    "status": "OK",
                    "code": 200,
                    "_postman_previewlanguage": "json",
                    "header": [{"key": "Content-Type", "value": "application/json"}],
                    "cookie": [],
                    "responseTime": None,
                    "body": ex.get("body", ""),
                })
            folder_items.append(manual_item)
            total_requests += 1

        folder_item = {
            "name": folder_name,
            "item": folder_items,
        }
        if folder_desc:
            folder_item["description"] = folder_desc
        items.append(folder_item)

    # Build collection
    collection = {
        "info": {
            "_postman_id": collection_config.get("_postman_id", str(uuid.uuid4())),
            "name": collection_config.get("name", "EODHD Documentation"),
            "description": collection_config.get("description", ""),
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        },
        "item": items,
        "variable": [
            {
                "key": k,
                "value": v,
                "type": "string",
            }
            for k, v in variables_config.items()
        ],
    }

    print(f"\nGenerated: {len(items)} folders, {total_requests} requests")
    return collection


def validate_collection(collection: dict):
    """Run basic validation checks on the generated collection."""
    errors = []
    warnings = []

    items = collection.get("item", [])
    if not items:
        errors.append("No folders found in collection")

    all_names = set()
    total = 0
    for folder in items:
        folder_name = folder.get("name", "")
        for req in folder.get("item", []):
            total += 1
            req_name = req.get("name", "")
            full_name = f"{folder_name}/{req_name}"

            if full_name in all_names:
                errors.append(f"Duplicate request name: {full_name}")
            all_names.add(full_name)

            request = req.get("request", {})
            if not request.get("description"):
                warnings.append(f"No description: {full_name}")

            url = request.get("url", {})
            query = url.get("query", [])
            for param in query:
                if not param.get("description") and param.get("key") != "api_token":
                    warnings.append(f"No param description: {full_name} -> {param.get('key')}")

            if not req.get("response"):
                warnings.append(f"No example response: {full_name}")

    # Check _postman_id preserved
    postman_id = collection.get("info", {}).get("_postman_id", "")
    if postman_id != "963a320c-db6e-4629-96fe-adf9dac8e14d":
        warnings.append(f"_postman_id mismatch: {postman_id}")

    print(f"\nValidation: {total} requests, {len(errors)} errors, {len(warnings)} warnings")
    for e in errors:
        print(f"  ERROR: {e}", file=sys.stderr)
    for w in warnings[:10]:
        print(f"  WARN: {w}", file=sys.stderr)
    if len(warnings) > 10:
        print(f"  ... and {len(warnings) - 10} more warnings", file=sys.stderr)

    return len(errors) == 0


def main():
    print("EODHD Postman Collection Generator")
    print("=" * 40)

    # Ensure output dir exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    collection = generate_collection()

    if not validate_collection(collection):
        print("\nGeneration FAILED due to errors.", file=sys.stderr)
        sys.exit(1)

    # Wrap in Postman API format
    output = {"collection": collection}

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nOutput: {OUTPUT_FILE}")
    print("Done!")


if __name__ == "__main__":
    main()

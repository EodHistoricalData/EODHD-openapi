#!/bin/bash
# Validation script for EODHD OpenAPI Specification

echo "🔍 Validating EODHD OpenAPI Specification..."
echo ""

# Check if npx is available
if ! command -v npx &> /dev/null; then
    echo "❌ npx not found. Please install Node.js and npm."
    exit 1
fi

# Validate with Redocly CLI
echo "Running Redocly validation..."
npx @redocly/cli lint openapi.yaml

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Specification is valid!"
    echo ""
    echo "📊 Statistics:"
    echo "  - Endpoints: $(find paths -name "*.yaml" | wc -l)"
    echo "  - Schemas: $(find components/schemas -name "*.yaml" | wc -l)"
    echo "  - Parameters: $(find components/parameters -name "*.yaml" | wc -l)"
    echo "  - Responses: $(find components/responses -name "*.yaml" | wc -l)"
else
    echo ""
    echo "❌ Validation failed. Please check errors above."
    exit 1
fi

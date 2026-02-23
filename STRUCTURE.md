# Project Structure

This document describes the complete structure of the EODHD OpenAPI Specification project.

## Directory Layout

```
eodhd_openapi/
├── openapi.yaml                      # Main OpenAPI 3.1.0 specification
├── README.md                         # Project documentation
├── EXAMPLES.md                       # Usage examples and API guides
├── CONTRIBUTING.md                   # Contribution guidelines
├── LICENSE                           # MIT License
├── STRUCTURE.md                      # This file
├── package.json                      # NPM configuration
├── validate.sh                       # Validation script
├── generate_specs.py                 # Generator script
├── .gitignore                        # Git ignore rules
│
├── paths/                            # Individual endpoint definitions (33 files)
│   ├── calendar_earnings.yaml       # GET /calendar/earnings
│   ├── calendar_ipos.yaml           # GET /calendar/ipos
│   ├── calendar_splits.yaml         # GET /calendar/splits
│   ├── calendar_trends.yaml         # GET /calendar/trends
│   ├── div_ticker.yaml              # GET /div/{ticker}
│   ├── economic-events.yaml         # GET /economic-events
│   ├── eod_ticker.yaml              # GET /eod/{ticker}
│   ├── eod-bulk-last-day_exchange.yaml  # GET /eod-bulk-last-day/{exchange}
│   ├── exchange-details_EXCHANGE_CODE.yaml  # GET /exchange-details/{EXCHANGE_CODE}
│   ├── exchanges-list.yaml          # GET /exchanges-list
│   ├── exchange-symbol-list_exchangeCode.yaml  # GET /exchange-symbol-list/{exchangeCode}
│   ├── fundamentals_ticker.yaml     # GET /fundamentals/{ticker}
│   ├── historical-market-cap_ticker.yaml  # GET /historical-market-cap/{ticker}
│   ├── insider-transactions.yaml    # GET /insider-transactions
│   ├── internal-user.yaml           # GET /internal-user
│   ├── intraday_ticker.yaml         # GET /intraday/{ticker}
│   ├── logo_symbol.yaml             # GET /logo/{symbol}
│   ├── macro-indicator_country.yaml # GET /macro-indicator/{country}
│   ├── mp_unicornbay_options_contracts.yaml  # GET /mp/unicornbay/options/contracts
│   ├── mp_unicornbay_options_eod.yaml  # GET /mp/unicornbay/options/eod
│   ├── mp_unicornbay_options_underlying-symbols.yaml  # GET /mp/unicornbay/options/underlying-symbols
│   ├── mp_unicornbay_spglobal_comp_symbol.yaml  # GET /mp/unicornbay/spglobal/comp/{symbol}
│   ├── mp_unicornbay_spglobal_list.yaml  # GET /mp/unicornbay/spglobal/list
│   ├── news.yaml                    # GET /news
│   ├── news-word-weights.yaml       # GET /news-word-weights
│   ├── real-time_ticker.yaml        # GET /real-time/{ticker}
│   ├── screener.yaml                # GET /screener
│   ├── search_query.yaml            # GET /search/{query}
│   ├── sentiments.yaml              # GET /sentiments
│   ├── splits_ticker.yaml           # GET /splits/{ticker}
│   ├── symbol-change-history.yaml   # GET /symbol-change-history
│   ├── technical_ticker.yaml        # GET /technical/{ticker}
│   └── ticks.yaml                   # GET /ticks
│
├── components/                       # Reusable components
│   ├── index.yaml                   # Components index with $refs
│   ├── securitySchemes.yaml         # API authentication schemes
│   │
│   ├── parameters/                  # Reusable parameters (5 files)
│   │   ├── ApiToken.yaml           # api_token parameter
│   │   ├── DateFrom.yaml           # from date parameter
│   │   ├── DateTo.yaml             # to date parameter
│   │   ├── FmtCsvJson.yaml         # csv/json format parameter
│   │   └── FmtJsonXml.yaml         # json/xml format parameter
│   │
│   ├── responses/                   # Common responses (4 files)
│   │   ├── UnauthorizedHtml.yaml   # 401 Unauthorized
│   │   ├── ForbiddenHtml.yaml      # 403 Forbidden
│   │   ├── NotFoundHtml.yaml       # 404 Not Found
│   │   └── TooManyHtml.yaml        # 429 Too Many Requests
│   │
│   └── schemas/                     # Data models (58 files)
│       ├── Error.yaml
│       ├── InternalUser.yaml
│       ├── SearchResult.yaml
│       ├── WordWeightsResponse.yaml
│       ├── Links.yaml
│       ├── MetaPagination.yaml
│       ├── OptionsCommonAttributes.yaml
│       ├── OptionsContractsItem.yaml
│       ├── OptionsContractsResponse.yaml
│       ├── OptionsEODItem.yaml
│       ├── OptionsEODResponse.yaml
│       ├── OptionsEODCompactResponse.yaml
│       ├── OptionsUnderlyingSymbolsItem.yaml
│       ├── OptionsUnderlyingSymbolsResponse.yaml
│       ├── StockFinancials.yaml
│       ├── IndexGeneral.yaml
│       ├── IndexListItem.yaml
│       ├── IndexListResponse.yaml
│       ├── IndexComponent.yaml
│       ├── IndexComponentItem.yaml
│       ├── IndexComponentsMap.yaml
│       ├── IndexComponentsResponse.yaml
│       ├── HistoricalIndexComponent.yaml
│       ├── HistoricalComponentItem.yaml
│       ├── HistoricalComponentsMap.yaml
│       ├── FinancialStatementRow.yaml
│       └── ... (and 33 more schema files)
```

## File Counts

- **Total YAML files**: 103
  - Main specification: 1
  - Path definitions: 33
  - Component files: 69 (5 parameters + 4 responses + 58 schemas + 2 indexes)

- **Documentation files**: 5
  - README.md
  - EXAMPLES.md
  - CONTRIBUTING.md
  - STRUCTURE.md (this file)
  - LICENSE

- **Configuration files**: 3
  - package.json
  - .gitignore
  - validate.sh

- **Utility files**: 1
  - generate_specs.py

## Component Organization

### Security Schemes

The API uses API Key authentication:

- **EODHDQueryKey**: Query parameter authentication using `api_token`

### Common Parameters

Reusable parameters shared across endpoints:

1. **ApiToken**: Required API token for authentication
2. **DateFrom**: Optional start date (YYYY-MM-DD format)
3. **DateTo**: Optional end date (YYYY-MM-DD format)
4. **FmtCsvJson**: Format parameter (csv or json)
5. **FmtJsonXml**: Format parameter (json or xml)

### Standard Responses

Common error responses:

1. **UnauthorizedHtml** (401): Invalid or missing API token
2. **ForbiddenHtml** (403): Access denied
3. **NotFoundHtml** (404): Resource not found
4. **TooManyHtml** (429): Rate limit exceeded (includes rate limit headers)

### Schema Categories

Schemas are organized by data type:

- **Error Handling**: Error
- **User Management**: InternalUser
- **Search & Discovery**: SearchResult
- **News & Sentiment**: WordWeightsResponse, Links, MetaPagination
- **Options Data**: OptionsCommonAttributes, OptionsContractsItem, OptionsContractsResponse, OptionsEODItem, OptionsEODResponse, OptionsEODCompactResponse, OptionsUnderlyingSymbolsItem, OptionsUnderlyingSymbolsResponse
- **Financials**: StockFinancials, FinancialStatementRow
- **Indices**: IndexGeneral, IndexListItem, IndexListResponse, IndexComponent, IndexComponentItem, IndexComponentsMap, IndexComponentsResponse
- **Historical Data**: HistoricalIndexComponent, HistoricalComponentItem, HistoricalComponentsMap
- And many more...

## API Endpoint Categories

### Calendar Events (4 endpoints)
- Earnings calendar
- IPO calendar
- Splits calendar
- Market trends

### End-of-Day Data (3 endpoints)
- Historical EOD prices
- Bulk EOD data
- Historical market capitalization

### Real-time & Intraday (3 endpoints)
- Real-time quotes
- Intraday data
- Tick data

### Fundamentals (4 endpoints)
- Comprehensive fundamentals
- Dividend history
- Split history
- Historical market cap

### Exchanges (3 endpoints)
- List exchanges
- Exchange details
- Exchange symbols

### Economic Data (2 endpoints)
- Economic events
- Macro indicators

### Options (3 endpoints)
- Options contracts
- Options EOD data
- Underlying symbols

### News & Sentiment (3 endpoints)
- News feed
- Sentiment analysis
- News word weights

### Technical Analysis (1 endpoint)
- Technical indicators

### Screening & Search (2 endpoints)
- Stock screener
- Symbol search

### Corporate Actions (2 endpoints)
- Symbol change history
- Insider transactions

### Other (3 endpoints)
- Company logos
- User account info
- S&P Global data

## Reference Structure

The specification uses `$ref` to maintain modularity:

### Main OpenAPI File

```yaml
paths:
  /calendar/earnings:
    $ref: './paths/calendar_earnings.yaml#/calendar/earnings'
  # ... other paths

components:
  $ref: 'components/index.yaml'
```

### Components Index

```yaml
parameters:
  ApiToken:
    $ref: './parameters/ApiToken.yaml#ApiToken'
  # ... other parameters

schemas:
  Error:
    $ref: './schemas/Error.yaml#Error'
  # ... other schemas
```

### Path Files

Each path file contains a complete endpoint definition:

```yaml
/calendar/earnings:
  get:
    summary: Retrieve upcoming earnings data
    operationId: GetUpcomingEarnings
    parameters: [...]
    responses: [...]
```

## Regenerating the Specification

To regenerate all files from source:

```bash
python3 generate_specs.py
```

This will:
1. Load source JSON specifications
2. Extract all paths, components, and schemas
3. Generate individual YAML files
4. Create references in index files
5. Generate main openapi.yaml with all references

## Validation

Validate the complete specification:

```bash
# Using validation script
bash validate.sh

# Using npm
npm run validate

# Using Redocly CLI directly
npx @redocly/cli lint openapi.yaml
```

## Viewing the Documentation

### Local Preview

```bash
npm run preview
```

Opens interactive documentation at http://localhost:8080

### Swagger Editor

1. Go to https://editor.swagger.io/
2. File → Import File → Select openapi.yaml

### Redoc

```bash
npx @redocly/cli preview-docs openapi.yaml
```

## Code Generation

Generate client libraries:

```bash
# Python
npm run generate-python

# TypeScript
npm run generate-typescript

# Java
npm run generate-java

# Go
npm run generate-go
```

## Maintenance

### Adding New Endpoints

1. Add endpoint definition to source JSON file
2. Run `python3 generate_specs.py`
3. Validate: `npm run validate`
4. Commit changes

### Modifying Existing Endpoints

1. Edit the specific path file in `paths/`
2. Validate: `npm run validate`
3. Test: `npm run preview`
4. Commit changes

### Adding New Schemas

1. Create schema file in `components/schemas/`
2. Add reference in `components/index.yaml`
3. Validate: `npm run validate`
4. Commit changes

## Version Control

### Recommended Git Workflow

```bash
# Create feature branch
git checkout -b feature/add-new-endpoint

# Make changes
# ...

# Validate
npm run validate

# Commit
git add .
git commit -m "feat(endpoints): add new endpoint for X"

# Push and create PR
git push origin feature/add-new-endpoint
```

### What to Commit

✅ **Do commit:**
- All `.yaml` files
- Documentation (`.md` files)
- Configuration (`package.json`, `.gitignore`)
- Scripts (`validate.sh`, `generate_specs.py`)

❌ **Don't commit:**
- `node_modules/`
- Generated client code (in `clients/`)
- Build artifacts (in `dist/`)
- Log files

## Integration

### Using in Projects

#### As Git Submodule

```bash
git submodule add https://github.com/yourusername/eodhd-openapi-spec.git specs
```

#### As NPM Dependency

```json
{
  "dependencies": {
    "eodhd-openapi-spec": "github:yourusername/eodhd-openapi-spec"
  }
}
```

#### Direct Download

```bash
curl -O https://raw.githubusercontent.com/yourusername/eodhd-openapi-spec/main/openapi.yaml
```

## Additional Resources

- [OpenAPI 3.1.0 Specification](https://spec.openapis.org/oas/v3.1.0)
- [JSON Schema 2020-12](https://json-schema.org/specification.html)
- [Redocly CLI](https://redocly.com/docs/cli/)
- [OpenAPI Generator](https://openapi-generator.tech)
- [EODHD API Docs](https://eodhd.com/financial-apis/)

## Support

For issues, questions, or contributions:

- GitHub Issues: https://github.com/yourusername/eodhd-openapi-spec/issues
- Documentation: See README.md
- Examples: See EXAMPLES.md
- Contributing: See CONTRIBUTING.md

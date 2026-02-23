# EODHD Financial Data API - OpenAPI Specification

Comprehensive OpenAPI 3.1.0 specification for the [EOD Historical Data (EODHD)](https://eodhd.com) Financial Data API.

## Overview

This repository contains a complete, modular OpenAPI specification for the EODHD API, covering **74 REST endpoints** across 22 categories. The API provides access to:

- **End-of-Day (EOD) Data**: Historical and current stock prices
- **Intraday & Real-time Data**: Live market data, ticks, and delayed quotes
- **Fundamentals**: Company financial statements, valuations, metrics, and bulk fundamentals
- **Calendar Events**: Earnings, IPOs, splits, dividends, and trends
- **Economic Data**: Macro indicators and economic events
- **Options Data**: Options contracts and pricing
- **News & Sentiment**: Financial news and sentiment analysis
- **Technical Indicators**: Technical analysis data
- **Exchange Information**: Exchange details and symbol listings
- **Corporate Actions**: Dividends, splits, symbol changes, and insider transactions
- **Screening Tools**: Stock screening and search functionality
- **Indices**: S&P/Dow Jones indices data and components
- **US Treasury**: Bill rates, yield curves, long-term rates, and real yields
- **Trading Hours**: Market hours, status, and lookup
- **CBOE**: CBOE index data and listings
- **ESG**: Environmental, Social, and Governance ratings (Investverte)
- **Risk Analytics**: Performance, risk, volatility analysis (illio)
- **Investment Analytics**: Risk scoring, bond analysis, bank financials (PRAAMS)

> **Note**: EODHD also provides a WebSocket endpoint (`wss://ws.eodhistoricaldata.com/ws/{market}`) for real-time streaming data, which is documented separately and not included in this REST specification.

## Specification Structure

The specification is organized into modular files for better maintainability:

```
eodhd_openapi/
├── openapi.yaml                    # Main OpenAPI specification file
├── paths/                          # Individual endpoint definitions
│   ├── calendar_earnings.yaml
│   ├── calendar_dividends.yaml
│   ├── eod_ticker.yaml
│   ├── fundamentals_ticker.yaml
│   ├── cboe_indices.yaml
│   ├── ust_yield-rates.yaml
│   ├── mp_illio_chapters_*.yaml
│   ├── mp_investverte_*.yaml
│   ├── mp_praams_*.yaml
│   └── ... (74 endpoint files total)
├── components/
│   ├── index.yaml                 # Components index with references
│   ├── securitySchemes.yaml       # API authentication schemes
│   ├── parameters/                # Reusable parameters
│   │   ├── ApiToken.yaml
│   │   ├── FmtCsvJson.yaml
│   │   ├── DateFrom.yaml
│   │   └── DateTo.yaml
│   ├── responses/                 # Common response definitions
│   │   ├── UnauthorizedHtml.yaml
│   │   ├── ForbiddenHtml.yaml
│   │   ├── NotFoundHtml.yaml
│   │   └── TooManyHtml.yaml
│   └── schemas/                   # Data model schemas (58 files)
│       ├── Error.yaml
│       ├── InternalUser.yaml
│       └── ...
└── README.md                       # This file
```

## API Endpoints

The specification includes 74 API endpoints organized by category:

### Calendar Events
- `GET /calendar/earnings` - Upcoming and historical earnings
- `GET /calendar/ipos` - IPO calendar
- `GET /calendar/splits` - Stock splits calendar
- `GET /calendar/trends` - Market trends calendar
- `GET /calendar/dividends` - Dividends calendar

### End-of-Day Data
- `GET /eod/{ticker}` - Historical EOD prices
- `GET /eod-bulk-last-day/{exchange}` - Bulk EOD data for entire exchange
- `GET /historical-market-cap/{ticker}` - Historical market capitalization

### Intraday & Real-time
- `GET /intraday/{ticker}` - Intraday price data
- `GET /real-time/{ticker}` - Real-time quotes
- `GET /ticks` - Tick-level data
- `GET /us-quote-delayed` - US 15-minute delayed quotes
- `GET /mp/unicornbay/tickdata/ticks` - Marketplace tick data

### Fundamentals
- `GET /fundamentals/{ticker}` - Comprehensive fundamental data
- `GET /bulk-fundamentals/{EXCHANGE}` - Bulk fundamentals for an exchange

### Exchanges
- `GET /exchanges-list` - List all exchanges
- `GET /exchange-details/{EXCHANGE_CODE}` - Exchange details
- `GET /exchange-symbol-list/{exchangeCode}` - Symbols for exchange

### Economic Data
- `GET /economic-events` - Economic calendar events
- `GET /macro-indicator/{country}` - Macro economic indicators

### Options Data
- `GET /mp/unicornbay/options/contracts` - Options contracts
- `GET /mp/unicornbay/options/eod` - Options EOD data
- `GET /mp/unicornbay/options/underlying-symbols` - Underlying symbols

### News & Sentiment
- `GET /news` - Financial news
- `GET /sentiments` - Sentiment analysis
- `GET /news-word-weights` - News word weights analysis

### Technical Analysis
- `GET /technical/{ticker}` - Technical indicators

### Screening & Search
- `GET /screener` - Stock screener
- `GET /search/{query}` - Symbol search

### Dividends & Splits
- `GET /div/{ticker}` - Dividend history
- `GET /splits/{ticker}` - Split history

### Corporate Actions
- `GET /symbol-change-history` - Symbol changes
- `GET /insider-transactions` - Insider trading data

### Logos
- `GET /logo/{symbol}` - Company logos (PNG)
- `GET /logo-svg/{symbol}` - Company logos (SVG)

### Indices (S&P/Dow Jones)
- `GET /mp/unicornbay/spglobal/list` - S&P Global indices list
- `GET /mp/unicornbay/spglobal/comp/{symbol}` - Index components

### US Treasury
- `GET /ust/bill-rates` - Treasury bill discount rates
- `GET /ust/yield-rates` - Yield curve constant maturity rates
- `GET /ust/long-term-rates` - Long-term average rates
- `GET /ust/real-yield-rates` - TIPS-derived real yield rates

### CBOE
- `GET /cboe/indices` - List CBOE indices
- `GET /cboe/index` - Historical CBOE index data

### Trading Hours
- `GET /mp/tradinghours/markets` - List all markets
- `GET /mp/tradinghours/markets/lookup` - Lookup market by code
- `GET /mp/tradinghours/markets/details` - Market trading hours details
- `GET /mp/tradinghours/markets/status` - Current market status

### ESG (Investverte)
- `GET /mp/investverte/companies` - List ESG-rated companies
- `GET /mp/investverte/countries` - ESG country scores
- `GET /mp/investverte/sectors` - ESG sector scores
- `GET /mp/investverte/esg/{symbol}` - Company ESG rating
- `GET /mp/investverte/country/{symbol}` - Country ESG details
- `GET /mp/investverte/sector/{symbol}` - Sector ESG details

### Risk Analytics (illio)
- `GET /mp/illio/chapters/best-and-worst/{id}` - Best/worst periods
- `GET /mp/illio/chapters/beta-bands/{id}` - Beta bands analysis
- `GET /mp/illio/chapters/volatility/{id}` - Volatility analysis
- `GET /mp/illio/chapters/volume/{id}` - Volume analysis
- `GET /mp/illio/chapters/performance/{id}` - Performance analysis
- `GET /mp/illio/chapters/risk/{id}` - Risk analysis
- `GET /mp/illio/categories/performance/{id}` - Category performance
- `GET /mp/illio/categories/risk/{id}` - Category risk

### Investment Analytics (PRAAMS)
- `GET /mp/praams/bank/balance_sheet/ticker/{ticker}` - Bank balance sheet by ticker
- `GET /mp/praams/bank/balance_sheet/isin/{isin}` - Bank balance sheet by ISIN
- `GET /mp/praams/bank/income_statement/ticker/{ticker}` - Bank income statement by ticker
- `GET /mp/praams/bank/income_statement/isin/{isin}` - Bank income statement by ISIN
- `GET /mp/praams/analyse/bond/{isin}` - Bond analysis
- `GET /mp/praams/analyse/equity/ticker/{ticker}` - Equity analysis by ticker
- `GET /mp/praams/analyse/equity/isin/{isin}` - Equity analysis by ISIN
- `GET /mp/praams/reports/bond/{isin}` - Bond report
- `GET /mp/praams/reports/equity/ticker/{ticker}` - Equity report by ticker
- `GET /mp/praams/reports/equity/isin/{isin}` - Equity report by ISIN
- `GET /mp/praams/explore/bond` - Explore/search bonds
- `GET /mp/praams/explore/equity` - Explore/search equities

### User
- `GET /internal-user` - User account information

## Authentication

The API uses API key authentication via query parameter:

```
?api_token=YOUR_API_TOKEN
```

All endpoints require a valid API token. You can obtain one by registering at [eodhd.com](https://eodhd.com).

## Servers

Two API servers are available:

- **Primary**: `https://eodhd.com/api`
- **Alternative**: `https://eodhistoricaldata.com/api`

## Response Formats

Most endpoints support multiple output formats:

- **JSON** (default): Structured JSON response
- **CSV**: Comma-separated values (selected endpoints)
- **XML**: XML format (selected endpoints)

Specify format using the `fmt` query parameter:
```
?fmt=json
?fmt=csv
?fmt=xml
```

## Rate Limiting

The API implements rate limiting. When exceeded, responses include:

- **Status**: `429 Too Many Requests`
- **Headers**:
  - `X-RateLimit-Limit`: Requests per minute limit
  - `X-RateLimit-Remaining`: Requests remaining
  - `Retry-After`: Seconds to wait before retry

## Error Responses

Standard HTTP error codes are used:

- `400` - Bad Request: Invalid parameters
- `401` - Unauthorized: Invalid or missing API token
- `403` - Forbidden: Access denied for current subscription
- `404` - Not Found: Resource not found
- `429` - Too Many Requests: Rate limit exceeded
- `500` - Internal Server Error: Server error

Error responses include:
```json
{
  "status": 400,
  "error": "Bad Request",
  "message": "Detailed error message"
}
```

## Usage Examples

### Get EOD Data for Apple Stock
```bash
curl "https://eodhd.com/api/eod/AAPL.US?api_token=YOUR_TOKEN&fmt=json"
```

### Get Upcoming Earnings
```bash
curl "https://eodhd.com/api/calendar/earnings?api_token=YOUR_TOKEN&from=2024-01-01&to=2024-01-31&fmt=json"
```

### Get Real-time Quote
```bash
curl "https://eodhd.com/api/real-time/MSFT.US?api_token=YOUR_TOKEN&fmt=json"
```

### Get Fundamental Data
```bash
curl "https://eodhd.com/api/fundamentals/GOOGL.US?api_token=YOUR_TOKEN"
```

### Get US Treasury Yield Rates
```bash
curl "https://eodhd.com/api/ust/yield-rates?api_token=YOUR_TOKEN&from=2024-01-01&to=2024-01-31&fmt=json"
```

### Get Market Trading Status
```bash
curl "https://eodhd.com/api/mp/tradinghours/markets/status?api_token=YOUR_TOKEN&fin_id=us.nyse&fmt=json"
```

### Get ESG Rating for a Company
```bash
curl "https://eodhd.com/api/mp/investverte/esg/AAPL.US?api_token=YOUR_TOKEN&fmt=json"
```

### Analyse Equity Risk (PRAAMS)
```bash
curl "https://eodhd.com/api/mp/praams/analyse/equity/ticker/AAPL.US?api_token=YOUR_TOKEN&fmt=json"
```

### Search for Symbols
```bash
curl "https://eodhd.com/api/search/Tesla?api_token=YOUR_TOKEN"
```

## OpenAPI Specification Compliance

This specification adheres to:

- **OpenAPI Specification 3.1.0**: [spec.openapis.org/oas/v3.1.0](https://spec.openapis.org/oas/v3.1.0.html)
- **JSON Schema 2020-12**: Full compatibility with modern JSON Schema
- **Swagger/OpenAPI**: Compatible with Swagger UI and other OpenAPI tools

## Viewing the Specification

### Using Swagger UI

1. Visit [Swagger Editor](https://editor.swagger.io/)
2. Load the `openapi.yaml` file
3. Explore the API interactively

### Using Redoc

```bash
npx @redocly/cli preview-docs openapi.yaml
```

### Using VS Code

Install the "OpenAPI (Swagger) Editor" extension and open `openapi.yaml`.

## Code Generation

Generate client libraries using OpenAPI Generator:

### Python Client
```bash
openapi-generator-cli generate -i openapi.yaml -g python -o ./python-client
```

### JavaScript/TypeScript Client
```bash
openapi-generator-cli generate -i openapi.yaml -g typescript-axios -o ./typescript-client
```

### Java Client
```bash
openapi-generator-cli generate -i openapi.yaml -g java -o ./java-client
```

### Other Languages
OpenAPI Generator supports 50+ languages. See: [openapi-generator.tech](https://openapi-generator.tech)

## Validation

Validate the specification:

```bash
# Using Redocly CLI
npx @redocly/cli lint openapi.yaml

# Using Swagger CLI
swagger-cli validate openapi.yaml

# Using OpenAPI CLI
openapi lint openapi.yaml
```

## Development

### Regenerating the Specification

The specification was generated from source JSON files using the included Python script:

```bash
python3 generate_specs.py
```

**Requirements**:
- Python 3.7+
- PyYAML: `pip install pyyaml`

### Modifying Endpoints

Each endpoint is in a separate file under `paths/`. Modify the relevant file and they will be automatically included via the references in `openapi.yaml`.

### Adding New Schemas

Add new schema files to `components/schemas/` and reference them in `components/index.yaml`.

## Resources

- **EODHD Website**: [eodhd.com](https://eodhd.com)
- **API Documentation**: [eodhd.com/financial-apis/](https://eodhd.com/financial-apis/)
- **API Registration**: [eodhd.com/register](https://eodhd.com/register)
- **Support**: support@eodhd.com

## Specification Version

- **Version**: 2.0.0
- **OpenAPI**: 3.1.0
- **Last Updated**: 2026-02-18

## License

This OpenAPI specification is provided as-is for use with the EODHD API. The API itself is proprietary and subject to EODHD's terms of service.

## Contributing

To contribute to this specification:

1. Fork the repository
2. Create a feature branch
3. Make your changes to the relevant files
4. Validate the specification
5. Submit a pull request

## Tags

`openapi` `api` `financial-data` `stocks` `market-data` `eodhd` `swagger` `rest-api` `trading` `finance` `esg` `treasury` `options` `indices`

## Changelog

### 2.0.0 (2026-02-18)
- Expanded from 33 to 74 REST endpoints
- Added 7 new tags: US Treasury, Trading Hours, CBOE, ESG, Risk Analytics, Investment Analytics, Indices
- Added US Treasury endpoints (bill rates, yield curves, long-term rates, real yields)
- Added CBOE index endpoints
- Added Trading Hours marketplace endpoints (markets, lookup, details, status)
- Added ESG/Investverte endpoints (companies, countries, sectors, ratings)
- Added Risk Analytics/illio endpoints (best-and-worst, beta-bands, volatility, volume, performance, risk, categories)
- Added Investment Analytics/PRAAMS endpoints (bank financials, bond/equity analysis, reports, explore)
- Added calendar dividends, bulk fundamentals, SVG logos, US delayed quotes, marketplace tick data
- Formalized Indices tag for S&P/Dow Jones endpoints
- Version bump to 2.0.0

### 1.0.0 (2026-02-10)
- Initial release
- Complete specification for all 33 EODHD API endpoints
- Modular structure with separate files per endpoint
- 58 schema definitions
- Comprehensive documentation and examples

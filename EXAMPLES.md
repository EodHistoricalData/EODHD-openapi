# EODHD API Examples

This document provides practical examples for using the EODHD Financial Data API.

## Table of Contents

- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [End-of-Day Data](#end-of-day-data)
- [Real-time & Intraday Data](#real-time--intraday-data)
- [Calendar Events](#calendar-events)
- [Fundamentals](#fundamentals)
- [Exchange Information](#exchange-information)
- [Options Data](#options-data)
- [News & Sentiment](#news--sentiment)
- [Technical Analysis](#technical-analysis)
- [Screening & Search](#screening--search)
- [Error Handling](#error-handling)

## Getting Started

All examples assume you have an API token. Replace `YOUR_API_TOKEN` with your actual token.

Base URLs:
- Primary: `https://eodhd.com/api`
- Alternative: `https://eodhistoricaldata.com/api`

## Authentication

All requests require an `api_token` query parameter:

```bash
curl "https://eodhd.com/api/exchanges-list?api_token=YOUR_API_TOKEN"
```

## End-of-Day Data

### Get Historical EOD Prices

Get historical daily prices for Apple stock:

```bash
curl "https://eodhd.com/api/eod/AAPL.US?api_token=YOUR_API_TOKEN&from=2024-01-01&to=2024-12-31&fmt=json"
```

**Response:**
```json
[
  {
    "date": "2024-01-02",
    "open": 187.15,
    "high": 188.44,
    "low": 183.89,
    "close": 185.64,
    "adjusted_close": 185.64,
    "volume": 82488300
  },
  {
    "date": "2024-01-03",
    "open": 184.22,
    "high": 185.88,
    "low": 183.43,
    "close": 184.25,
    "adjusted_close": 184.25,
    "volume": 58414400
  }
]
```

### Get Latest EOD Data for Entire Exchange

Get all latest prices for NASDAQ:

```bash
curl "https://eodhd.com/api/eod-bulk-last-day/US?api_token=YOUR_API_TOKEN&fmt=json"
```

### Get Specific Period

Last 30 days only:

```bash
curl "https://eodhd.com/api/eod/MSFT.US?api_token=YOUR_API_TOKEN&period=d&order=d"
```

### CSV Format

```bash
curl "https://eodhd.com/api/eod/GOOGL.US?api_token=YOUR_API_TOKEN&fmt=csv"
```

## Real-time & Intraday Data

### Get Real-time Quote

```bash
curl "https://eodhd.com/api/real-time/TSLA.US?api_token=YOUR_API_TOKEN&fmt=json"
```

**Response:**
```json
{
  "code": "TSLA.US",
  "timestamp": 1704398400,
  "gmtoffset": -18000,
  "open": 238.45,
  "high": 245.32,
  "low": 237.12,
  "close": 243.84,
  "volume": 145632100,
  "previousClose": 237.93,
  "change": 5.91,
  "change_p": 2.48
}
```

### Get Intraday Data

5-minute intervals:

```bash
curl "https://eodhd.com/api/intraday/AAPL.US?api_token=YOUR_API_TOKEN&interval=5m&from=1704067200&to=1704153600&fmt=json"
```

1-hour intervals:

```bash
curl "https://eodhd.com/api/intraday/MSFT.US?api_token=YOUR_API_TOKEN&interval=1h&fmt=json"
```

## Calendar Events

### Get Upcoming Earnings

Next 7 days:

```bash
curl "https://eodhd.com/api/calendar/earnings?api_token=YOUR_API_TOKEN&fmt=json"
```

Specific date range:

```bash
curl "https://eodhd.com/api/calendar/earnings?api_token=YOUR_API_TOKEN&from=2024-03-01&to=2024-03-31&fmt=json"
```

**Response:**
```json
{
  "type": "Earnings",
  "description": "Historical and upcoming Earnings",
  "from": "2024-03-01",
  "to": "2024-03-31",
  "earnings": [
    {
      "code": "AAPL.US",
      "report_date": "2024-03-15",
      "date": "2024-03-15",
      "before_after_market": "AfterMarket",
      "currency": "USD",
      "actual": 1.52,
      "estimate": 1.48,
      "difference": 0.04,
      "percent": 2.7
    }
  ]
}
```

Specific symbols only:

```bash
curl "https://eodhd.com/api/calendar/earnings?api_token=YOUR_API_TOKEN&symbols=AAPL.US,MSFT.US,GOOGL.US&fmt=json"
```

### Get IPO Calendar

```bash
curl "https://eodhd.com/api/calendar/ipos?api_token=YOUR_API_TOKEN&from=2024-01-01&to=2024-12-31&fmt=json"
```

### Get Stock Splits

```bash
curl "https://eodhd.com/api/calendar/splits?api_token=YOUR_API_TOKEN&from=2024-01-01&to=2024-12-31&fmt=json"
```

### Get Market Trends

```bash
curl "https://eodhd.com/api/calendar/trends?api_token=YOUR_API_TOKEN&fmt=json"
```

## Fundamentals

### Get Comprehensive Fundamental Data

```bash
curl "https://eodhd.com/api/fundamentals/AAPL.US?api_token=YOUR_API_TOKEN"
```

**Response includes:**
- General company information
- Highlights (market cap, P/E ratio, etc.)
- Valuation metrics
- Share statistics
- Technicals
- Splits and dividends history
- Financials (Income Statement, Balance Sheet, Cash Flow)
- Earnings history and estimates
- Analyst ratings

### Filter Fundamental Data

Get only highlights:

```bash
curl "https://eodhd.com/api/fundamentals/AAPL.US?api_token=YOUR_API_TOKEN&filter=Highlights::*"
```

Get only financials:

```bash
curl "https://eodhd.com/api/fundamentals/AAPL.US?api_token=YOUR_API_TOKEN&filter=Financials::*"
```

### Get Dividend History

```bash
curl "https://eodhd.com/api/div/AAPL.US?api_token=YOUR_API_TOKEN&from=2020-01-01&fmt=json"
```

### Get Split History

```bash
curl "https://eodhd.com/api/splits/TSLA.US?api_token=YOUR_API_TOKEN&from=2020-01-01&fmt=json"
```

### Get Historical Market Cap

```bash
curl "https://eodhd.com/api/historical-market-cap/AAPL.US?api_token=YOUR_API_TOKEN&from=2023-01-01&to=2023-12-31"
```

## Exchange Information

### List All Exchanges

```bash
curl "https://eodhd.com/api/exchanges-list?api_token=YOUR_API_TOKEN&fmt=json"
```

**Response:**
```json
[
  {
    "Name": "New York Stock Exchange",
    "Code": "US",
    "OperatingMIC": "XNYS",
    "Country": "USA",
    "Currency": "USD",
    "CountryISO2": "US",
    "CountryISO3": "USA"
  },
  {
    "Name": "NASDAQ",
    "Code": "NASDAQ",
    "OperatingMIC": "XNAS",
    "Country": "USA",
    "Currency": "USD",
    "CountryISO2": "US",
    "CountryISO3": "USA"
  }
]
```

### Get Exchange Details

```bash
curl "https://eodhd.com/api/exchange-details/US?api_token=YOUR_API_TOKEN&fmt=json"
```

### List Symbols for Exchange

All NASDAQ symbols:

```bash
curl "https://eodhd.com/api/exchange-symbol-list/NASDAQ?api_token=YOUR_API_TOKEN&fmt=json"
```

## Options Data

### Get Options Contracts

```bash
curl "https://eodhd.com/api/mp/unicornbay/options/contracts?api_token=YOUR_API_TOKEN&symbol=AAPL.US&fmt=json"
```

### Get Options EOD Data

```bash
curl "https://eodhd.com/api/mp/unicornbay/options/eod?api_token=YOUR_API_TOKEN&symbol=AAPL.US&date=2024-01-15&fmt=json"
```

### Get Underlying Symbols

```bash
curl "https://eodhd.com/api/mp/unicornbay/options/underlying-symbols?api_token=YOUR_API_TOKEN&fmt=json"
```

## News & Sentiment

### Get Latest News

All news:

```bash
curl "https://eodhd.com/api/news?api_token=YOUR_API_TOKEN&fmt=json"
```

**Response:**
```json
[
  {
    "date": "2024-01-15T14:30:00Z",
    "title": "Apple Announces New Product Line",
    "content": "Apple Inc. today announced...",
    "link": "https://example.com/article",
    "symbols": ["AAPL.US"],
    "tags": ["Technology", "Consumer Electronics"],
    "sentiment": {
      "polarity": 0.75,
      "sentiment": "positive"
    }
  }
]
```

Filter by symbol:

```bash
curl "https://eodhd.com/api/news?api_token=YOUR_API_TOKEN&s=AAPL.US&fmt=json"
```

Filter by date range:

```bash
curl "https://eodhd.com/api/news?api_token=YOUR_API_TOKEN&from=2024-01-01&to=2024-01-31&fmt=json"
```

Limit results:

```bash
curl "https://eodhd.com/api/news?api_token=YOUR_API_TOKEN&limit=10&offset=0&fmt=json"
```

### Get Sentiment Analysis

```bash
curl "https://eodhd.com/api/sentiments?api_token=YOUR_API_TOKEN&s=AAPL.US&from=2024-01-01&to=2024-01-31&fmt=json"
```

### Get News Word Weights

```bash
curl "https://eodhd.com/api/news-word-weights?api_token=YOUR_API_TOKEN&s=AAPL.US&fmt=json"
```

## Technical Analysis

### Get Technical Indicators

```bash
curl "https://eodhd.com/api/technical/AAPL.US?api_token=YOUR_API_TOKEN&function=sma&period=50&fmt=json"
```

Available functions:
- `sma` - Simple Moving Average
- `ema` - Exponential Moving Average
- `wma` - Weighted Moving Average
- `rsi` - Relative Strength Index
- `macd` - Moving Average Convergence Divergence
- `bbands` - Bollinger Bands
- `stoch` - Stochastic Oscillator
- `adx` - Average Directional Index

Multiple indicators:

```bash
curl "https://eodhd.com/api/technical/AAPL.US?api_token=YOUR_API_TOKEN&function=sma&period=50&from=2024-01-01&to=2024-12-31&fmt=json"
```

## Screening & Search

### Search for Symbols

Search by name or ticker:

```bash
curl "https://eodhd.com/api/search/Tesla?api_token=YOUR_API_TOKEN&fmt=json"
```

**Response:**
```json
[
  {
    "Code": "TSLA",
    "Exchange": "US",
    "Name": "Tesla Inc",
    "Type": "Common Stock",
    "Country": "USA",
    "Currency": "USD",
    "ISIN": "US88160R1014"
  }
]
```

### Screen Stocks

Screen by criteria:

```bash
curl "https://eodhd.com/api/screener?api_token=YOUR_API_TOKEN&filters=[[%22market_capitalization%22,%22%3E%22,1000000000],[%22pe_ratio%22,%22%3C%22,30]]&fmt=json"
```

Parameters:
- Market cap > $1B
- P/E ratio < 30

## Economic Data

### Get Economic Events

```bash
curl "https://eodhd.com/api/economic-events?api_token=YOUR_API_TOKEN&from=2024-01-01&to=2024-01-31&fmt=json"
```

### Get Macro Indicators

US GDP:

```bash
curl "https://eodhd.com/api/macro-indicator/USA?api_token=YOUR_API_TOKEN&indicator=gdp_current_usd&fmt=json"
```

Available indicators include:
- `gdp_current_usd` - GDP
- `inflation_consumer_prices_annual` - Inflation rate
- `unemployment_total` - Unemployment rate
- And many more...

## Corporate Actions

### Symbol Change History

```bash
curl "https://eodhd.com/api/symbol-change-history?api_token=YOUR_API_TOKEN&from=2024-01-01&to=2024-12-31&fmt=json"
```

### Insider Transactions

```bash
curl "https://eodhd.com/api/insider-transactions?api_token=YOUR_API_TOKEN&code=AAPL.US&limit=100&fmt=json"
```

## Other Features

### Get Company Logo

```bash
curl "https://eodhd.com/api/logo/AAPL.US?api_token=YOUR_API_TOKEN" > apple_logo.png
```

Returns 200x200 PNG with transparent background.

### Get User Account Info

```bash
curl "https://eodhd.com/api/internal-user?api_token=YOUR_API_TOKEN"
```

## Error Handling

### Rate Limiting

When rate limited, response includes:

```http
HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
Retry-After: 60
```

### Error Response Format

```json
{
  "status": 401,
  "error": "Unauthorized",
  "message": "Invalid API token"
}
```

### Common Status Codes

- `200` - Success
- `400` - Bad Request (invalid parameters)
- `401` - Unauthorized (invalid token)
- `403` - Forbidden (subscription doesn't include this endpoint)
- `404` - Not Found (symbol or resource doesn't exist)
- `429` - Too Many Requests (rate limit exceeded)
- `500` - Internal Server Error

## Best Practices

### 1. Use Date Filters

Always specify date ranges to get relevant data:

```bash
# Good
curl "https://eodhd.com/api/eod/AAPL.US?api_token=YOUR_API_TOKEN&from=2024-01-01&to=2024-12-31"

# Less efficient
curl "https://eodhd.com/api/eod/AAPL.US?api_token=YOUR_API_TOKEN"
```

### 2. Choose the Right Format

Use JSON for programmatic access, CSV for analysis:

```bash
# JSON for apps
&fmt=json

# CSV for spreadsheets
&fmt=csv
```

### 3. Batch Requests

For multiple symbols, use bulk endpoints when available:

```bash
# Efficient - bulk endpoint
curl "https://eodhd.com/api/eod-bulk-last-day/US?api_token=YOUR_API_TOKEN"

# Less efficient - multiple individual requests
curl "https://eodhd.com/api/eod/AAPL.US?api_token=YOUR_API_TOKEN"
curl "https://eodhd.com/api/eod/MSFT.US?api_token=YOUR_API_TOKEN"
```

### 4. Cache Responses

Cache EOD data since it doesn't change after market close:

```python
import requests
from datetime import datetime

def get_eod_cached(symbol, date):
    cache_key = f"{symbol}_{date}"
    # Check cache first
    if cache_key in cache:
        return cache[cache_key]

    # Fetch from API
    response = requests.get(
        f"https://eodhd.com/api/eod/{symbol}",
        params={"api_token": "YOUR_TOKEN", "from": date, "to": date}
    )

    # Cache the result
    cache[cache_key] = response.json()
    return cache[cache_key]
```

### 5. Handle Rate Limits

Implement exponential backoff:

```python
import time
import requests

def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            time.sleep(retry_after)
            continue

        response.raise_for_status()

    raise Exception("Max retries exceeded")
```

## Integration Examples

### Python

```python
import requests

class EODHDClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://eodhd.com/api"

    def get_eod(self, symbol, from_date=None, to_date=None):
        params = {"api_token": self.api_token, "fmt": "json"}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = requests.get(f"{self.base_url}/eod/{symbol}", params=params)
        response.raise_for_status()
        return response.json()

    def get_real_time(self, symbol):
        params = {"api_token": self.api_token, "fmt": "json"}
        response = requests.get(f"{self.base_url}/real-time/{symbol}", params=params)
        response.raise_for_status()
        return response.json()

# Usage
client = EODHDClient("YOUR_API_TOKEN")
prices = client.get_eod("AAPL.US", "2024-01-01", "2024-12-31")
quote = client.get_real_time("AAPL.US")
```

### JavaScript/Node.js

```javascript
const axios = require('axios');

class EODHDClient {
  constructor(apiToken) {
    this.apiToken = apiToken;
    this.baseUrl = 'https://eodhd.com/api';
  }

  async getEOD(symbol, fromDate, toDate) {
    const params = { api_token: this.apiToken, fmt: 'json' };
    if (fromDate) params.from = fromDate;
    if (toDate) params.to = toDate;

    const response = await axios.get(`${this.baseUrl}/eod/${symbol}`, { params });
    return response.data;
  }

  async getRealTime(symbol) {
    const params = { api_token: this.apiToken, fmt: 'json' };
    const response = await axios.get(`${this.baseUrl}/real-time/${symbol}`, { params });
    return response.data;
  }
}

// Usage
const client = new EODHDClient('YOUR_API_TOKEN');
const prices = await client.getEOD('AAPL.US', '2024-01-01', '2024-12-31');
const quote = await client.getRealTime('AAPL.US');
```

## Resources

- [OpenAPI Specification](openapi.yaml)
- [API Documentation](https://eodhd.com/financial-apis/)
- [Get API Token](https://eodhd.com/register)
- [Support](mailto:support@eodhd.com)

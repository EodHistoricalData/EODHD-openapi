# Quick Start Guide

Get up and running with the EODHD OpenAPI Specification in minutes.

## Prerequisites

- **Node.js** (v14 or higher) - For validation and previewing
- **Python 3.7+** - For regenerating specs (optional)
- **Git** - For version control

## Installation

### 1. Clone or Download

```bash
# If this is a Git repository
git clone https://github.com/yourusername/eodhd-openapi-spec.git
cd eodhd-openapi-spec

# Or download and extract the ZIP
```

### 2. Install Dependencies

```bash
npm install
```

This installs:
- `@redocly/cli` - For validation and preview
- `@openapitools/openapi-generator-cli` - For code generation

## Quick Commands

### View the Specification

Open `openapi.yaml` in:
- **VS Code**: Install "OpenAPI (Swagger) Editor" extension
- **Swagger Editor**: https://editor.swagger.io/
- **Command line**:
  ```bash
  npm run preview
  ```
  Then visit http://localhost:8080

### Validate the Specification

```bash
npm run validate
# or
bash validate.sh
```

### Generate Client Code

```bash
# Python client
npm run generate-python

# TypeScript client
npm run generate-typescript

# Java client
npm run generate-java

# Go client
npm run generate-go
```

Clients will be generated in `./clients/<language>/`

## Using the API

### Get an API Token

1. Register at https://eodhd.com/register
2. Get your API token from the dashboard
3. Use it in all requests: `?api_token=YOUR_TOKEN`

### Example: Get Stock Prices

```bash
# Get historical EOD data
curl "https://eodhd.com/api/eod/AAPL.US?api_token=YOUR_TOKEN&from=2024-01-01&to=2024-12-31&fmt=json"

# Get real-time quote
curl "https://eodhd.com/api/real-time/AAPL.US?api_token=YOUR_TOKEN&fmt=json"

# Get fundamental data
curl "https://eodhd.com/api/fundamentals/AAPL.US?api_token=YOUR_TOKEN"
```

### Example: Python Client

```python
import requests

API_TOKEN = "YOUR_TOKEN"
BASE_URL = "https://eodhd.com/api"

# Get EOD data
response = requests.get(
    f"{BASE_URL}/eod/AAPL.US",
    params={
        "api_token": API_TOKEN,
        "from": "2024-01-01",
        "to": "2024-12-31",
        "fmt": "json"
    }
)

prices = response.json()
print(prices)
```

### Example: JavaScript/Node.js

```javascript
const axios = require('axios');

const API_TOKEN = 'YOUR_TOKEN';
const BASE_URL = 'https://eodhd.com/api';

async function getStockPrice(symbol) {
  const response = await axios.get(`${BASE_URL}/real-time/${symbol}`, {
    params: {
      api_token: API_TOKEN,
      fmt: 'json'
    }
  });
  return response.data;
}

// Usage
getStockPrice('AAPL.US').then(data => console.log(data));
```

## Directory Structure

```
.
├── openapi.yaml           # Main specification (start here)
├── paths/                 # 33 endpoint definitions
├── components/            # Reusable components
│   ├── parameters/        # Common parameters
│   ├── responses/         # Common responses
│   └── schemas/           # Data models (58 schemas)
└── [documentation files]
```

## Common Tasks

### Find an Endpoint

Look in the `paths/` directory or check the main `openapi.yaml` file.

Example endpoints:
- `paths/eod_ticker.yaml` - Historical prices
- `paths/real-time_ticker.yaml` - Real-time quotes
- `paths/fundamentals_ticker.yaml` - Fundamental data
- `paths/calendar_earnings.yaml` - Earnings calendar

### Understand a Data Model

Check `components/schemas/` for data structure definitions.

### Modify an Endpoint

1. Edit the file in `paths/`
2. Validate: `npm run validate`
3. Preview: `npm run preview`
4. Commit changes

### Add a New Endpoint

1. Create a new file in `paths/`
2. Add reference in `openapi.yaml`
3. Validate and test

## Getting Help

- **Documentation**: See [README.md](README.md)
- **Examples**: See [EXAMPLES.md](EXAMPLES.md)
- **API Docs**: https://eodhd.com/financial-apis/
- **Issues**: GitHub Issues

## Next Steps

1. ✅ Browse the [API Examples](EXAMPLES.md)
2. ✅ Read the [full README](README.md)
3. ✅ Check the [Project Structure](STRUCTURE.md)
4. ✅ Generate a client for your language
5. ✅ Start building!

## Quick Reference

| Task | Command |
|------|---------|
| Validate | `npm run validate` |
| Preview | `npm run preview` |
| Generate Python | `npm run generate-python` |
| Generate TypeScript | `npm run generate-typescript` |
| Regenerate specs | `python3 generate_specs.py` |

## Resources

- 📚 [OpenAPI Specification](https://spec.openapis.org/oas/v3.1.0)
- 🔧 [Redocly CLI](https://redocly.com/docs/cli/)
- 🎨 [Swagger Editor](https://editor.swagger.io/)
- 💾 [EODHD API](https://eodhd.com)

---

**Ready to go!** Start exploring the API at https://eodhd.com 🚀

# Contributing to EODHD OpenAPI Specification

Thank you for your interest in contributing to the EODHD OpenAPI Specification!

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/eodhd-openapi-spec.git
   cd eodhd-openapi-spec
   ```
3. **Install dependencies**:
   ```bash
   npm install
   # or
   pip install pyyaml
   ```

## Making Changes

### Modifying Endpoints

Each API endpoint has its own file in the `paths/` directory:

1. Find the relevant endpoint file (e.g., `paths/eod_{ticker}.yaml`)
2. Make your changes following OpenAPI 3.1.0 specification
3. Update descriptions, parameters, or response schemas as needed

### Adding New Schemas

To add a new data schema:

1. Create a new file in `components/schemas/` (e.g., `NewSchema.yaml`)
2. Define your schema following JSON Schema 2020-12 format:
   ```yaml
   NewSchema:
     type: object
     properties:
       field1:
         type: string
         description: Description of field1
       field2:
         type: number
         description: Description of field2
     required:
       - field1
   ```
3. Reference it in `components/index.yaml`:
   ```yaml
   schemas:
     NewSchema:
       $ref: './schemas/NewSchema.yaml#/NewSchema'
   ```

### Adding Parameters or Responses

Follow the same pattern as schemas:

1. Create file in `components/parameters/` or `components/responses/`
2. Update `components/index.yaml` with the reference

## Validation

Always validate your changes before submitting:

```bash
# Using npm script
npm run validate

# Using shell script
bash validate.sh

# Using Redocly CLI directly
npx @redocly/cli lint openapi.yaml
```

## Testing

### Preview Documentation

Preview the specification in a browser:

```bash
npm run preview
```

This will start a local server at `http://localhost:8080`

### Test Code Generation

Ensure client code can be generated:

```bash
# Python client
npm run generate-python

# TypeScript client
npm run generate-typescript
```

## Code Style

### YAML Formatting

- Use 2 spaces for indentation
- No trailing whitespace
- UTF-8 encoding
- Unix line endings (LF)

### Descriptions

- Write clear, concise descriptions
- Use proper grammar and punctuation
- Include examples where helpful
- Document all required vs optional fields

### Examples

Always provide examples for:
- Request parameters
- Request bodies
- Response bodies

Example format:
```yaml
examples:
  example1:
    summary: Basic example
    value:
      field1: "value1"
      field2: 123
```

## Commit Guidelines

### Commit Messages

Follow conventional commit format:

```
type(scope): subject

body (optional)

footer (optional)
```

**Types**:
- `feat`: New feature or endpoint
- `fix`: Bug fix or correction
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(endpoints): add new options data endpoint

docs(readme): update authentication section

fix(schemas): correct InternalUser schema property types
```

### Branch Naming

Use descriptive branch names:
- `feature/add-new-endpoint`
- `fix/correct-schema-definition`
- `docs/update-examples`

## Pull Request Process

1. **Create a descriptive PR title** following commit message format
2. **Describe your changes** in the PR description:
   - What changed?
   - Why was it changed?
   - How was it tested?
3. **Link related issues** if applicable
4. **Ensure validation passes**:
   - Run `npm run validate`
   - Fix any linting errors
5. **Request review** from maintainers
6. **Address feedback** if requested
7. **Wait for approval** before merging

## Pull Request Checklist

- [ ] Changes follow OpenAPI 3.1.0 specification
- [ ] All files use consistent formatting (2-space indentation)
- [ ] Validation passes (`npm run validate`)
- [ ] Documentation is updated if needed
- [ ] Examples are provided for new endpoints/schemas
- [ ] Commit messages follow conventional format
- [ ] Branch is up to date with main

## Questions?

If you have questions or need help:

1. Check existing [Issues](https://github.com/yourusername/eodhd-openapi-spec/issues)
2. Review the [OpenAPI Specification](https://spec.openapis.org/oas/v3.1.0)
3. Open a new issue with your question

## Resources

- [OpenAPI 3.1.0 Specification](https://spec.openapis.org/oas/v3.1.0)
- [JSON Schema 2020-12](https://json-schema.org/specification.html)
- [Redocly CLI Documentation](https://redocly.com/docs/cli/)
- [EODHD API Documentation](https://eodhd.com/financial-apis/)

## Code of Conduct

Please be respectful and professional in all interactions. We aim to maintain a welcoming and inclusive community.

Thank you for contributing! 🎉

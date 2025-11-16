# TODO API - Stepwise Plugin Validation Project

> 🔬 **Validation project** for [stepwise-dev](https://github.com/nikeyes/stepwise-dev) - Claude Code plugin that implements the Research → Plan → Implement → Validate workflow

Simple REST API built with FastAPI to validate the stepwise plugin workflow.

## About This Project

This project is a testing laboratory to validate the **[stepwise-dev](https://github.com/nikeyes/stepwise-dev)** plugin, which structures development in four phases to maintain coherence in complex implementations.

**Why does this project exist?**
- Test the complete stepwise-dev cycle with a real API
- Validate that the workflow works with features of different complexities
- Document best practices for using the plugin

📋 **[See complete features roadmap →](STEPWISE_FEATURES.md)**

## Features

### ✅ Implemented Endpoints

- `GET /` - API information and endpoint list
- `GET /todos` - List all todos
- `GET /todos/{id}` - Get a specific todo
- `POST /todos` - Create a new todo

### 🚧 Intentionally Incomplete Endpoints

These endpoints are stubs that return `501 Not Implemented`:

- `PATCH /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a todo
- `GET /todos/search?q=...` - Search/filter todos

### ❌ Not Implemented Features

- Rate limiting middleware
- Request validation beyond basic Pydantic models
- Data persistence (in-memory only)
- Authentication/Authorization

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

## Quick Start

```bash
# Install dependencies
make install

# Run development server
make run

# Run tests
make test

# Lint code
make lint

# Format code
make format
```

## API Usage Examples

### Create a todo

```bash
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

### List all todos

```bash
curl http://localhost:8000/todos
```

### Get a specific todo

```bash
curl http://localhost:8000/todos/1
```

### Try incomplete endpoints (returns 501)

```bash
# Update - NOT IMPLEMENTED
curl -X PATCH http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete - NOT IMPLEMENTED
curl -X DELETE http://localhost:8000/todos/1

# Search - NOT IMPLEMENTED
curl http://localhost:8000/todos/search?q=groceries
```

## Interactive API Documentation

Open http://localhost:8000/docs in your browser for interactive Swagger UI documentation.

## Project Structure

```
.
├── README.md                    # This file - Quick guide
├── STEPWISE_FEATURES.md         # Detailed feature analysis for stepwise-dev
├── Makefile                     # Development commands
├── pyproject.toml               # Configuration and dependencies
├── src/
│   └── todo_api/
│       ├── __init__.py
│       ├── main.py              # FastAPI app and endpoints
│       ├── models.py            # Pydantic models
│       └── storage.py           # In-memory storage
└── tests/
    ├── __init__.py
    └── test_api.py              # Test suite
```

## Stepwise-Dev Workflow

This project is designed to validate the 4-phase stepwise-dev cycle:

| Phase | Description | Example in this project |
|-------|-------------|-------------------------|
| **🔍 Research** | Explore codebase and understand context | Investigate incomplete endpoints, analyze current storage |
| **📋 Plan** | Create detailed implementation plan | Design JWT authentication, plan DB migration |
| **⚙️ Implement** | Execute phase by phase with validations | Implement endpoints, add middleware |
| **✅ Validate** | Systematically verify complete implementation | Run tests, verify integration |

**Key benefit**: Context is cleared between phases and persisted in `thoughts/`, preventing the LLM from losing attention on complex projects.

### Features to Validate

#### 🎯 Simple (implement directly)
- `PATCH /todos/{id}` - Update todo
- `DELETE /todos/{id}` - Delete todo
- `GET /todos/search` - Basic search

#### 🚀 Complex (ideal for stepwise-dev)
- 🔐 **Authentication/Authorization** - JWT, OAuth2, permissions
- 💾 **Data Persistence** - SQLAlchemy, migrations, transactions
- ⏱️ **Rate Limiting** - Middleware, strategies, headers
- 🔍 **Advanced Search + Tags** - Full-text search, filters, categories

📖 **[See detailed analysis of each feature →](STEPWISE_FEATURES.md)**

## Development Roadmap

Features prioritized for implementation with stepwise-dev:

1. **🔐 Authentication** (Priority: High) - Foundation for ownership and permissions
2. **💾 Persistence** (Priority: High) - Fundamental architectural change
3. **⏱️ Rate Limiting** (Priority: Medium) - Production middleware
4. **🔍 Search + Tags** (Priority: Medium) - UX improvements

**See details**: [STEPWISE_FEATURES.md](STEPWISE_FEATURES.md) includes complexity analysis, architectural decisions, and specific steps for each feature.

## Testing

Tests are written using pytest and cover:
- All implemented endpoints
- Validation rules
- Error cases (404, 422)
- Stub endpoints (verify 501 responses)

Run with:
```bash
make test
```

## Development

```bash
# Install dev dependencies
make install

# Run linter
make lint

# Format code
make format

# Clean cache files
make clean
```

## License

MIT

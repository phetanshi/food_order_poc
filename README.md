# Food Order PoC

This project contains a minimal FastAPI application skeleton for a food ordering conversational assistant.

## Structure

- app/api: API endpoints
- app/core: configuration, logging, prompts
- app/db: database setup and models
- app/repositories: data access layers
- app/services: business logic services
- app/schemas: request/response schemas
- app/utils: helper utilities

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --env-file .env.dev
```

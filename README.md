# 🍽️ AI Food Ordering Chatbot (FastAPI + Hugging Face)

A lightweight AI-powered food ordering backend built using **FastAPI**, **Python**, **SQLAlchemy**, and the **Hugging Face Inference API**.

This project demonstrates how to integrate a Large Language Model (LLM) into a real-world application while keeping all business logic inside the backend.

The LLM is responsible **only** for:

- Understanding user intent
- Extracting structured information from natural language

The backend is responsible for:

- Menu validation
- Cart management
- Price calculation
- Order placement
- Database operations
- Transaction management
- Conversation state management

This project intentionally does **not** use LangChain, DialogFlow, Rasa, Botpress, or any chatbot framework.

---

# Features

- AI-powered natural language ordering
- Multi-turn conversations
- Conversation memory per user session
- Menu validation
- Shopping cart management
- Order placement
- SQL Server persistence
- Hugging Face Inference API integration
- Clean Architecture
- Fully asynchronous implementation
- SQLAlchemy 2.x
- Alembic database migrations
- Production-style project structure

---

# Technology Stack

| Technology | Version |
|------------|---------|
| Python | 3.13+ |
| FastAPI | Latest |
| SQLAlchemy | 2.x |
| Alembic | Latest |
| Microsoft SQL Server | Latest |
| Hugging Face Inference API | Latest |
| Pydantic | v2 |
| AsyncIO | Built-in |

---

# Project Structure

```text
app
│
├── api
│
├── core
│
├── db
│
├── domain
│
├── dto
│
├── exceptions
│
├── prompts
│
├── repositories
│
├── services
│   ├── handlers
│   └── ...
│
├── conversation
│
├── dispatcher
│
├── dependencies.py
│
└── main.py

tests

alembic

requirements.txt
```

---

# Architecture

```
                User
                  │
                  ▼
          FastAPI Controller
                  │
                  ▼
            Chat Service
                  │
                  ▼
        Conversation Manager
                  │
                  ▼
        Hugging Face Service
                  │
                  ▼
        Intent + Entity Extraction
                  │
                  ▼
         Intent Dispatcher
                  │
                  ▼
         Intent Handlers
                  │
                  ▼
     Business Services
                  │
                  ▼
        Repository Layer
                  │
                  ▼
           SQL Server
```

---

# Supported Intents

- GREETING
- SHOW_MENU
- ADD_ITEM
- REMOVE_ITEM
- UPDATE_QUANTITY
- SHOW_CART
- SHOW_TOTAL
- CONFIRM_ORDER
- CANCEL_ORDER
- END_CONVERSATION
- UNKNOWN

---

# Database

The application uses three tables.

## FoodItem

Stores menu items.

## Order

Stores customer orders.

## FoodItemOrder

Stores ordered food items.

---

# Setup

## Clone Repository

```bash
git clone <repository-url>

cd food-order-poc
```

---

# Create Virtual Environment

```bash
python -m venv .venv
```

---

# Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

---

# Upgrade pip

```bash
python.exe -m pip install --upgrade pip
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment

Create a `.env.dev` file.

Example:

```text
APP_NAME=Food Ordering AI_DEV

LLM_PROVIDER=huggingface

HF_API_KEY=YOUR_API_KEY

HF_MODEL=Qwen/Qwen2.5-7B-Instruct

DB_SERVER=YOUR_SERVER

DB_DATABASE=FoodOrderPoc

DB_USERNAME=YOUR_USERNAME

DB_PASSWORD=YOUR_PASSWORD
```

---

# Database Migration

Generate migration

```bash
alembic revision --autogenerate -m "Initial database schema"
```

Apply migration

```bash
alembic upgrade head
```

---

# Run Application

```bash
uvicorn app.main:app --reload --env-file .env.dev
```

---

# Swagger UI

```
http://localhost:8000/docs
```

---

# Sample Request

POST

```
/api/chat
```

Request

```json
{
    "session_id":"user-001",
    "message":"Add two chicken biryanis"
}
```

Example Response

```json
{
    "reply":"I've added the requested items to your cart.",
    "cart":{
        "items":[
            {
                "food_item_id":4,
                "food_item_name":"Chicken Biryani",
                "quantity":2,
                "unit_price":"35.00",
                "total_price":"70.00"
            }
        ],
        "total":"70.00"
    }
}
```

---

# Conversation Example

```
User:
Hello

Bot:
Welcome to Nahansh Food Services.

------------------------------------

User:
Add two chicken biryanis

------------------------------------

User:
Add one Coke

------------------------------------

User:
Remove one biryani

------------------------------------

User:
Show my cart

------------------------------------

User:
Place my order
```

---

# Design Principles

- Clean Architecture
- SOLID Principles
- Dependency Injection
- Repository Pattern
- DTO Pattern
- Stateless Services
- Async Programming
- Separation of Concerns

---

# LLM Responsibilities

The LLM is responsible only for:

- Intent Detection
- Entity Extraction
- Understanding natural language

The LLM **never**:

- Calculates prices
- Validates menu items
- Creates orders
- Accesses the database
- Performs business logic

---

# Backend Responsibilities

The backend performs:

- Menu validation
- Cart management
- Quantity validation
- Price calculation
- Order creation
- SQL transactions
- Exception handling
- Conversation management

---

# Development Workflow

After changing SQLAlchemy models:

```bash
alembic revision --autogenerate -m "Description"

alembic upgrade head
```

Run the application

```bash
uvicorn app.main:app --reload --env-file .env.dev
```

---

# Running Tests

```bash
pytest
```

---

# Future Enhancements

- Authentication
- Redis conversation storage
- Streaming responses
- WebSocket support
- Docker support
- Kubernetes deployment
- Payment gateway integration
- Menu recommendation engine
- Order history
- Admin portal

---

# License

This project is intended for learning and demonstration purposes.
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.api import api_response
from app.core.config import get_settings
from fastapi import APIRouter, Depends
from app.exceptions.handlers import register_exception_handlers
from app.repositories import FoodRepository
from app.dependencies import get_food_repository
from app.api.chat_controller import chat_router
from app.api.menu_controller import menu_router
from app.api.health_controller import health_router


app = FastAPI(title="Food Ordering AI", version="1.0.0")
settings = get_settings()
router = APIRouter()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup/shutdown.
    """
    print("========================================")
    print(" Nahansh Food Ordering API Started")
    print("========================================")

    yield

    print("========================================")
    print(" Nahansh Food Ordering API Stopped")
    print("========================================")


app = FastAPI(
    title="Nahansh Food Ordering AI",
    description="AI powered food ordering backend using FastAPI and Hugging Face.",
    version="1.0.0",
    lifespan=lifespan,
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

# -------------------------
# CORS
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routers
# -------------------------

app.include_router(chat_router)
app.include_router(menu_router)
app.include_router(health_router)

# -------------------------
# Exception Handlers
# -------------------------

register_exception_handlers(app)
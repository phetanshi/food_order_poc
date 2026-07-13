from functools import lru_cache
import os
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=f".env.{os.getenv('ENV', 'dev')}", env_file_encoding="utf-8", extra="ignore")

    app_name: str = Field(default="food-order-chatbot")
    app_env: str = Field(default="development")
    debug: bool = Field(default=True)

    llm_provider: Literal["openai", "huggingface"] = Field(default="openai")
    

    openai_api_key: str | None = Field(default=None)
    openai_base_url: str = Field(default="https://api.openai.com/v1")
    openai_model: str = Field(default="gpt-4o-mini")

    # Hugging Face Inference API settings
    hf_api_key: str | None = Field(default=None)
    hf_model: str = Field(default="mistralai/Mistral-7B-Instruct-v0.1")

    db_server: str = Field(default="PSN_AI")
    db_database: str = Field(default="FoodOrderPoc")
    db_username: str = Field(default="sa")
    db_password: str = Field(default="pwd")

@lru_cache
def get_settings() -> Settings:
    return Settings()
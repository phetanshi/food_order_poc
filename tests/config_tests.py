import os
import pytest
from app.core.config import Settings


def test_default_settings():
    """
    Verifies that default values are used when
    no environment variables are supplied.
    """

    settings = Settings(_env_file=None)
    assert settings.app_name == "Food-order-chatbot"
    assert settings.app_env == "development"
    assert settings.openai_model == "gpt-4o-mini"
    assert settings.hf_model == "Qwen/Qwen2.5-7B-Instruct"
    assert settings.db_server == "PSN_AI"
    assert settings.db_database == "FoodOrderPoc"

def test_default_settings():
    settings = Settings(_env_file=None)
    print()
    print("App Name      :", settings.app_name)
    print("App Env       :", settings.app_env)
    print("LLM Provider  :", settings.llm_provider)
    print("HF Model      :", settings.hf_model)
    print("DB Server     :", settings.db_server)
    print()
    assert settings.app_name == "food-order-chatbot"

def test_load_env_dev():
    """
    Verifies values are loaded from .env.dev
    """

    settings = Settings(_env_file=".env.dev")
    assert settings.app_name == "Food Ordering AI_DEV"
    assert settings.llm_provider == "huggingface"
    assert settings.hf_model == "Qwen/Qwen2.5-7B-Instruct"
    assert settings.db_server == "PSN_AI"
    assert settings.db_database == "FoodOrderPoc"


def test_environment_variables_override(monkeypatch):

    """
    Environment variables should override .env values.
    """
    monkeypatch.setenv("HF_MODEL", "test-model")
    monkeypatch.setenv("LLM_PROVIDER", "huggingface")
    settings = Settings(_env_file=None)
    assert settings.hf_model == "test-model"
    assert settings.llm_provider == "huggingface"
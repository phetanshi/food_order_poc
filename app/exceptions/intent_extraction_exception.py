from app.exceptions.llm_exception import LLMException


class IntentExtractionException(LLMException):
    """Failed to extract intent."""
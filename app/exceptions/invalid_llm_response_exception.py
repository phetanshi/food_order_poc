from app.exceptions.llm_exception import LLMException


class InvalidLLMResponseException(LLMException):
    """LLM returned invalid JSON."""
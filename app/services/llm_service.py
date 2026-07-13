from abc import ABC
from abc import abstractmethod
from app.dto import LlmResponse


class LLMService(ABC):

    @abstractmethod
    async def extract_intent(self, conversation: list[str], user_message: str) -> LlmResponse:
        ...
from abc import ABC
from abc import abstractmethod

from app.dto import ChatResult
from app.services.handlers.handler_context import HandlerContext


class BaseIntentHandler(ABC):
    @abstractmethod
    async def handle(self, context: HandlerContext) -> ChatResult:
        ...
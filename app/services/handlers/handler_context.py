from dataclasses import dataclass
from app.domain.conversation import Conversation
from app.domain.resolved_menu_item import ResolvedMenuItem
from app.dto import LlmResponse


@dataclass(slots=True)
class HandlerContext:

    conversation: Conversation
    llm_response: LlmResponse
    resolved_items: list[ResolvedMenuItem]
    unavailable_items: list[str]
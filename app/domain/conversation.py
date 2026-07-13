from dataclasses import dataclass, field
from datetime import datetime

from app.domain.cart import Cart
from app.domain.chat_message import ChatMessage, Role


@dataclass(slots=True)
class Conversation:
    session_id: str
    cart: Cart
    history: list[ChatMessage] = field(default_factory=list)

    MAX_HISTORY = 10

    def add_user_message(self, message: str) -> None:
        """
        Add a user message to the conversation history.
        """
        self.history.append(ChatMessage(role=Role.USER, content=message.strip(), created_at=datetime.now()))

    def add_assistant_message(self, message: str) -> None:
        """
        Add an assistant message to the conversation history.
        """
        self.history.append(ChatMessage(role=Role.ASSISTANT, content=message.strip(), created_at=datetime.now()))
        

    def clear_history(self) -> None:
        """
        Clear conversation history while keeping the cart.
        """
        self.history.clear()

    def to_prompt(self) -> list[dict[str, str]]:
        """
        Convert the last N messages into the format expected by
        Hugging Face/OpenAI chat completion APIs.
        """

        messages: list[dict[str, str]] = []
        history = self.history[-self.MAX_HISTORY :]
        for msg in history:
            messages.append(
                {
                    "role": msg.role.value,
                    "content": msg.content,
                }
            )

        return messages
    
    def to_messages(self, system_prompt: str) -> list[dict[str, str]]:
        messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]
        messages.extend(self.to_prompt())
        return messages
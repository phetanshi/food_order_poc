from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"


@dataclass
class ChatMessage:
    role: Role
    content: str
    created_at: datetime
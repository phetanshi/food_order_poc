from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    session_id: str = Field(
        ...,
        description="Unique conversation/session identifier",
        examples=["user-001"],
    )

    message: str = Field(
        ...,
        min_length=1,
        description="User's chat message",
        examples=["Add two chicken biryanis"],
    )
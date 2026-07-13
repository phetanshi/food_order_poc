from fastapi import APIRouter
from fastapi import Depends
from app.dto import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

from app.dependencies import get_chat_service

chat_router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)


@chat_router.post("",response_model=ChatResponse)
async def chat(request: ChatRequest, chat_service: ChatService = Depends(get_chat_service)) -> ChatResponse:
    chat_response = await chat_service.process_message(session_id=request.session_id, message=request.message)
    return chat_response
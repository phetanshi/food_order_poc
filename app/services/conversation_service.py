from cachetools import TTLCache
from app.domain.cart import Cart
from app.domain.conversation import Conversation


class ConversationManagerService:
    """
    Manages per-session conversation state.
    This implementation is intentionally simple for the POC.
    Later we can replace the cache with Redis without changing
    the rest of the application.
    """

    def __init__(self, ttl_seconds: int = 1800, max_sessions: int = 10000):
        self._cache = TTLCache(maxsize=max_sessions, ttl=ttl_seconds)

    def get_or_create(self, session_id: str) -> Conversation:
        conversation = self._cache.get(session_id)
        if conversation is None:
            conversation = Conversation(
                session_id=session_id,
                cart=Cart(session_id=session_id)
            )
            self._cache[session_id] = conversation
        return conversation

    def remove(self, session_id: str) -> None:
        self._cache.pop(session_id, None)

    def exists(self, session_id: str) -> bool:
        return session_id in self._cache
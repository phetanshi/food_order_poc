from huggingface_hub import AsyncInferenceClient

from app.core.config import get_settings
from app.dto import LlmResponse
from app.prompts import SYSTEM_PROMPT, PromptBuilder
from app.services.llm_service import LLMService
from app.utils.json_parser import extract_json

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

from app.core.logging import logger

settings = get_settings()



class HuggingFaceService(LLMService):
    def __init__(self):
        self.client = AsyncInferenceClient(api_key=settings.hf_api_key)
        self.prompter = PromptBuilder()
    
    @retry(
            stop=stop_after_attempt(3), 
            wait=wait_exponential(min=1, max=8), 
            reraise=True
            )
    async def extract_intent(self, conversation_history: list[dict], user_message: str) -> LlmResponse:
        try:
            messages = self.prompter.get_prompt(conversation_history, user_message)
        
            response = await self.client.chat.completions.create(
                model=settings.hf_model,
                messages=messages,
                temperature=0,
                max_tokens=150,
            )
            content = response.choices[0].message.content
            if isinstance(content, list):
                content = "".join(
                    part.text if hasattr(part, "text") else str(part) 
                    for part in content
                    )
            parsed = extract_json(content)
            llm_response = LlmResponse.model_validate(parsed)
            return llm_response
        except Exception as e:
            logger.exception("LLM Error")
            raise e
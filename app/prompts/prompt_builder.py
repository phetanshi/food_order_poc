from app.prompts.intent_extraction_prompt import INTENT_EXTRACTION_PROMPT_TEMPLATE
from app.prompts.system_prompt import SYSTEM_PROMPT

class PromptBuilder:
    def build_extraction_prompt(self, 
        history: str,
        message: str,
    ) -> str:

        return INTENT_EXTRACTION_PROMPT_TEMPLATE.format(
            history=history,
            message=message,
        )
    
    def build_prompt(self, history:list[dict], message:str) -> str:
        history_text = ""
        for item in history[-10:]:
            history_text += (
                f"{item['role'].capitalize()}: "
                f"{item['content']}\n"
            )
        return self.build_extraction_prompt(
            history=history_text,
            message=message,
        )
    
    def get_prompt(self, conversation_history: list[dict], user_message: str) -> str:
        prompt = self.build_prompt(conversation_history, user_message)
        messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        return messages


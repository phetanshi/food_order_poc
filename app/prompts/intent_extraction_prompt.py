INTENT_EXTRACTION_PROMPT_TEMPLATE = """
Conversation History

{history}

----------------------------------------

Latest User Message

{message}

----------------------------------------

Instructions

Analyze ONLY the Latest User Message.

Use the Conversation History ONLY to resolve references such as:

- another one
- one more
- remove it
- make it three

Never extract food items from previous messages.

Return ONLY valid JSON.

Do not return markdown.

Do not explain anything.
"""
import json
import re


def extract_json(text: str):
    text = text.strip()
    # Remove markdown fences
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = text.replace("```", "")
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found.")

    return json.loads(match.group())
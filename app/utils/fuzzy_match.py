from rapidfuzz import process
from rapidfuzz import fuzz


class FuzzyMatcher:
    @staticmethod
    def find_best_match(user_input: str,choices: list[str], minimum_score: int = 70) -> str | None:

        if not choices:
            return None

        result = process.extractOne(
            query=user_input,
            choices=choices,
            scorer=fuzz.WRatio
        )

        if result is None:
            return None

        match, score, _ = result
        if score < minimum_score:
            return None

        return match
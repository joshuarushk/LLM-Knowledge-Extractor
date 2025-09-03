from .base import Step


POSITIVE_WORDS = {"good", "great", "excellent", "positive", "happy", "success"}
NEGATIVE_WORDS = {"bad", "poor", "negative", "sad", "fail", "problem"}

class SentimentStep(Step):
    def run(self, data: dict) -> dict:
        text = data.get("text", "").lower()

        score = 0
        for word in POSITIVE_WORDS:
            if word in text:
                score += 1
        for word in NEGATIVE_WORDS:
            if word in text:
                score -= 1

        if score > 0:
            sentiment = "positive"
        elif score < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        # Only override if LLM didn’t provide sentiment
        if "sentiment" not in data or not data["sentiment"]:
            data["sentiment"] = sentiment
        else:
            data["sentiment_fallback"] = sentiment  # store as comparison

        return data

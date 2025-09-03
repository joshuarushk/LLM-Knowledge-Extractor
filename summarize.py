import os, json
from openai import OpenAI
from .base import Step

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SummarizeStep(Step):
    def run(self, data: dict) -> dict:
        text = data["text"]
        prompt = f"""
        Summarize and extract metadata:
        ---
        {text}
        ---
        Return JSON with summary, title, topics, sentiment.
        """
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        content = resp.choices[0].message.content
        metadata = json.loads(content)
        data.update(metadata)
        return data

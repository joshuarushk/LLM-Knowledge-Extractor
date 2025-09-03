from app.pipeline.summarize import SummarizeStep
from app.pipeline.keywords import KeywordStep
from app.pipeline.sentiment import SentimentStep

def build_pipeline():
    return [
        SummarizeStep(),
        KeywordStep(),
        SentimentStep() 
    ]

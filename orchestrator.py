from app.pipeline.summarize import SummarizeStep
from app.pipeline.keywords import KeywordStep
from app.pipeline.sentiment import SentimentStep
from app.pipeline.storage import StorageStep

def build_pipeline():
    return [
        SummarizeStep(),
        KeywordStep(),
        SentimentStep(),
        StorageStep() 
    ]

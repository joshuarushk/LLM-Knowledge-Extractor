from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import run_pipeline

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(input: InputText):
    result = run_pipeline(input.text)
    return result

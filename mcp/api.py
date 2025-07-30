from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

from models.ollama_client import OllamaClient
from agents.orchestrator import Orchestrator

app = FastAPI()

llm_client = OllamaClient()
orchestrator = Orchestrator(llm_client)

class FileRegistrationRequest(BaseModel):
    path: str

class RefactorRequest(BaseModel):
    instruction: str

@app.post("/register-file/")
def register_file(req: FileRegistrationRequest):
    path = req.path
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found.")
    try:
        agent = orchestrator.register_file(path)
        return {"message": f"Registered agent for {path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/summarize/")
def summarize_all():
    try:
        summaries = orchestrator.summarize_all()
        return summaries
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/refactor/")
def refactor_code(req: RefactorRequest):
    try:
        results = orchestrator.refactor_all(req.instruction)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
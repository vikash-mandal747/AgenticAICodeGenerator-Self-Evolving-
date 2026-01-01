import os
from fastapi import FastAPI
from pydantic import BaseModel
from run_engine import run_agentic_system
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # frontend will be on different domain
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    instruction: str

@app.post("/generate")
def generate_code(prompt: Prompt):
    output = run_agentic_system(prompt.instruction)
    return {"output": output}

@app.get("/")
def health():
    return {"status": "ok"}

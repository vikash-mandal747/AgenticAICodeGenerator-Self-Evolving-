from fastapi import FastAPI
from pydantic import BaseModel
from run_engine import run_agentic_system
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow frontend (Lovable)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    instruction: str

@app.post("/generate")
def generate_code(prompt: Prompt):
    result = run_agentic_system(prompt.instruction)
    return {"output": result}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from run_engine import run_agentic_system

app = FastAPI(title="Code Generator Agent API")

# Allow frontend (React, etc.) to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Prompt(BaseModel):
    user_instruction: str


@app.get("/")
def root():
    return {"message": "Welcome to your Code Generator Agent API!"}


@app.post("/generate")
def generate_code(prompt: Prompt):
    """
    Receives user prompt and returns generated code.
    The code is also auto-saved in output folder.
    """
    code_output = run_agentic_system(prompt.user_instruction)
    return {"generated_code": code_output}

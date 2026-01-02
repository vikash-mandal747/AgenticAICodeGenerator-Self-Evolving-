from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from run_engine import run_agentic_system

app = FastAPI()

# CORS settings
# origins = [
#     "http://localhost:8080",  # your React dev server
#     "http://127.0.0.1:8080",
# ]

origins = [
    "*"  # allow all origins for now; you can restrict later to your frontend URL
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow these origins
    allow_credentials=True,
    allow_methods=["*"],    # allow GET, POST, etc.
    allow_headers=["*"],    # allow all headers
)


class InstructionRequest(BaseModel):
    instruction: str


@app.post("/generate")
def generate_code(request: InstructionRequest):
    instruction = request.instruction
    output = run_agentic_system(instruction)
    return {"code": output}

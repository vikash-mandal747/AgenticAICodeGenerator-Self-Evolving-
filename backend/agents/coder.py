from agentic_engine import create_llm

def code_agent(prompt: str) -> str:
    return create_llm(prompt)

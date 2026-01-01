from agentic_engine import create_llm

def run_agentic_system(user_input: str) -> str:
    return create_llm(user_input)

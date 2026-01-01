from agents.coder import code_agent
from agents.reviewer import review_and_improve
from agents.planner import planner_agent
from agentic_engine import create_llm


def self_evolving_workflow(user_instruction: str) -> str:
    # Step 1: Create a plan
    plan = planner_agent(create_llm, user_instruction)

    # Step 2: Generate initial code from plan
    initial_code = code_agent(plan)

    # Step 3: Review and improve the code
    improved_code = review_and_improve(initial_code, plan)

    return improved_code

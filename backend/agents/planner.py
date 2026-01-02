def planner_agent(llm_func, user_instruction):
    """
    Generates a step-by-step plan for the user's coding prompt
    """
    prompt = f"Create a step-by-step plan to build: {user_instruction}"
    return llm_func(prompt)

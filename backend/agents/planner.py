def planner_agent(llm, user_instruction):
    prompt = f"Create a step-by-step plan to build: {user_instruction}"
    return llm.generate(prompt)

def coder_agent(llm, plan):
    prompt = f"Write code based on this plan:\n{plan}"
    return llm.generate(prompt)

def reviewer_agent(llm, instruction, code):
    prompt = f"""
Review and improve the following code.

Instruction:
{instruction}

Code:
{code}
"""
    return llm.generate(prompt)

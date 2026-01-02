from agentic_engine import create_llm


def review_and_improve(code: str, original_prompt: str) -> str:
    review_prompt = f"""
You are a senior code reviewer.

Original task:
{original_prompt}

Generated code:
{code}

Improve the code if needed.
If the code is already good, return it as-is.
Return ONLY code.
"""
    return create_llm(review_prompt)

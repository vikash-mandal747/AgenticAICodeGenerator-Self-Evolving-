from litellm import completion
import os

def create_llm(user_prompt: str) -> str:
    response = completion(
        model="groq/llama-3.1-8b-instant",  # STABLE MODEL
        messages=[
            {
                "role": "system",
                "content": "You are an expert senior software engineer. Generate clean, production-ready code."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3,
        max_tokens=2000,
        api_key=os.getenv("GROQ_API_KEY")
    )

    return response["choices"][0]["message"]["content"]

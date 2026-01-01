import time
from litellm import completion
from litellm.exceptions import RateLimitError


def create_llm(prompt: str):
    """
    Sends the prompt to Groq LLM and retries automatically if rate limit is reached.
    """
    while True:
        try:
            response = completion(
                model="groq/llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful code generator."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            return response["choices"][0]["message"]["content"]

        except RateLimitError as e:
            wait_time = 30  # seconds
            print(
                f"⚠ Rate limit reached. Waiting {wait_time}s before retrying...")
            time.sleep(wait_time)

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            break

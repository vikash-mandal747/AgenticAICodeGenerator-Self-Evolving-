import os
from datetime import datetime
from agentic_engine import create_llm
from workflows.workflow import self_evolving_workflow  # your workflow

OUTPUT_DIR = "output"  # folder to save generated code
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_output(llm_output: str):
    """Save each prompt output in a unique file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
    filename = f"generated_{timestamp}.txt"
    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(llm_output)

    return file_path


def run_agentic_system(user_instruction: str):
    # Run your self-evolving workflow
    llm_output = self_evolving_workflow(user_instruction)

    # Save to unique file
    file_path = save_output(llm_output)

    print(f"\n✅ Output saved to: {file_path}\n")
    print(f"🖥️ Generated Code:\n\n{llm_output}\n{'-'*50}")

    return llm_output

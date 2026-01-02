# AgenticAICodeGenerator-Self-Evolving-

## Agentic AI Code Generator (Self-Evolving)

Build an **Agentic AI system** that takes natural language instructions from a user and autonomously:

* **Plans the task** using multiple agents
* **Generates** working code
* **Verifies and improves** the generated code
* **Outputs** runnable files
* **Provides** a simple UI for interaction

---

# Agentic AI Code Generator

## Overview

This project demonstrates an Agent-based AI system that autonomously generates and improves code from natural language instructions using Large Language Models.

## Key Concepts

* Agentic AI
* Task Planning
* Self-Evolving Agents
* Multi-Agent Workflow

## Architecture

User Instruction → Planner Agent → Code Generator Agent → Code Reviewer Agent → Output Files

## Tech Stack

* Python
* evoagentx
* OpenAI / Anthropic LLMs / Groq
* Lovable UI

## Example

Input:
"print fibonacci series in JS"

Output:
* give code as output

## How to Run

1. Add API keys in `.env`
2. Install dependencies
3. Run `python app.py`
4. python -m venv .venv (create virtual envronemen)
5. .venv\Scripts\activate (activate the environment)
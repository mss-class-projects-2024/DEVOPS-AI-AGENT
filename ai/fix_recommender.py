from ai.ollama_client import ask_llm


def recommend_fix(issue):

    prompt = f"""
You are a Senior DevOps Engineer.

Issue:

{issue}

Provide:

1. Root Cause
2. Impact
3. Recommended Fix
4. Example Configuration
5. Best Practice
"""

    return ask_llm(prompt)
from ai.ollama_client import ask_llm


def explain_repository(report_text):

    prompt = f"""
You are a Senior DevOps Architect.

Analyze the repository report below.

Provide:

1. Project Overview
2. Architecture Summary
3. Technologies Used
4. Deployment Flow
5. Security Risks
6. Improvement Recommendations

Repository Report:

{report_text}
"""

    return ask_llm(prompt)
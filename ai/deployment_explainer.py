from ai.ollama_client import ask_llm


def explain_deployment(report_text):

    prompt = f"""
You are a Senior DevOps Architect.

Analyze the project report below.

Explain:

1. Deployment Architecture
2. Deployment Flow
3. Infrastructure Components
4. Application Components
5. Networking Flow
6. CI/CD Flow (if applicable)
7. Potential Deployment Risks

Create a step-by-step deployment explanation.

Project Report:

{report_text}
"""

    return ask_llm(prompt)
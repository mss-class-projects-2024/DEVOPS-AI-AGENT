from ai.ollama_client import ask_llm

response = ask_llm(
    "Explain Kubernetes readinessProbe"
)

print(response)
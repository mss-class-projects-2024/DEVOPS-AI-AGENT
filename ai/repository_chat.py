from ai.ollama_client import ask_llm

def chat_with_repository(report_text):

    while True:

        question = input(
            "\nAsk about repository: "
        )

        if question.lower() == "exit":
            break

        prompt = f"""
Repository Information:

{report_text}

Question:
{question}
"""

        print(
            ask_llm(prompt)
        )
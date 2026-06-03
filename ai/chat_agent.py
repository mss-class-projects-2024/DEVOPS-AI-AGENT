from ai.ollama_client import ask_llm


def start_chat():

    print("\nDevOps AI Agent")
    print("Type 'exit' to quit\n")

    while True:

        question = input(
            "\nDevOps-AI > "
        )

        if (
            question.lower()
            == "exit"
        ):
            break

        response = ask_llm(
            question
        )

        print("\n")
        print(response)
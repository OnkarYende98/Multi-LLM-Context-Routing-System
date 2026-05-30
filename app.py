from memory import (
    add_message,
    clear_history
)

from router import (
    get_response
)

print("\n=================================")
print("MULTI LLM CONTEXT ROUTER")
print("=================================")

print("\nCommands:")
print("exit  -> Close application")
print("quit  -> Close application")
print("bye   -> Close application")
print("clear -> Clear chat history")
print("\n")


while True:

    user_input = input(
        "You: "
    )

    command = user_input.lower().strip()

    if command in [
        "exit",
        "quit",
        "bye"
    ]:

        print(
            "\nClosing Multi LLM Router..."
        )

        break

    if command == "clear":

        clear_history()

        with open(
            "summary.json",
            "w"
        ) as file:

            file.write(
                '{\n    "summary": ""\n}'
            )

        print(
            "\nHistory Cleared\n"
        )

        continue

    add_message(
        "user",
        user_input
    )

    response = get_response(
        user_input
    )

    print(
        "\nAssistant:\n"
    )

    print(
        response
    )

    add_message(
        "assistant",
        response
    )

print(
    "\nApplication Closed"
)
from token_monitor import (
    threshold_reached
)

from summarizer import (
    create_summary,
    load_summary
)

from memory import (
    load_history
)

from providers import (
    ask_gemini,
    ask_groq
)


def get_response(user_input):

    if not threshold_reached():

        print(
            "\n[ROUTER] Using Gemini\n"
        )

        return ask_gemini(
            user_input
        )

    print(
        "\n[ROUTER] Threshold Reached"
    )

    summary = create_summary()

    print(
        "\n[ROUTER] Summary Created"
    )

    history = load_history()

    recent_messages = history[-5:]

    recent_context = ""

    for msg in recent_messages:

        recent_context += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    context_prompt = f"""
CONVERSATION SUMMARY

{summary}

RECENT MESSAGES

{recent_context}

CURRENT USER MESSAGE

{user_input}
"""

    print(
        "\n[ROUTER] Routing To Groq\n"
    )

    return ask_groq(
        context_prompt
    )
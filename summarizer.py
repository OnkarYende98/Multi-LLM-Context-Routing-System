import json

from memory import load_history

from providers import ask_gemini


SUMMARY_FILE = "summary.json"


def create_summary():

    history = load_history()

    conversation = ""

    for message in history:

        conversation += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    prompt = f"""
You are a memory compression agent.

Your job is to compress the conversation while preserving:

1. User goals
2. Projects being discussed
3. Decisions already made
4. Technical stack
5. Important facts
6. Current task
7. Future plans

Remove:

- greetings
- repetitions
- small talk
- unnecessary details

Return output in this format:

PROJECTS:
...

GOALS:
...

DECISIONS:
...

TECH STACK:
...

CURRENT TASK:
...

FUTURE TASKS:
...

Conversation:

{conversation}
"""

    summary = ask_gemini(prompt)

    with open(
        SUMMARY_FILE,
        "w"
    ) as file:

        json.dump(
            {"summary": summary},
            file,
            indent=4
        )

    return summary


def load_summary():

    try:

        with open(
            SUMMARY_FILE,
            "r"
        ) as file:

            return json.load(file)["summary"]

    except:

        return ""
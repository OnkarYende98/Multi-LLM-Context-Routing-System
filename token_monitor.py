from memory import load_history


THRESHOLD = 300


def estimate_tokens(text):

    words = len(text.split())

    return int(words * 1.3)


def get_total_tokens():

    history = load_history()

    total_tokens = 0

    for message in history:

        total_tokens += estimate_tokens(
            message["content"]
        )

    return total_tokens


def threshold_reached():

    total_tokens = get_total_tokens()

    print(
        f"\n[TOKEN MONITOR] Estimated Tokens: {total_tokens}"
    )

    print(
        f"[TOKEN MONITOR] Threshold: {THRESHOLD}"
    )

    return total_tokens >= THRESHOLD
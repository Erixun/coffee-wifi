emoji = {"coffee": "☕️", "power": "💪", "wifi": "🔌"}


def make_choices(emoji):
    return [(i, emoji * i if 0 < i else "✘") for i in [0, 1, 2, 3, 4, 5]]

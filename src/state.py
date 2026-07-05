import json
import os

STATE_FILE = "state/state.json"


def load_state():
    os.makedirs("state", exist_ok=True)

    if not os.path.exists(STATE_FILE):
        return {
            "last_count": None,
            "last_alert": None,
            "alerts_sent": 0,
            "runs": 0
        }

    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        # corrupted or empty file fallback
        return {
            "last_count": None,
            "last_alert": None,
            "alerts_sent": 0,
            "runs": 0
        }


def save_state(state):
    os.makedirs("state", exist_ok=True)

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def should_alert(state, current_count):

    if current_count is None:
        return False

    if current_count <= 0:
        return False

    # only alert on odd numbers
    if current_count % 2 == 0:
        return False

    # prevent duplicate alerts
    if state.get("last_count") == current_count:
        return False

    return True

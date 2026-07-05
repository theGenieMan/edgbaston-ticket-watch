import json
import os

STATE_FILE = "state/state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "last_count": None,
            "last_alert": None,
            "alerts_sent": 0,
            "runs": 0
        }

    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    os.makedirs("state", exist_ok=True)

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def should_alert(state, current_count):
    """
    Alert only when:
    - count is odd
    - and it has changed since last alert
    """

    if current_count == 0:
        return False

    if current_count % 2 == 0:
        return False

    return state["last_count"] != current_count

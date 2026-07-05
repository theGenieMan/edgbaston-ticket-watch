from datetime import datetime
from zoneinfo import ZoneInfo

from parser import get_ticket_count
from telegram import send_message
from logger import log_run
from state import load_state, save_state, should_alert
from config import TIMEZONE


def main():

    now = datetime.now(ZoneInfo(TIMEZONE))

    state = load_state()
    state["runs"] += 1

    try:
        count = get_ticket_count()

        log_run(f"Tickets={count} Run={state['runs']}")

        if should_alert(state, count):

            send_message(
                f"""🎟 England vs India ODI

{count} tickets available!

https://ticketexchange.edgbaston.com/list/resaleProducts?lang=en"""
            )

            log_run("ALERT SENT")
            state["last_alert"] = now.isoformat()
            state["alerts_sent"] += 1

        state["last_count"] = count

    except Exception as e:

        log_run(f"ERROR: {str(e)}")

    save_state(state)


if __name__ == "__main__":
    main()

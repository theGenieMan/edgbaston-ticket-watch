import time
from datetime import datetime
from zoneinfo import ZoneInfo

from parser import get_ticket_count
from telegram import send_message
from logger import log_run
from state import load_state, save_state, should_alert
from config import TIMEZONE


def main():

    start_time = time.time()

    state = load_state()
    state["runs"] += 1

    try:
        # -----------------------------
        # Get ticket count from page
        # -----------------------------
        count = get_ticket_count()

        # -----------------------------
        # Decide if we should alert
        # -----------------------------
        alert = should_alert(state, count)

        # -----------------------------
        # Send Telegram alert (if needed)
        # -----------------------------
        if alert:

            send_message(
                f"""🎟 England vs India ODI

{count} tickets available!

https://ticketexchange.edgbaston.com/list/resaleProducts?lang=en"""
            )

            state["last_alert"] = datetime.now(ZoneInfo(TIMEZONE)).isoformat()
            state["alerts_sent"] += 1

        # Update state
        state["last_count"] = count

        # -----------------------------
        # Measure duration
        # -----------------------------
        duration = time.time() - start_time

        # -----------------------------
        # LOG RUN (FIXED CALL)
        # -----------------------------
        log_run(count, alert, duration)

    except Exception as e:

        duration = time.time() - start_time

        # Log failed run safely
        log_run(-1, False, duration)

        send_message(f"❌ Error in monitor: {str(e)}")

    # Save updated state (cached)
    save_state(state)


if __name__ == "__main__":
    main()

import csv
import os
from telegram import send_message

LOG_FILE = "logs/current.csv"


def build_summary():

    if not os.path.exists(LOG_FILE):
        return "No data available."

    rows = []

    with open(LOG_FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        return "No data available."

    total_runs = len(rows)
    alerts = sum(1 for r in rows if r["alert"] == "YES")

    max_tickets = max(int(r["tickets"]) for r in rows if r["tickets"].isdigit())

    return f"""📊 Edgbaston Summary

Runs: {total_runs}
Alerts: {alerts}
Max tickets: {max_tickets}
"""


def send_summary():

    summary = build_summary()

    send_message(summary)

    # reset log after sending
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

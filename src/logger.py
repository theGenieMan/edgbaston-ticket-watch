import os
import csv
from datetime import datetime
from zoneinfo import ZoneInfo

from config import TIMEZONE

LOG_FILE = "logs/current.csv"


def log_run(tickets, alert, duration):

    os.makedirs("logs", exist_ok=True)

    now = datetime.now(ZoneInfo(TIMEZONE))

    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "tickets",
                "alert",
                "duration_seconds"
            ])

        writer.writerow([
            now.strftime("%Y-%m-%d %H:%M:%S"),
            tickets,
            "YES" if alert else "NO",
            round(duration, 2)
        ])

from datetime import datetime
from zoneinfo import ZoneInfo

from config import TIMEZONE


def log(message):

    now = datetime.now(ZoneInfo(TIMEZONE))

    print(
        f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    )

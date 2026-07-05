"""
Edgbaston Ticket Watch
Configuration
"""

# Event to monitor
EVENT_NAME = "2026 England vs India Men's ODI"

# Ticket Exchange URL
URL = "https://ticketexchange.edgbaston.com/list/resaleProducts?lang=en"

# Timezone
TIMEZONE = "Europe/London"

# Monitoring hours
CHECK_START_HOUR = 7
CHECK_END_HOUR = 22

# Buying one ticket means we only want alerts when the
# remaining tickets would be even (odd ticket count)
BUYING_TICKETS = 1

# Ticket text pattern
TICKET_PATTERN = r"(\d+)\s+tickets"

# Telegram Secrets
TELEGRAM_BOT_TOKEN = "TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "TELEGRAM_CHAT_ID"

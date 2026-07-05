from playwright.sync_api import sync_playwright
import re

from config import URL, EVENT_NAME, TICKET_PATTERN


def get_ticket_count():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            URL,
            wait_until="networkidle",
            timeout=60000,
        )

        page.wait_for_timeout(5000)

        body = page.locator("body").inner_text()

        browser.close()

    start = body.find(EVENT_NAME)

    if start == -1:
        raise RuntimeError("Event not found")

    section = body[start:]

    headings = list(re.finditer(r"\n20\d\d", section))

    if len(headings) >= 2:
        section = section[:headings[1].start()]

    match = re.search(TICKET_PATTERN, section)

    if not match:
        raise RuntimeError("Ticket count not found")

    return int(match.group(1))

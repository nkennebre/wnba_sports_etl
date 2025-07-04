import requests
import json
from datetime import datetime, timedelta
from time import sleep
import os

def get_game_ids(start_date="20250516", end_date="20250630", exclude_dates=None):
    if exclude_dates is None:
        exclude_dates = []

    current = datetime.strptime(start_date, "%Y%m%d")
    end = datetime.strptime(end_date, "%Y%m%d")
    game_ids = []

    while current <= end:
        date_str = current.strftime("%Y%m%d")
        if date_str in exclude_dates:
            print(f"Skipping excluded date: {date_str}")
            current += timedelta(days=1)
            continue

        url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard?dates={date_str}"
        print(f"Scraping: {url}")
        try:
            resp = requests.get(url)
            data = resp.json()
            for event in data.get("events", []):
                game_id = event.get("id")
                if game_id:
                    game_ids.append(game_id)
        except Exception as e:
            print(f"❌ Error on {date_str}: {e}")
        current += timedelta(days=1)
        sleep(0.2)

    return sorted(set(game_ids))
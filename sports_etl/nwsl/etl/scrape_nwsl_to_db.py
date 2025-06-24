import pandas as pd
import sqlite3
import time
from pathlib import Path
from typing import Dict
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Define log types and corresponding database table names
MATCHLOG_TYPES: Dict[str, str] = {
    "Scores-and-Fixtures": "nwsl_scores_and_fixtures",
    "shooting": "nwsl_shooting",
    "keeper": "nwsl_goalkeeping",
    "passing": "nwsl_passing",
    "passing_types": "nwsl_pass_types",
    "gca": "nwsl_gca",
    "defense": "nwsl_defensive_actions",
    "possession": "nwsl_possession",  
    "misc": "nwsl_misc"
}

# Define teams (fbref ID and team name slug used in the URL)
TEAMS: Dict[str, str] = {
    "d976a235": "Chicago-Stars",
    "6f666306": "Kansas-City-Current",
    "2a6178ac": "Orlando-Pride",
    "bf961da0": "San-Diego-Wave",
    "e442aad0": "Washington-Spirit",
    "df9a10a1": "Portland-Thorns-FC",
    "257fad2b": "Seattle-Reign-FC",
    "da19ebd1": "Racing-Louisville",
    "8e306dc6": "Gotham-FC",
    "85c458aa": "North-Carolina-Courage",
    "231a532f": "Bay-FC",
    "ae38d267": "Angel-City-FC",
    "e813709a": "Houston-Dash",
    "d4c130bc": "Utah-Royals"
}

YEARS = list(range(2015, 2026))
DB_PATH = Path("data/nwsl/nwsl_matchlogs.db")

def scrape_nwsl_matchlog_table(team_code: str, team_name_slug: str, year: int, log_type: str) -> pd.DataFrame:
    # Sanitize team_name_slug to ensure it’s hyphenated (no spaces)
    slug = team_name_slug.replace(" ", "-")

    url = f"https://fbref.com/en/squads/{team_code}/{year}/matchlogs/c182/{log_type}/{slug}-Match-Logs-NWSL"
    logging.info(f"Scraping: {url}")

    tables = pd.read_html(url, match="Date")
    if not tables:
        raise ValueError(f"No table found at {url}")

    df = tables[0]
    df["season"] = year
    df["team"] = slug.replace("-", " ")

    return df

def save_to_sqlite(df: pd.DataFrame, db_path: Path, table_name: str):
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists="append", index=False)

def scrape_nwsl_logs_to_db(team_code: str, team_name: str, season: int, db_path: Path = DB_PATH):
    for log_type, table_name in MATCHLOG_TYPES.items():
        try:
            df = scrape_nwsl_matchlog_table(team_code, team_name, season, log_type)
            save_to_sqlite(df, db_path, table_name)
            logging.info(f"Saved: {team_name} {season} {log_type} => {table_name} ({len(df)} rows)")
            time.sleep(1.5)
        except Exception as e:
            logging.warning(f"Failed: {team_name} {season} {log_type}: {e}")


if __name__ == "__main__":
    for team_code, team_name in TEAMS.items():
        for year in YEARS:
            scrape_nwsl_logs_to_db(team_code, team_name, year)


# run_etl.py

from sports_etl.etl.scrape_wnba_stats import scrape_games_for_team
from sports_etl.etl.transform import transform_team_stats_my_dataset
from sports_etl.etl.load import save_to_sqlite
from sports_etl.config import BASE_DIR

import sys

def main(team_code="SEA", season=2025):
    print(f"Scraping data for {team_code} ({season})...")

    # Step 1: Scrape
    df_raw = scrape_games_for_team(team_code, season=season)
    if df_raw.empty:
        print("No data found. Exiting.")
        sys.exit()

    # Step 2: Transform
    df_clean = transform_team_stats_my_dataset(df_raw)

    # Step 3: Load into SQLite
    db_path = BASE_DIR / "data" / "teamstats.db"
    save_to_sqlite(df_clean, db_path=db_path, if_exists="append")


    print(f"ETL complete for {team_code} {season} — {len(df_clean)} rows written.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run WNBA ETL pipeline.")
    parser.add_argument("--team", type=str, default="SEA", help="3-letter WNBA team code")
    parser.add_argument("--season", type=int, default=2025, help="Season year")

    args = parser.parse_args()
    main(team_code=args.team.upper(), season=args.season)
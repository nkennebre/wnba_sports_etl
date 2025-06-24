# scripts/test_scrape_nwsl.py

from sports_etl.nwsl.etl.scrape_nwsl_to_db import MATCHLOG_TYPES, scrape_nwsl_logs_to_db

# 🔧 Set parameters for test
team_name = "Chicago-Stars"
team_id = "d976a235"     # Chicago Stars
season = 2025
log_types = ["misc", "keeper"]  # You can test one or more, e.g. ["misc"]

# Run the test
print(f"Running NWSL scraper for {team_name} ({season}) — Logs: {log_types}")
scrape_nwsl_logs_to_db(team_name, team_id, season, log_types)
print("✅ Done!")
# sports_etl/etl/scrape_wnba_stats.py

import pandas as pd
import time
import random

def scrape_games_for_team(team_abbr: str, season: int = 2025) -> pd.DataFrame:
    """
    Scrapes WNBA game stats for a given team and season.
    Args:
        team_abbr (str): 3-letter team code (e.g., 'SEA', 'NYL')
        season (int): Year of the season
    Returns:
        pd.DataFrame: Raw box score data
    """
    url = f"https://www.basketball-reference.com/wnba/teams/{team_abbr}/{season}/gamelog"
    print(f"Scraping URL: {url}")

    try:
        df = pd.read_html(url, header=1, attrs={'id': 'wnba_tgl_basic'})[0]
    except ValueError:
        raise ValueError(f"Table not found at {url}")

    # Drop rows with non-numeric 'Rk' (usually headers)
    df = df[df['Rk'].astype(str).str.isnumeric()]

    # Drop irrelevant columns
    for col in ['Rk', 'Unnamed: 6', 'Unnamed: 9', 'Unnamed: 26']:
        if col in df.columns:
            df = df.drop(columns=[col])

    # Rename columns
    tm_stats = [
        'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
        'FT', 'FTA', 'FT%', 'ORB', 'TRB', 'AST',
        'STL', 'BLK', 'TOV', 'PF'
    ]
    tm_stats_dict = {stat: 'Tm_' + stat for stat in tm_stats}
    opp_stats_dict = {stat + '.1': 'Opp_' + stat for stat in tm_stats}

    df.rename(columns={'Unnamed: 3': 'Home', 'Tm': 'Tm_Pts', 'Opp.1': 'Opp_Pts'}, inplace=True)
    df.rename(columns=tm_stats_dict, inplace=True)
    df.rename(columns=opp_stats_dict, inplace=True)

    # Encode Home column: @ = Away → 0, else = Home → 1
    df['Home'] = df['Home'].apply(lambda x: 0 if x == '@' else 1)

    # Insert team and season columns
    df.insert(loc=0, column='Season', value=season)
    df.insert(loc=1, column='Team', value=team_abbr.upper())

    # Pause for scraping etiquette
    time.sleep(random.randint(3, 5))

    return df
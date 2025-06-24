from sports_etl.utils.logger import get_logger
import pandas as pd

logger = get_logger(__name__)

def clean_box_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw box score data scraped from WNBA.com or another live source.
    This is a placeholder until real scraping logic is added.
    """
    df = df.copy()

    # Example cleaning steps (adjust based on actual scraped data)
    df["Date"] = pd.to_datetime(df["Date"])
    df["3PT"] = pd.to_numeric(df["3PT"], errors="coerce")
    df["Rebounds"] = pd.to_numeric(df["Rebounds"], errors="coerce")

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    logger.info(f"Cleaned scraped box score data — shape: {df.shape}")
    return df


def transform_team_stats_kaggle(df):
    """
    Transform raw WNBA team stats into engineered, clean format.
    """
    df = df.copy()
    
    # Rename columns if needed
    df.rename(columns={
        "threepoint_fgm": "3pt_m",
        "threepoint_fga": "3pt_a",
        "threepoint_fg_percent": "3pt_pct"
    }, inplace=True)

    # Add features
    df["3pt_pct"] = df["3pt_m"] / df["3pt_a"].replace(0, pd.NA)
    df["efg_pct"] = (df["fgm"] + 0.5 * df["3pt_m"]) / df["fga"].replace(0, pd.NA)
    df["possessions"] = df["fga"] + 0.44 * df["fta"] - df["oreb"] + df["tov"]
    df["off_rating"] = df["ppg"] / df["possessions"].replace(0, pd.NA) * 100
    
    # Drop rows with any resulting NAs
    df.dropna(inplace=True)
    
    # Drop exact duplicate rows (across all columns)
    df.drop_duplicates(inplace=True)

    logger.info(f"Transformed team stats — final shape after deduplication: {df.shape}")
    logger.info("Transformed team stats with new features.")
    return df

def transform_team_stats_my_dataset(df):
    """
    Transform raw WNBA team stats into engineered, clean format.
    """
    df = df.copy()
    
    # Add features
    df["win_margin"] = df["Tm_Pts"] - df["Opp_Pts"]
    df["Tm_poss"] = df["Tm_FGA"] + 0.44 * df["Tm_FTA"] - df["Tm_ORB"] + df["Tm_TOV"]
    df["Opp_poss"] = df["Opp_FGA"] + 0.44 * df["Opp_FTA"] - df["Opp_ORB"] + df["Opp_TOV"]
    df["Tm_off_rating"] = (df["Tm_Pts"] / df["Tm_poss"].replace(0, pd.NA)) * 100
    df["Tm_def_rating"] = (df["Opp_Pts"] / df["Opp_poss"].replace(0, pd.NA)) * 100
    df["Tm_tov_rate"] = df["Tm_TOV"]/df["Tm_poss"]
    df["Opp_tov_rate"] = df["Opp_poss"]/df["Opp_poss"]
     
    # Drop rows with any resulting NAs
    df.dropna(inplace=True)
    
    # Drop exact duplicate rows (across all columns)
    df.drop_duplicates(inplace=True)

    logger.info(f"Transformed team stats — final shape after deduplication: {df.shape}")
    logger.info("Transformed team stats with new features.")
    return df
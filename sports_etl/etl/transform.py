from sports_etl.utils.logger import get_logger
import pandas as pd

logger = get_logger(__name__)

def transform_team_stats(df):
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
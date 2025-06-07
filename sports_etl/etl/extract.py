import pandas as pd
from pathlib import Path
from sports_etl.utils.logger import get_logger

logger = get_logger(__name__)

def load_team_stats(csv_path: str | Path) -> pd.DataFrame:
    csv_path = Path(csv_path)

    if not csv_path.exists():
        logger.error(f"File not found: {csv_path}")
        raise FileNotFoundError(f"No file found at {csv_path}")

    try:
        df = pd.read_csv(csv_path)
        logger.info(f"Loaded {df.shape[0]} rows × {df.shape[1]} columns from {csv_path.name}")
        return df
    except Exception as e:
        logger.exception("Failed to load CSV")
        raise e
import pandas as pd
import sqlite3
from pathlib import Path
from sports_etl.utils.logger import get_logger

logger = get_logger(__name__)


def save_to_csv(df: pd.DataFrame, filepath: str | Path, index: bool = False):
    """
    Save DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): Data to save
        filepath (str | Path): Destination path
        index (bool): Whether to include the index column
    """
    filepath = Path(filepath)
    df.to_csv(filepath, index=index)
    logger.info(f"Saved DataFrame to CSV: {filepath}")


def save_to_sqlite(df: pd.DataFrame, db_path: str = "data/teamstats.db", if_exists: str = "append"):
    """
    Save DataFrame to SQLite and remove duplicate team/date entries.
    """
    conn = sqlite3.connect(db_path)

    try:
        df.to_sql("game_stats", conn, if_exists=if_exists, index=False)
        logger.info(f"Saved {len(df)} rows to game_stats table.")

        # Deduplication logic: keep only the first occurrence of each (Team, Date)
        cursor = conn.cursor()
        dedupe_sql = """
        DELETE FROM game_stats
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM game_stats
            GROUP BY Team, Date
        )
        """
        cursor.execute(dedupe_sql)
        conn.commit()
        logger.info("Deduplicated game_stats table by (Team, Date).")

    except Exception as e:
        logger.error(f"Error writing to SQLite: {e}")
        raise

    finally:
        conn.close()
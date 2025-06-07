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


def save_to_sqlite(df: pd.DataFrame, db_path: str | Path, table_name: str, if_exists: str = "replace"):
    """
    Save DataFrame to an SQLite database.

    Args:
        df (pd.DataFrame): Data to save
        db_path (str | Path): SQLite DB file path
        table_name (str): Table name to insert into
        if_exists (str): What to do if the table exists: 'fail', 'replace', 'append'
    """
    db_path = Path(db_path)
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)
        logger.info(f"Saved DataFrame to SQLite: {db_path} (table: {table_name}, mode: {if_exists})")
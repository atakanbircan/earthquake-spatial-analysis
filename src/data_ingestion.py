import logging
import pandas as pd
from typing import Optional

def fetch_earthquake_data(url: str) -> Optional[pd.DataFrame]:
    logging.info(f"Fetching data from endpoint: {url}")
    try:
        df = pd.read_csv(url)
        logging.info(f"Successfully loaded {len(df)} records from the source.")
        return df
    except Exception as e:
        logging.error(f"Failed to fetch data. Error: {e}")
        return None
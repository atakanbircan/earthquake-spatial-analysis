import logging
import pandas as pd
import os

def filter_significant_earthquakes(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    logging.info(f"Applying magnitude threshold filter (>= {threshold})")
    filtered_df = df[df['mag'] >= threshold].copy()
    filtered_df.sort_values(by='mag', ascending=False, inplace=True)
    logging.info(f"Filtered dataset down to {len(filtered_df)} significant events.")
    return filtered_df

def export_spatial_data(df: pd.DataFrame, output_dir: str, filename: str) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, filename)
    df.to_csv(file_path, index=False)
    logging.info(f"Spatial data successfully exported to: {os.path.abspath(file_path)}")
import logging
import os
import config

from src.data_ingestion import fetch_earthquake_data
from src.processing import filter_significant_earthquakes, export_spatial_data
from src.visualization import create_interactive_map

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("--- Starting Spatial Earthquake Analysis Pipeline ---")

    df_raw = fetch_earthquake_data(config.DATA_URL)
    if df_raw is None or df_raw.empty:
        return

    df_processed = filter_significant_earthquakes(df_raw, config.MAGNITUDE_THRESHOLD)

    if not df_processed.empty:
        export_spatial_data(df_processed, config.PROCESSED_DATA_DIR, config.EXPORT_FILENAME)

        eq_map = create_interactive_map(df_processed)
        if not os.path.exists(config.MAP_OUTPUT_DIR):
            os.makedirs(config.MAP_OUTPUT_DIR)

        map_path = os.path.join(config.MAP_OUTPUT_DIR, config.MAP_FILENAME)
        eq_map.save(map_path)
        logging.info(f"Interactive map successfully saved to: {os.path.abspath(map_path)}")

    logging.info("--- Pipeline Execution Completed Successfully ---")

if __name__ == "__main__":
    main()
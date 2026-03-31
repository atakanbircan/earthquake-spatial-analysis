import logging
import folium
import pandas as pd

def create_interactive_map(df: pd.DataFrame) -> folium.Map:
    logging.info("Initializing spatial visualization...")
    mean_lat = df['latitude'].mean() if not df.empty else 0
    mean_lon = df['longitude'].mean() if not df.empty else 0

    base_map = folium.Map(location=[mean_lat, mean_lon], zoom_start=2, tiles="CartoDB positron")

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=row['mag'] * 1.5,
            popup=f"Magnitude: {row['mag']} | Location: {row['place']}",
            color="#e74c3c",
            fill=True,
            fill_color="#e74c3c",
            fill_opacity=0.7,
            weight=1
        ).add_to(base_map)

    return base_map
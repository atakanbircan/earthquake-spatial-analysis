# Spatial Analysis and Automated ETL Pipeline for Global Earthquakes

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-orange.svg)
![Folium](https://img.shields.io/badge/Folium-Web_Mapping-success.svg)
![QGIS](https://img.shields.io/badge/QGIS-Spatial_Analysis-lightgrey.svg)

## 📌 Project Overview
This project implements an automated, production-grade ETL (Extract, Transform, Load) pipeline to retrieve, process, and visualize real-time global earthquake data from the USGS (United States Geological Survey) API. 

The pipeline is designed with modular software engineering principles, ensuring clean architecture, reproducibility, and seamless integration with external Geographic Information System (GIS) tools like QGIS.

## 🏗️ Architecture & Project Structure
The repository follows standard Data Science project structures to separate configurations, source code, and outputs:

```text
earthquake-spatial-analysis/
├── data/
│   └── processed/            # Cleaned data ready for GIS integration
├── outputs/                  # Generated interactive HTML maps and static layouts
├── src/                      # Core pipeline modules
│   ├── __init__.py
│   ├── data_ingestion.py     # API connection and data retrieval
│   ├── processing.py         # Data cleaning and magnitude filtering
│   └── visualization.py      # Interactive spatial visualization
├── config.py                 # Pipeline configurations and thresholds
├── main.py                   # Main execution script
├── requirements.txt          # Environment dependencies
└── README.md                 # Project documentation
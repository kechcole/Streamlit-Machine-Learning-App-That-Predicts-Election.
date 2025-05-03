import pandas as pd
import geopandas as gpd


# Read and clean data 
def fetch_clean_data():
    
    data = gpd.read_file('1.Predict US Election - ML App Streamlit/Data/Contigous_US_County_Election_Results.gpkg', layer='simplified')

    return data


def main():
    data = fetch_clean_data()

if __name__ == '__main__':
    main()
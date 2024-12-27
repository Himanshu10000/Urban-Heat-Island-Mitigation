import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

# Load temperature data (latitude, longitude, temperature values)
def load_temperature_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Convert to GeoDataFrame for spatial analysis
def create_geodataframe(data):
    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['longitude'], data['latitude']))
    return gdf

# Plot heat map using Folium
def create_heatmap(gdf):
    # Create base map
    m = folium.Map(location=[gdf.geometry.y.mean(), gdf.geometry.x.mean()], zoom_start=12)
    
    # Convert to list of lat-long points
    heat_data = [[point.y, point.x] for point in gdf.geometry]
    
    # Add heat layer
    HeatMap(heat_data).add_to(m)
    
    # Save map as HTML
    m.save("heat_map.html")
    print("Heat map created and saved as 'heat_map.html'")

# Main function
if __name__ == '__main__':
    data = load_temperature_data('temperature_data.csv')  # Replace with actual data path
    gdf = create_geodataframe(data)
    create_heatmap(gdf)

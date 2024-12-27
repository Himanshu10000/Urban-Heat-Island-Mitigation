import geopandas as gpd
import pandas as pd

# Function to suggest rooftop garden locations based on building type and heat zones
def suggest_rooftop_gardens(gdf, heat_threshold=30):
    # Filter buildings in high-heat areas (example threshold of 30°C)
    high_heat_areas = gdf[gdf['temperature'] > heat_threshold]
    
    # Suggest rooftop gardens in these areas
    high_heat_areas['rooftop_garden_suggestion'] = True
    return high_heat_areas

# Function to suggest tree plantations
def suggest_tree_plantations(gdf, park_data, distance_threshold=100):
    # Buffer parks and recommend tree plantations within a 100m radius
    parks_gdf = gpd.read_file(park_data)
    gdf['buffer'] = gdf.geometry.buffer(distance_threshold)
    
    suggested_locations = gpd.sjoin(gdf, parks_gdf, how='inner', op='intersects')
    suggested_locations['tree_plantation_suggestion'] = True
    return suggested_locations

# Main function
if __name__ == '__main__':
    # Load building and temperature data
    gdf = gpd.read_file('buildings.shp')  # Replace with actual buildings shapefile path
    gdf_temp = pd.read_csv('temperature_data.csv')
    
    # Merge temperature data with buildings data
    gdf['temperature'] = gdf_temp['temperature']
    
    # Suggest rooftop gardens and tree plantations
    rooftop_suggestions = suggest_rooftop_gardens(gdf)
    tree_suggestions = suggest_tree_plantations(gdf, 'parks.shp')  # Replace with actual park shapefile
    
    # Save the suggested locations
    rooftop_suggestions.to_file("rooftop_gardens_suggestions.shp")
    tree_suggestions.to_file("tree_plantation_suggestions.shp")
    
    print("Rooftop garden and tree plantation suggestions saved.")

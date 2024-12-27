import geopandas as gpd

# Function to generate recommendations for urban planning based on heat zones
def generate_planning_report(gdf, heat_threshold=30):
    high_heat_areas = gdf[gdf['temperature'] > heat_threshold]
    
    report = f"Urban Planning Report: Heat-Prone Areas\n"
    report += f"------------------------------------\n"
    report += f"Total number of high-heat areas identified: {len(high_heat_areas)}\n"
    
    # Suggest areas for tree plantations and rooftop gardens
    report += "Suggested interventions:\n"
    report += "- Rooftop gardens in high-heat areas\n"
    report += "- Tree plantations in open spaces\n"
    
    # Save report to a text file
    with open('urban_planning_report.txt', 'w') as f:
        f.write(report)
    print("Urban planning report saved as 'urban_planning_report.txt'")

# Main function
if __name__ == '__main__':
    gdf = gpd.read_file('urban_area.shp')  # Replace with actual urban area shapefile path
    generate_planning_report(gdf)

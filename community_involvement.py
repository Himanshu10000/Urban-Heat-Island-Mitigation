import folium

# Function to create an interactive map where citizens can suggest greening efforts
def create_community_map():
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)  # Centering on San Francisco for example
    
    # Add a marker for citizen greening suggestions
    folium.Marker([37.7749, -122.4194], popup="Suggest Tree Plantation Site").add_to(m)
    
    # Save map
    m.save("community_engagement_map.html")
    print("Community engagement map created and saved as 'community_engagement_map.html'")

# Main function
if __name__ == '__main__':
    create_community_map()

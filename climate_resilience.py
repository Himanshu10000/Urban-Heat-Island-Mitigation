import pandas as pd
import matplotlib.pyplot as plt

# Function to model the impact of green infrastructure on temperature reduction
def model_heat_impact_before_after(gdf, intervention_col):
    # Calculate the average temperature before and after intervention
    before_intervention = gdf[gdf[intervention_col] == False]['temperature'].mean()
    after_intervention = gdf[gdf[intervention_col] == True]['temperature'].mean()
    
    # Plot temperature change
    labels = ['Before Intervention', 'After Intervention']
    temperatures = [before_intervention, after_intervention]
    
    plt.bar(labels, temperatures)
    plt.ylabel('Average Temperature (°C)')
    plt.title('Impact of Green Infrastructure on Temperature')
    plt.show()

# Main function
if __name__ == '__main__':
    gdf = pd.read_csv('urban_data_with_interventions.csv')  # Replace with actual data
    
    # Call the model impact function to visualize the result
    model_heat_impact_before_after(gdf, 'greening_intervention')

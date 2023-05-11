import pandas as pd
import matplotlib.pyplot as plt
from math import ceil
import os
from datetime import datetime

# Read the CSV file
data = pd.read_csv('biomass.csv')

# Extract the relevant columns
samples = data['sample']
carbon = data['carbon']
hydrogen = data['hydrogen']
oxygen = data['oxygen']
nitrogen = data['nitrogen']
sulfur = data['sulfur']
hhv = data['HHV']

# Create a directory to store the figure files
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
directory = f"figures_{current_datetime}"
os.makedirs(directory, exist_ok=True)

# Loop through each sample and create a pie chart
for i in range(len(samples)):
    elements = ['Sulfur', 'Carbon', 'Nitrogen', 'Hydrogen', 'Oxygen', 'HHV']
    composition = [sulfur[i], carbon[i], nitrogen[i], hydrogen[i], oxygen[i], hhv[i]]

    # Create a new figure
    fig, ax = plt.subplots(figsize=(6, 6))

    # Create a pie chart
    ax.pie(composition, labels=elements, autopct='%1.1f%%', startangle=90)

    # Set the title
    ax.set_title(f"Biomass Composition of  {samples[i]} ")

    # Adjust the size of the pie chart and font size of labels
    ax.set_aspect('equal')
    ax.tick_params(labelsize=8)

    # Save the figure as a PNG file in the figures directory
    fig.savefig(f"{directory}/figure_{i + 1}.png", dpi=300)

    # Close the figure
    plt.close(fig)

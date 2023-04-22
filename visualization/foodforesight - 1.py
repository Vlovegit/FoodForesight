import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV file
data = pd.read_csv('F:/New folder/Desktop/visualization/data.csv')

# Create a pivot table with zip codes as rows and county names as columns
pivot = pd.pivot_table(data, values='zip_code', index='NAME', aggfunc='count')

# Generate heatmap using seaborn
ax = sns.heatmap(pivot, cmap='YlGnBu', annot=True, fmt='d')

# set Title label
ax.set_title('Zip Code in Atlanta')
# Set x-axis label
ax.set_xlabel('County Name')

# Set y-axis label
ax.set_ylabel('Zip Code')

# Show plot
plt.show()

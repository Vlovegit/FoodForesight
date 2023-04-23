import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('F:/New folder/Desktop/visualization/data.csv')

# Create a scatter plot with zip codes on the y-axis and longitudes on the x-axis
plt.scatter(data['NAME'], data['zip_code'])

# Set plot title and labels
plt.title('Zip Code in Atlanta')
plt.xlabel('NAME')
plt.ylabel('Zip Code')

# Show plot
plt.show()

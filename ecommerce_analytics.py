# ecommerce_analytics.py
import matplotlib
matplotlib.use('TkAgg')  # Use 'TkAgg' backend for compatibility


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the E-commerce dataset
dataset_path = '/Users/christiansamson/Documents/Personal/Coding/Projects/ecommerce_analytics/data/online_retail_II.csv'  # Update with your dataset file name
df = pd.read_csv(dataset_path)

# Your data analysis and visualizations here...

# Save or display visualizations
plt.show()

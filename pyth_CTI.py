import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Load CSV files into Pandas DataFrames
attacks_df = pd.read_csv('C:\\Users\\maila\\OneDrive\\Documents\\attacks.csv')
malware_df = pd.read_csv('C:\\Users\\maila\\OneDrive\\Documents\\malware.csv')

# Data processing and analysis
# You can customize this based on your specific threat intelligence data and requirements
# For example, aggregating the number of attacks or analyzing malware types

# Example: Count the number of attacks per category
attacks_count = attacks_df['Category'].value_counts()

# Example: Group malware by type and count occurrences
malware_count = malware_df['MalwareType'].value_counts()

# Data visualization using Matplotlib and Plotly
# You can customize the visualizations based on your specific data and preferences

# Example: Bar chart for number of attacks per category using Matplotlib
plt.figure(figsize=(10, 6))
attacks_count.plot(kind='bar', color='skyblue')
plt.title('Number of Attacks per Category')
plt.xlabel('Category')
plt.ylabel('Number of Attacks')
plt.show()

# Example: Pie chart for malware types using Plotly
fig = px.pie(malware_count, values=malware_count.values, names=malware_count.index,
             title='Malware Distribution')
fig.show()

#histogram
plt.figure(figsize=(10, 6))
plt.hist(malware_df['MalwareType'], color='salmon', edgecolor='black', bins=len(malware_count))
plt.title('Malware Type Distribution')
plt.xlabel('Malware Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.show()

#scatter.plot
plt.figure(figsize=(10, 6))
plt.scatter(attacks_df['Timestamp'], attacks_df['SourceIP'], color='orange', label='Attacks')
plt.scatter(malware_df['Timestamp'], malware_df['SourceIP'], color='green', label='Malware')
plt.title('Timestamp vs SourceIP')
plt.xlabel('Timestamp')
plt.ylabel('SourceIP')
plt.legend()
plt.show()


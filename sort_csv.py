import pandas as pd

data = pd.read_csv('aggregate_data.csv')
# Sort the DataFrame based on the third column
sorted_data = data.sort_values(by=data.columns[2])

sorted_data.to_csv('sorted_aggregate_data.csv', index=False)
import os
import pandas as pd
from datetime import datetime

def concatenate_files_per_month(folder_path):
    # Dictionary to hold dataframes for each month
    monthly_data = {}

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.startswith("sorted_"):
            # Extract the date part from the filename
            date_str = filename.split('_')[1]
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            month_name = date_obj.strftime('%B').lower()

            # Read the file into a dataframe
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)

            # Append the dataframe to the corresponding month in the dictionary
            if month_name not in monthly_data:
                monthly_data[month_name] = df
            else:
                monthly_data[month_name] = pd.concat([monthly_data[month_name], df])

    # Save the concatenated dataframes to new files
    for month, data in monthly_data.items():
        output_file = os.path.join(folder_path, f"{month}.csv")
        data.to_csv(output_file, index=False)

# Example usage
folder_path = '2023_ats_data'
concatenate_files_per_month(folder_path)


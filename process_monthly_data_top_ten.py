# This program takes in the monthly ats data 
# and outputs the top 10 issue names and their total share 
# quantity for each month.

import os
import pandas as pd

def process_monthly_files(directory):
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    
    monthly_data = {month: {} for month in months}

    for filename in os.listdir(directory):
        for month in months:
            if month in filename.lower():
                with open(os.path.join(directory, filename), 'r') as file:
                    df = pd.read_csv(file)
                    # Process the data as needed
                    print(f"Processing file: {filename}")
                    
                    # Group by issueName and sum the totalWeeklyShareQuantity
                    for issueName, group in df.groupby('issueName'):
                        if issueName not in monthly_data[month]:
                            monthly_data[month][issueName] = 0
                        monthly_data[month][issueName] += group['totalWeeklyShareQuantity'].sum()
                break

    # Combine all monthly data into a single DataFrame
    combined_data = []
    for month, data in monthly_data.items():
        # Sort the issue names by total share quantity and get the top 10
        top_10_issues = sorted(data.items(), key=lambda x: x[1], reverse=True)[:10]
        for issueName, total in top_10_issues:
            combined_data.append({'Month': month, 'Issue Name': issueName, 'Total Share Quantity': total})
        break
    combined_df = pd.DataFrame(combined_data)
    combined_df.to_csv(os.path.join(directory, f'{directory_path}_top_ten.csv'), index=False)


# Example usage
directory_path = '2024_ats_data'
process_monthly_files(directory_path)

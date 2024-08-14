# This program takes in the monthly ats data 
# and outputs the top 10 meme and stock tickers and their total share 
# quantity for each month.

# List I found on google - AMC, GameStop, Bed Bath and Beyond, Nokia, Blackberry
# Tesla, Palantir, 

import os
import pandas as pd

def process_monthly_files(directory):
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]

    meme_stock_list = ['AMC', 'GME', 'BBBY', 'NOK', 'BLB',
                      'TSLA', 'PLTR', 'NVDA']
    
    monthly_data = {month: {} for month in months}

    for filename in os.listdir(directory):
        for month in months:
            if month in filename.lower():
                with open(os.path.join(directory, filename), 'r') as file:
                    df = pd.read_csv(file)
                    # Process the data as needed
                    print(f"Processing file: {filename}")

                    # Get unique MPIDs and their totalWeeklyShareQuantity
                    for issueSymbol, group in df.groupby('issueSymbolIdentifier'):
                        if issueSymbol in meme_stock_list:
                            if issueSymbol not in monthly_data[month]:
                                monthly_data[month][issueSymbol] = 0
                            monthly_data[month][issueSymbol] += group['totalWeeklyShareQuantity'].sum()

    # Combine all monthly data into a single DataFrame
    combined_data = []
    for month, data in monthly_data.items():
        for issueSymbol, total in data.items():
            combined_data.append({'Month': month, 'Issue Name': issueSymbol, 'Total Share Quantity': total})

    combined_df = pd.DataFrame(combined_data)
    combined_df.to_csv(os.path.join(directory, f'{directory_path}_meme_stock.csv'), index=False)



# Example usage
directory_path = '2024_ats_data'
process_monthly_files(directory_path)

    
# This program takes in the monthly ats data 
# and outputs the top 10 meme and stock tickers and their total share 
# quantity for each month.

# List I found on google - AMC, GameStop, Bed Bath and Beyond, Nokia, Blackberry
# Tesla, Palantir, 

import os
import pandas as pd


def process_yearly_files(base_directory, years):
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]

    meme_stock_list = ['AMC', 'GME', 'BBBY', 'NOK', 'BLB',
                      'TSLA', 'PLTR', 'NVDA']
    
    yearly_data = {year: {month: {} for month in months} for year in years}

    for year in years:
        directory = os.path.join(f'{year}_ats_data')
        for filename in os.listdir(directory):
            for month in months:
                if month in filename.lower():
                    with open(os.path.join(directory, filename), 'r') as file:
                        df = pd.read_csv(file)
                        # Process the data as needed
                        print(f"Processing file: {filename} for year: {year}")

                        # Get unique MPIDs and their totalWeeklyShareQuantity
                        for issueSymbol, group in df.groupby('issueSymbolIdentifier'):
                            if issueSymbol in meme_stock_list:
                                if issueSymbol not in yearly_data[year][month]:
                                    yearly_data[year][month][issueSymbol] = 0
                                yearly_data[year][month][issueSymbol] += group['totalWeeklyShareQuantity'].sum()

    # Combine all yearly data into a single DataFrame
    combined_data = []
    for year, months_data in yearly_data.items():
        for month, data in months_data.items():
            for issueSymbol, total in data.items():
                combined_data.append({'Year': year, 'Month': month, 'Issue Name': issueSymbol, 'Total Share Quantity': total})

    combined_df = pd.DataFrame(combined_data)
    os.makedirs('yearly_meme_stock_data', exist_ok=True)
    combined_df.to_csv(os.path.join('yearly_meme_stock_data', 'combined_meme_stock_data.csv'), index=False)

# Example usage
base_directory = 'ats_data'
years = [2019, 2020, 2021, 2022, 2023, 2024]
process_yearly_files(base_directory, years)


    
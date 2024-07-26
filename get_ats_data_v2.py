import requests
import config
import csv 
import time
from test import generate_date_ranges
import os 
import pandas as pd

# This program gets the aggregate data for each week, and saves it to 'ats_data.csv'
# This is used to get the symbols so that get_individual_data can run and get the individual ATS data

# Replace these with your actual API Client ID and API Client Secret
client_id = config.finra_api_client
client_secret = config.finra_api_secret
access_token = config.finra_access_token

# Generate date ranges to automate downloading all the files e.g. in 2024 between 01-01 and 06-17
date_ranges = generate_date_ranges("2024-01-01", "2024-06-17")

# Directory to save the ats data
output_dir = '2024_ats_data'
os.makedirs(output_dir, exist_ok=True)

# Define the API URL and parameters
api_url = "https://api.finra.org/data/group/otcMarket/name/weeklySummary"
params = {
    "limit": 1000,
    "offset": 0,
    "delimiter": ",",
    "quoteValues": "true",
    "async": "false",
    "dateRangeFilters": [{"startDate": "2024-06-03", "endDate": "2024-06-03", "fieldName": "weekStartDate"}],
    "domainFilters": [{"fieldName": "summaryTypeCode", "values": ['ATS_W_SMBL_FIRM']},
                      {"fieldName": "tierDescription", "values": ['NMS Tier 1']}],
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

all_data = []

for start_date, end_date in date_ranges:

    params['dateRangeFilters'][0]['startDate'] = start_date
    params['dateRangeFilters'][0]['endDate'] = end_date
    params['offset'] = 0  # Reset offset for each date range

    while True:
        # Make the POST request
        api_response = requests.post(api_url, headers=headers, json=params)
        
        if api_response.status_code == 200:
            try:
                response_json = api_response.json()
                if not response_json:
                    break  # Exit loop if no more data is returned
                all_data.extend(response_json)
                if len(response_json) < params['limit'] or len(response_json) == 0: # If no more data is returned, break the loop
                    break
                params['offset'] += params['limit']  # Increment the offset for the next request
            except requests.exceptions.JSONDecodeError:
                print("Failed to parse JSON response.")
                print(api_response.text)
                break
        else:
            print(f"Failed to fetch data. Status code: {api_response.status_code}")
            print(api_response.text)
            break
        # Add a 0.5-second delay between requests
        time.sleep(0.5)



    # Write the response to a CSV file
    if all_data:
        filename = os.path.join(output_dir, f'{start_date}_ats_data.csv')
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = all_data[0].keys() 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for entry in all_data:
                writer.writerow(entry)
        data = pd.read_csv(filename)
        # Sort the DataFrame based on the third column
        sorted_data = data.sort_values(by=data.columns[2])
        
        sorted_filename = os.path.join(output_dir, f'sorted_{start_date}_ats_data.csv')
        sorted_data.to_csv(sorted_filename, index=False)

        print(f"Data saved for date range {start_date} to {end_date}.")
    else:
        print(f"No data received for date range {start_date} to {end_date}.")
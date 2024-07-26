import requests
import config
import csv 
import time


# This program gets the aggregate data, and saves it to 'aggregate_data.csv'
# This is used to get the symbols so that get_individual_data can run and get the individual ATS data

# Replace these with your actual API Client ID and API Client Secret
client_id = config.finra_api_client
client_secret = config.finra_api_secret
access_token = config.finra_access_token

# Define the API URL and parameters
api_url = "https://api.finra.org/data/group/otcMarket/name/weeklySummary"
params = {
    "limit": 1000,
    "offset": 0,
    "delimiter": ",",
    "quoteValues": "true",
    "async": "false",
    "dateRangeFilters": [{"startDate": "2024-06-03", "endDate": "2024-06-03", "fieldName": "weekStartDate"}],
    "domainFilters": [{"fieldName": "summaryTypeCode", "values": ['ATS_W_SMBL_FIRM']}],
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

all_data = []

while True:
    # Make the POST request
    api_response = requests.post(api_url, headers=headers, json=params)
    
    if api_response.status_code == 200:
        try:
            response_json = api_response.json()
            if not response_json:
                break  # Exit loop if no more data is returned
            
            all_data.extend(response_json)
            if len(response_json) == 0:
                break
            if len(response_json) < params['limit']:
                params['offset'] += len(response_json)
                break  # Exit loop if the number of records returned is less than the limit
            else:
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
    with open('ats_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = all_data[0].keys()  # Assuming all entries have the same keys
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for entry in all_data:
            writer.writerow(entry)
else:
    print("No data received.")
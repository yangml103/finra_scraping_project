import requests
import config

# Replace these with your actual API Client ID and API Client Secret
client_id = config.finra_api_client
client_secret = config.finra_api_secret
access_token = config.finra_access_token

# Define the API URL and parameters
api_url = "https://api.finra.org/data/group/otcMarket/name/weeklySummary"
params = {
    "limit": 20,
    "delimiter": ",",
    "quoteValues": "true",
    "async": "false",
    "dateRangeFilters": [{"startDate": "2024-06-03", "endDate": "2024-07-01", "fieldName": "lastUpdateDate"}],
    "domainFilters": [{"fieldName": "summaryTypeCode", "values": ["ATS"]}]
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# # Make the GET request
api_response = requests.post(api_url, headers=headers, params=params)


if api_response.status_code == 200:
    try:
        response_json = api_response.json()
        print("API Response:", response_json)
        # Write the response to a file
        with open('api_response_1.json', 'w') as file:
            for entry in response_json:
                file.write(f"{entry}\n")
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse JSON response.")
        print(api_response.text)
else:
    print(f"Failed to fetch data. Status code: {api_response.status_code}")
    print(api_response.text)

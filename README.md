1) Create config.py file and fill in the following:

finra_api_client = "your_client_id"
finra_api_secret = "your_client_secret"

2) Run get_access_token.py to get the access token and save it to config.py

3) Run file get_aggregates to get the aggregate data

4) Run get_individual_ats to get individual ats data per ticker

5) The filtered data is saved to a csv file

Note: get_data.py doesn't work as intended at the moment 

Need to find a way to get the correct number of rows returned from the api call

weekly summary contains the aggregates, you need to specify the exact company name to 
see the individual ats data
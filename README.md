1) Create config.py file and fill in the following:

finra_api_client = "your_client_id"
finra_api_secret = "your_client_secret"

2) Run get_access_token.py to get the access token and save it to config.py

3) Run file using_finra_api.py to get data, change rows_returned to the number of rows you want to get

4) Run filter_ats.py to filter the data and only keep the rows containing ATS in the summarytypecode

5) The filtered data is saved to a csv file

Note: get_data.py doesn't work as intended at the moment 
1) Create config.py file and fill in the following:

finra_api_client = "your_client_id"
finra_api_secret = "your_client_secret"

2) Run get_access_token.py to get the access token and save it to config.py

finra_access_token = "your_access_token"

3) Run file get_ats_data_v2.py to get the aggregate data - MAKE SURE TO CHANGE DATE RANGE AND OUTPUT_DIR

#NOTE date range MUST match date ranges in week start date in ATS OTC website - otctransparency.finra.org/AtsDownload

4) the outputs are saved to file name specified in OUTPUT_DIR 

5) Currently there are 5 programs that you can use to process the data

NOTE:

concat_ats_data concatenates data based on week start date NOT LAST UPDATE DATE.
This could lead to data at the end of the month still being updated in the next month.

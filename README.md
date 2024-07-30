1) Create config.py file and fill in the following:

finra_api_client = "your_client_id"
finra_api_secret = "your_client_secret"

2) Run get_access_token.py to get the access token and save it to config.py

finra_access_token = "your_access_token"

3) Run file get_ats_data to get the aggregate data

4) the outputs are saved to 2024_ats_data 

5) Currently there are 3 programs that you can use to process the monthly data - you can group by MPID, or by Issue Name or by Top 10 Issue Names PER MONTH

NOTE:

concat_ats_data concatenates data based on week start date NOT LAST UPDATE DATE.
This could lead to data at the end of the month still being updated in the next month.

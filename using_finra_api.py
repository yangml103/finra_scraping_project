from config import finra_access_token
from finra_api_queries import finra_api_queries
from datetime import datetime, timedelta

dataset_name = "weekly_summary"
my_access_token = finra_access_token
rows_returned = 20 # Change number depending on how much data you want 

# Calculate the Monday of 5 weeks in the past
today = datetime.today()
days_since_monday = today.weekday()  # Monday is 0 and Sunday is 6
monday_5_weeks_ago = today - timedelta(weeks=5, days=days_since_monday)
monday_10_weeks_ago = today - timedelta(weeks=10, days=days_since_monday)
# Use this filter if you want to find the data ending 5 weeks ago
date_filter_inputs_monday_5weeksago = [{'startDate': monday_10_weeks_ago.strftime('%Y-%m-%d'), 'endDate': monday_5_weeks_ago.strftime('%Y-%m-%d'), 'fieldName': 'lastUpdateDate'}] 


filters_input = {'summaryTypeCode': ['ATS_W_SMBL'], 'tierDescription' : ['NMS Tier 1']}
date_filter_inputs = [{'startDate': '2024-06-03', 'endDate': '2024-07-01', 'fieldName': 'lastUpdateDate'}]

output_1 = finra_api_queries.retrieve_dataset(dataset_name, my_access_token, rows_returned,
                                            date_filter = date_filter_inputs,
                                            filters = filters_input) 

output_1.to_csv('test_output3.csv', index=False)

#print(finra_api_queries.show_filterable_columns(dataset_name, my_access_token))
#['issueSymbolIdentifier', 'issueName', 'firmCRDNumber', 'MPID', 'marketParticipantName', '
#tierIdentifier', 'tierDescription', 'summaryStartDate', 'totalWeeklyTradeCount', 
# 'totalWeeklyShareQuantity', 'productTypeCode', 'summaryTypeCode', 'weekStartDate', 
# 'lastUpdateDate', 'initialPublishedDate', 'lastReportedDate', 'totalNotionalSum']
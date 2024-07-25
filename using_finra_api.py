from config import finra_access_token
from finra_api_queries import finra_api_queries
import json

dataset_name = "weekly_summary"
my_access_token = finra_access_token
rows_returned = 1000 # Change number depending on how much data you want 
#filters_input = {'summaryTypeCode': ['.*ATS.*']}
date_filter_inputs = [{'startDate': '2024-06-03', 'endDate': '2024-07-01', 'fieldName': 'lastUpdateDate'}]

output_1 = finra_api_queries.retrieve_dataset(dataset_name, my_access_token, rows_returned,
                                            date_filter = date_filter_inputs) 

#output_1.to_json('output_2.json', orient='records')
output_1.to_csv('test_output1.csv', index=False)

#print(finra_api_queries.show_filterable_columns(dataset_name, my_access_token))
#['issueSymbolIdentifier', 'issueName', 'firmCRDNumber', 'MPID', 'marketParticipantName', '
#tierIdentifier', 'tierDescription', 'summaryStartDate', 'totalWeeklyTradeCount', 
# 'totalWeeklyShareQuantity', 'productTypeCode', 'summaryTypeCode', 'weekStartDate', 
# 'lastUpdateDate', 'initialPublishedDate', 'lastReportedDate', 'totalNotionalSum']
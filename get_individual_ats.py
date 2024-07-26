from config import finra_access_token
from finra_api_queries import finra_api_queries
from datetime import datetime, timedelta

dataset_name = "weekly_summary"
my_access_token = finra_access_token
#rows_returned = 20 # Change number depending on how much data you want 



filters_input = {'issueName': ['Agilent Technologies Inc.'], 'tierDescription' : ['NMS Tier 1']}
date_filter_inputs = [{'startDate': '2024-07-22', 'endDate': '2024-07-22', 'fieldName': 'lastUpdateDate'}]

output_1 = finra_api_queries.retrieve_dataset(dataset_name, my_access_token,
                                            date_filter = date_filter_inputs,
                                            filters = filters_input) 
#print(output_1.content)
output_1.to_csv('test_output_change_issueName.csv', index=False)

#print(finra_api_queries.show_filterable_columns(dataset_name, my_access_token))
#['issueSymbolIdentifier', 'issueName', 'firmCRDNumber', 'MPID', 'marketParticipantName', '
#tierIdentifier', 'tierDescription', 'summaryStartDate', 'totalWeeklyTradeCount', 
# 'totalWeeklyShareQuantity', 'productTypeCode', 'summaryTypeCode', 'weekStartDate', 
# 'lastUpdateDate', 'initialPublishedDate', 'lastReportedDate', 'totalNotionalSum']
from config import finra_access_token
from finra_api_queries import finra_api_queries
from datetime import datetime, timedelta

dataset_name = "weekly_summary"
my_access_token = finra_access_token
rows_returned = 20 # Change number depending on how much data you want 


#'summaryTypeCode': ['ATS_W_SMBL'], and ATS_W_SMBL_FIRM both work 
filters_input = {'summaryTypeCode': ['ATS_W_SMBL_FIRM'], 'tierDescription' : ['NMS Tier 1']}
# Chose 2024-06-03 to be safe since the data is most likely not going to change 
# To find the actual data on the ots website https://otctransparency.finra.org/AtsIssueData
# look for the weekly report on the start date, in this case 2024-06-03
date_filter_inputs = [{'startDate': '2024-06-03', 'endDate': '2024-06-03', 'fieldName': 'weekStartDate'}]

output_1 = finra_api_queries.retrieve_dataset(dataset_name, my_access_token, rows_returned,
                                            date_filter = date_filter_inputs,
                                            filters = filters_input) 
#print(output_1.content)
output_1.to_csv('test_output_change_tierDescription2.csv', index=False)

#print(finra_api_queries.show_filterable_columns(dataset_name, my_access_token))
#['issueSymbolIdentifier', 'issueName', 'firmCRDNumber', 'MPID', 'marketParticipantName', '
#tierIdentifier', 'tierDescription', 'summaryStartDate', 'totalWeeklyTradeCount', 
# 'totalWeeklyShareQuantity', 'productTypeCode', 'summaryTypeCode', 'weekStartDate', 
# 'lastUpdateDate', 'initialPublishedDate', 'lastReportedDate', 'totalNotionalSum']
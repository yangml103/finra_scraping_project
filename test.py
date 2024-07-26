# File to test random code
from datetime import datetime, timedelta

def generate_date_ranges(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    date_list = []

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        date_list.append([date_str, date_str])
        current_date += timedelta(days=7)

    return date_list

# Example usage
#date_ranges = generate_date_ranges("2024-01-01", "2024-06-17")

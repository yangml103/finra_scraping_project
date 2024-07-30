import os
import pandas as pd

def process_monthly_files(directory):
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    
    monthly_data = {month: {} for month in months}

    for filename in os.listdir(directory):
        for month in months:
            if month in filename.lower():
                with open(os.path.join(directory, filename), 'r') as file:
                    df = pd.read_csv(file)
                    # Process the data as needed
                    print(f"Processing file: {filename}")

                    # Get unique MPIDs and their totalWeeklyShareQuantity
                    for mpid, group in df.groupby('MPID'):
                        if mpid not in monthly_data[month]:
                            monthly_data[month][mpid] = 0
                        monthly_data[month][mpid] += group['totalWeeklyShareQuantity'].sum()
                break

    # Combine all monthly data into a single DataFrame
    combined_data = []
    for month, data in monthly_data.items():
        for mpid, total in data.items():
            combined_data.append({'Month': month, 'MPID': mpid, 'Total Share Quantity': total})

    combined_df = pd.DataFrame(combined_data)
    combined_df.to_csv(os.path.join(directory, f'{directory_path}_MPID.csv'), index=False)



# Example usage
directory_path = '2024_ats_data'
process_monthly_files(directory_path)

    
from config import global_results, error_logs
import csv
from datetime import datetime

def save_results(results, output_file):
    # Open the CSV file to save the results
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(['Datetime', 'URL', 'StatusCode', 'ResponseSize'])  

        # Write the result rows
        for result in results:
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), result[0], result[1], result[2]])

def log_summary():
    # Print the scan summary
    print("\n--- Scan Summary ---")
    print(f"Total URLs scanned: {len(global_results)}")
    
    if len(error_logs) == 0:  # Check if there are no errors
        print("No errors encountered.")
    else:
        print(f"Total Errors: {len(error_logs)}")  # Print the number of errors

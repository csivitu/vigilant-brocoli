from config import global_results, error_logs
import csv
from datetime import datetime

def save_results(results, output_file):
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Datetime', 'URL', 'StatusCode', 'ResponseSize'])  

        for result in results:
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), result[0], result[1], result[2]])

def log_summary():
    
    print("\n--- Scan Summary ---")
    print(f"Total URLs scanned: {len(global_results)}")
    if error_logs:
        print("No errors encountered.")
    else:
        print(f"Total Errors: {len(error_logs)}")

import argparse
import signal
import sys
import os
from utils import create_output_directory
from reporting import log_summary, save_results
from scanner import perform_scan

def signal_handler(sig, frame):
    
    print("\nProcess interrupted by user. Saving results and exiting...")
        
    from config import global_results  
    save_results(global_results, args.output)  
    log_summary()

def main():
    
    signal.signal(signal.SIGINT, signal_handler)
    
    parser = argparse.ArgumentParser(description="URL and Directory Scanner")
    parser.add_argument('-u', '--url', required=False, help="Base URL to scan (e.g., http://example.com)")  
    parser.add_argument('-d', '--dlist', required=True, help="Directory list file (e.g., common.txt)")  
    parser.add_argument('--useragent', default="Mozilla/5.0", help="User-agent string")  
    parser.add_argument('--ignorecertificate', action='store_true', help="Ignore SSL certificate errors")  
    parser.add_argument('--threads', type=int, default=-1, help="Number of threads for concurrent scanning")  
    parser.add_argument('--timeout', type=int, default=5, help="Timeout for requests (in seconds)")  
    parser.add_argument('--output', default="output.csv", help="Output CSV file for results")  
    parser.add_argument('--verbose', action='store_true', help="Enable verbose logging")  

    global args  
    args = parser.parse_args()

    try:
        
        output_directory=create_output_directory(args.url)
        args.output = os.path.join(output_directory, args.output)
   
        perform_scan(args)
    
        log_summary()

    except KeyboardInterrupt:
        
        print("\nScan interrupted by user. Saving results and exiting...")
        from config import global_results
        save_results(global_results, args.output)  
        log_summary()

if __name__ == "__main__":
    
    main()

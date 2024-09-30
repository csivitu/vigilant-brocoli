import concurrent.futures
from config import global_results, error_logs
from utils import fetch_url, parse_ports, parse_directories, print_message
from reporting import save_results

def perform_scan(args):
    base_url = args.url  
    port = parse_ports(base_url)  
    directories = parse_directories(args)  
    headers = {'User-Agent': args.useragent}  
    urls_to_scan = []  
    
    print_message("Starting the scan on base URL:", base_url, verbose=args.verbose)
    
    for directory in directories:
        full_url = f"{base_url}:{port}/{directory}"
        urls_to_scan.append(full_url)
    
    # Using ThreadPoolExecutor to fetch URLs concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(fetch_url, url, headers, args.ignorecertificate, args.timeout, verbose=args.verbose): url for url in urls_to_scan}
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:  
                global_results.append(result)

    print_message("Scan completed", verbose=args.verbose)
    
    save_results(global_results, args.output)  # Call save_results to save the results after the scan

import os
import requests
from urllib.parse import urlparse
from config import error_logs
import sys

def print_message(*args, verbose=False):

    if verbose:
        print("", " ".join(map(str, args)))

def fetch_url(url, headers=None, ignore_ssl=False, timeout=None, verbose=False):
    
    try:
  
        sys.stdout.write(f"Scanning: {url}... ")
        sys.stdout.flush()
        response = requests.get(url, headers=headers, verify=not ignore_ssl, timeout=timeout, allow_redirects=True)
        
        if 400 <= response.status_code < 500:
            sys.stdout.write("Client Error\n")
            sys.stdout.flush()
            return None  
        
        sys.stdout.write(f"Found! Status Code: {response.status_code}\n")
        sys.stdout.flush()

        print_message(f"Fetched {url} with status {response.status_code}", verbose=verbose)
        return url, response.status_code, len(response.content)  

    except requests.RequestException as e:
        
        error_logs.append(f"Error fetching {url}: {e}")
        sys.stdout.write("Error\n")
        sys.stdout.flush()
        return None

def create_output_directory(url):
    
    parsed_url = urlparse(url)  
    domain_dir = parsed_url.hostname.replace(".", "_")  
    os.makedirs(domain_dir, exist_ok=True)
    return domain_dir

def parse_ports(url):
    
    parsed_url = urlparse(url)
    if parsed_url.port:  
        return parsed_url.port
    return 443 if parsed_url.scheme == "https" else 80  

def parse_directories(args):
    
    try:
        file_name = args.dlist  
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]  
    except FileNotFoundError:
        error_logs.append(f"Directory list file not found: {file_name}")  
        return []
    except Exception as e:
        error_logs.append(f"Error reading directory list file: {e}")  
        return []

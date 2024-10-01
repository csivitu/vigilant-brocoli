import os
import requests
from urllib.parse import urlparse
from config import error_logs
import sys

def print_message(*args):
        
    print("", " ".join(map(str, args)))

def fetch_url(url, headers=None, ignore_ssl=False, timeout=None, verbose=False):
    
    try:
  
        print(f"Scanning: {url}... ", end='', flush=True)

        response = requests.get(url, headers=headers, verify=not ignore_ssl, timeout=timeout, allow_redirects=True)
        
        if 400 <= response.status_code < 500:
            return None  
        
        print(f"Scanning: {url}... ", end='', flush=True)

        print(f"Found! Status Code: {response.status_code}\n", end='', flush=True)

        if verbose:
            print_message(f"Fetched {url} with status {response.status_code}")
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

def parse_ports(url):
    
    parsed_url = urlparse(url)
    return parsed_url.port or 443 if parsed_url.scheme == "https" else 80  

def parse_directories(args):
    
    try:
        file_name = args.dlist  
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]  
    except FileNotFoundError as e:
        error_logs.append(f"Directory list file not found: {e}")  
        return []  

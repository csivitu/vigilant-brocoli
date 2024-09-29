# URL and Directory Scanner

## Overview

A multithreaded Python tool to scan web servers for accessible directories and log results, including status codes and response sizes.
This Python project is a multithreaded URL and directory scanner designed to scan web servers for accessible directories and log the results. The scanner takes a base URL and a list of directories to check and generates a report of the status codes and response sizes for each scanned URL. It also handles error logging and generates a summary of the scan results.

## Features

- **Concurrent Scanning**: Uses multithreading for faster scanning with adjustable thread count.
- **Custom User-Agent**: Supports custom user-agent strings for requests.
- **SSL Certificate Handling**: Option to ignore SSL certificate validation errors.
- **Configurable Timeout**: Allows setting request timeout per URL.
- **Error Logging**: Captures and logs any errors encountered during the scan.
- **CSV Reporting**: Saves the results to a CSV file including the timestamp, URL, HTTP status code, and response size.
- **Graceful Interruption Handling**: Automatically saves the scan results and exits cleanly if interrupted.


## Requirements

- Python 3.x
- `requests` library

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py 
```
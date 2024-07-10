#!/usr/bin/python3
"""
Script that sends a request to a URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code.
"""
import requests
import sys

def fetch_url(url):
    """
    Fetch the URL and display the body of the response.
    If the HTTP status code is >= 400, display the error code.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_url(sys.argv[1])

#!/usr/bin/python3
"""
display the value of the X-Request-Id in the response header
"""
import requests
import sys


def fetch_header(url):
    """
    Fetch the header from the provided URL and display the X-Request-Id value
    """
    response = requests.get(url)
    header_value = response.headers.get('X-Request-Id')
    print(header_value)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_header(sys.argv[1])

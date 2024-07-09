#!/usr/bin/python3
"""
Script to handle HTTP errors and display the error code
"""
import urllib.request
import sys


def handle_request(url):
    """
    Fetch the URL and display the response body or error code
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else 'http://0.0.0.0:5050'
    handle_request(url)

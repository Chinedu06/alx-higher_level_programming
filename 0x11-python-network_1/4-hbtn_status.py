#!/usr/bin/python3
"""
Script to fetch the status from a URL
"""
import requests


def fetch_status(url):
    """
    Fetch the status from the provided URL and display the response
    """
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    fetch_status("https://alx-intranet.hbtn.io/status")

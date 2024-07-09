#!/usr/bin/python3
"""
Module that fetches https://intranet.hbtn.io/status
"""
import urllib.request


def fetch_status():
    """
    Fetch and print the body response from the given URL
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()

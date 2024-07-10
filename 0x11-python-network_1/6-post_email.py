#!/usr/bin/python3
"""
Takes URL and email sends a POST request with the email and displays response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)

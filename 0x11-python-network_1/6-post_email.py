#!/usr/bin/python3
"""
Script to send a POST request to a URL with an email as a parameter
"""
import requests
import sys

def send_post_request(url, email):
    """
    Send a POST request to the provided URL with the email as a parameter
    and display the body of the response
    """
    response = requests.post(url, data={'email': email})
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        send_post_request(sys.argv[1], sys.argv[2])

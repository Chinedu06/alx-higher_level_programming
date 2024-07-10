#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
with the letter as a parameter. The letter must be sent in the variable q.
If no argument is given, set q="".
If the response body is properly JSON formatted and not empty
Otherwise:
Display "Not a valid JSON" if the JSON is invalid.
Display "No result" if the JSON is empty.
"""
import requests
import sys


def search_user(letter=""):
    """
    Sends a POST request to the given URL with the letter as a parameter.
    Handles and displays the response.
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    try:
        response = requests.post(url, data=data)
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)

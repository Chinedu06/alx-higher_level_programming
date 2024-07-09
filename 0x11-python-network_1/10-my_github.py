#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Get GitHub credentials from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL
    url = "https://api.github.com/user"

    # Send GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Parse and display the user ID from the JSON response
    try:
        user_data = response.json()
        print(user_data.get("id"))
    except ValueError:
        print("None")


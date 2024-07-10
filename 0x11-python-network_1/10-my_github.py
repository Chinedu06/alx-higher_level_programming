#!/usr/bin/python3
"""
Takes your GitHub credentials and uses the GitHub API to display your id.

Usage:
./10-my_github.py <username> <personal_access_token>
"""
import requests
import sys


def fetch_github_id(username, token):
    """
    Fetches and displays the GitHub ID using the provided details
    """
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        json_response = response.json()
        print(json_response.get('id'))
    except ValueError:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
    else:
        username = sys.argv[1]
        token = sys.argv[2]
        fetch_github_id(username, token)

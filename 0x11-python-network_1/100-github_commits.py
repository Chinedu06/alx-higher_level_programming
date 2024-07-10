#!/usr/bin/python3
"""
Script that lists 10 commits  of the repository "rails" by the user "rails".

Usage:
./100-github_commits.py <repository_name> <owner_name>
"""
import requests
import sys


def fetch_commits(repo, owner):
    """
    Fetches and prints the 10 most recent commits from the specified
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error code: {response.status_code}")
        return

    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
    else:
        repository = sys.argv[1]
        owner = sys.argv[2]
        fetch_commits(repository, owner)

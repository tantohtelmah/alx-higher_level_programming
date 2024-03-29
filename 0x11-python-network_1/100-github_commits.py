#!/usr/bin/python3
"""
Inisialisation of the code
"""

import requests
import sys

def get_commits(repo_name, owner_name):
    base_url = "https://api.github.com/repos"
    url = f"{base_url}/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()

        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")

    except requests.RequestException as e:
        print(f"Error fetching commits: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name, owner_name = sys.argv[1], sys.argv[2]
    get_commits(repo_name, owner_name)

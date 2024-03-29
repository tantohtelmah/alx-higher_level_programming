#!/usr/bin/python3
"""
Inisialisation of the code
"""

import requests
import sys


def get_owner_id(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    try:
        response = requests.get(url)
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()

        repo_data = response.json()
        owner_id = repo_data.get("owner", {}).get("id")
        if owner_id:
            print(f"Owner ID for {owner_name}/{repo_name}: {owner_id}")
        else:
            print(f"Unable to retrieve owner ID for {owner_name}/{repo_name}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")


if __name__ == "__main__":
    repo_name_arg = sys.argv[1]
    owner_name_arg = sys.argv[2]
    get_owner_id(repo_name_arg, owner_name_arg)

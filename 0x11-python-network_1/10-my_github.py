#!/usr/bin/python3
"""
Inisialisation of the code
"""
import requests
import sys


def get_github_user_id(username, token):
    url = "https://api.github.com/user"
    headers = {"Authorization": f"Basic {username}:{token}"}

    try:
        response = requests.get(url, headers=headers)
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()

        user_data = response.json()
        user_id = user_data.get("id")
        if user_id:
            print(f"Your GitHub user ID: {user_id}")
        else:
            print("Unable to retrieve user ID.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python script_name.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    get_github_user_id(username, token)

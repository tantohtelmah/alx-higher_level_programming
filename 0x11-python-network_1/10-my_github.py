#!/usr/bin/python3
"""
Inisialisation of the code
"""
import requests
import sys

def get_user_id(username, token):
    try:
        url = f"https://api.github.com/user"
        headers = {
            "Authorization": f"Basic {username}:{token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get("id")
            print(f"Your GitHub user ID is: {user_id}")
        else:
            print(f"Error fetching user data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
        sys.exit(1)

    username, token = sys.argv[1], sys.argv[2]
    get_user_id(username, token)

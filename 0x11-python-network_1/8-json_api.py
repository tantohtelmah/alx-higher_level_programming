#!/usr/bin/python3
"""
Inisialisation of the code
"""

import requests
import sys


def search_user_by_letter(letter):
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    try:
        response = requests.post(url, data=payload)
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()

        data = response.json()
        if data:
            user_id = data.get("id")
            user_name = data.get("name")
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request to {url}: {e}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user_by_letter(letter_arg)

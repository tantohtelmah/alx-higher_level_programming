#!/usr/bin/python3
"""
Inisialisation of the code
"""
import requests
import sys


def send_post_request(url, email):
    try:
        payload = {"email": email}
        response = requests.post(url, data=payload)
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()

        content = response.text
        print(f"Body response:\n{content}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request to {url}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)

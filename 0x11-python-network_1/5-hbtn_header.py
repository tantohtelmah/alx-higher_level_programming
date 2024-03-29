#!/usr/bin/python3
"""
Inisialisation of the code
"""
import requests
import sys


def fetch_x_request_id(url):
    try:
        response = requests.get(url)
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()

        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(f"{x_request_id}")
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)

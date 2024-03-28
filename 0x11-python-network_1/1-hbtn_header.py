#!/usr/bin/python3
"""
Inisialisation of the code
"""
import urllib.request
import sys


def get_X_Request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.info()
            x_request_id = headers.get("X-Request-Id")
            if x_request_id:
                print(f"{x_request_id}")
            else:
                print("X-Request-Id not found in the response headers.")
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_X_Request_id(url)

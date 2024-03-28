#!/usr/bin/python3
"""
Inisialisation of the code
"""

import requests
import sys


def fetch_url_content(url):
    try:
        response = requests.get(url)
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()

        content = response.text
        print(content)
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            status_code = e.response.status_code
            print(f"Error code: {status_code}")
        else:
            print(f"Error fetching data from {url}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)

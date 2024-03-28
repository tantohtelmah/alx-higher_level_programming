#!/usr/bin/python3
"""
Inisialisation of the code
"""
import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode("utf-8")
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)

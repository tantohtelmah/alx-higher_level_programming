#!/usr/bin/python3
"""
Inisialisation of the code
"""
import requests


url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    # Raise an exception if the status code is not 200 (OK)
    response.raise_for_status()

    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {url}: {e}")

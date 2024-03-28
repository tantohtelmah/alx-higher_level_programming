#!/usr/bin/python3
"""
Inisialisation of the code
"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf8_content}")
except urllib.error.URLError as e:
    print(f"Error fetching data from {url}: {e}")

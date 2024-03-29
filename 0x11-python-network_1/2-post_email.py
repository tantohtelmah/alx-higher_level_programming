#!/usr/bin/python3
"""
Inisialisation of the code
"""
import urllib.request
import sys


def send_Post_Request(url, email):
    try:
        # Encode the email parameter
        data = urllib.parse.urlencode({"email": email}).encode("utf-8")
        print("hi")
        # Create a POST request
        with urllib.request.urlopen(url, data=data) as response:
            print("hi")
            content = response.read().decode("utf-8")
            print(f"Your email is: {content}")
    except urllib.error.URLError as e:
        response_data = e.reason
        print(f"Error reason: {response_data}")
        print(f"Error sending POST request to {url}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_Post_Request(url, email)

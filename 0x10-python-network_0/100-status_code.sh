#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a request using curl and capture the status code
http_status=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Display the status code
echo "HTTP status code: $http_status"

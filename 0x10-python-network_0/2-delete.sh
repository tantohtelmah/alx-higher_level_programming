#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a DELETE request using curl and store the response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" -w "%{http_code}" "$url"

# Get the HTTP status code from the last line of the response
http_status=$(tail -n 1 "$response_file")

# Check if the status code is 200 (OK)
if [ "$http_status" -eq 200 ]; then
    # Display the body of the response
    cat "$response_file" | sed '$d'  # Remove the last line (status code)
else
    echo "Error: HTTP status code $http_status"
fi

# Clean up the temporary file
rm "$response_file"

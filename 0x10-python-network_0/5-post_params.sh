#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Variables for the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request using curl, include the variables, and store the response in a temporary file
response_file=$(mktemp)
curl -s -X POST -d "email=$email&subject=$subject" "$url" > "$response_file"

# Display the body of the response
cat "$response_file"

# Clean up the temporary file
rm "$response_file"

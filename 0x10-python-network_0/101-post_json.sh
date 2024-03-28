#!/bin/bash

# Check if both URL and filename arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Get the URL and filename from the command line arguments
url="$1"
filename="$2"

# Read the contents of the file
json_data=$(cat "$filename")

# Send a POST request using curl, include the JSON data, and store the response in a temporary file
response_file=$(mktemp)
curl -s -X POST -H "Content-Type: application/json" -d "$json_data" "$url" > "$response_file"

# Display the body of the response
cat "$response_file"

# Clean up the temporary file
rm "$response_file"

#!/bin/bash
# sends a JSON POST request to the specified URL using curl
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"

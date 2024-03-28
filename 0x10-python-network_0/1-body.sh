#!/bin/bash
# sends a GET request to the URL
curl -s -o /dev/null -w "%{http_code}" "$1"

#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me
curl -s -o /dev/null -w "%{http_code}" 0.0.0.0:5000/catch_me

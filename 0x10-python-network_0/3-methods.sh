#!/bin/bash
# isplays the supported HTTP methods
curl -i -L -X OPTIONS "$1" | grep -i "allow"

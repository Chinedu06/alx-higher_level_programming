#!/bin/bash
# Sends a GET request to the URL and displays the body of a 200 status code response
response=$(curl -s -o /dev/stderr -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && cat /dev/stderr

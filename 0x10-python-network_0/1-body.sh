#!/bin/bash
# Sends a GET request to the URL and displays only the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" -o /dev/stdout | grep -q "200$" && curl -sL "$1"

#!/bin/bash
# Sends a GET request to a URL and displays the body of the response if the status code is 200
curl -s -o - -w "%{http_code}" "$1" | awk '/200$/{print x};{x=$0}'

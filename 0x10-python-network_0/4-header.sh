#!/bin/bash
# Sends a GET request to a URL with a header variable X-School-User-Id set to 98 and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"


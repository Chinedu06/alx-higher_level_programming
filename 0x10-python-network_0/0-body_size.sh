#!/bin/bash
# Script to get the size of the response body for a given URL
curl -s "$1" | wc -c


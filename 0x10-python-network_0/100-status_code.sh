#!/bin/bash
# script that sends a request to a URL passed as an argument
url=$1

response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
echo $response

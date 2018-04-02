# URL-Verification-2

# This repository contains a script to verify URLs given from a .csv file as an input

# Imported modules/libraries are:
# codecs, requests, socket, urllib, json, pandas

# Every existing URL in the file is being verified if it's:
# 1. Working URL ('Working' or 'Redirect') based on the HTTP status code 2xx, and HTTP status code 3xx with requests history
# 2. Non-working URL (Non-existing URL in the server) based on the HTTP status cooe 4xx
# 3. URLs with Internal server problems (excluded in the result file) based on the HTTP status code 5xx

# With the help of pandas module in Python, created a DataFrame based on columns:
# 1. URLs (shown the ones from the list above)
# 2. Result (shown the results for verifying URLs)


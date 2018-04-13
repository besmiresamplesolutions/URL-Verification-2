# URL-Verification-2

This repository contains 2 main folders: [Splitted-file-for-AWS] and [URL-Verification]

1. [Splitted-file-for-AWS] contains a script that automates to split the input file into different files for each 80 lines
2. [URL-Verification] contains two subfolders:
  2.1 URL-Verification (1) is the 1st version of processing the file with URLs in order to verify them
  2.2 URL-Verification (2) is the 2nd version which has been updated to get the input file and output file as arguments

Imported modules/libraries are:
codecs, requests, socket, urllib, pandas, sys

How do we verify URLS:

Every existing URL in the file is being verified if it's:
  1. Working URL ('Working' or 'Redirect') based on the HTTP status code 2xx, and HTTP status code 3xx with requests history
  2. Non-working URL (Non-existing URL in the server) based on the HTTP status code 4xx
  3. URLs with Internal server problems (excluded in the result file) based on the HTTP status code 5xx

With the help of pandas module in Python, created a DataFrame based on columns:
  1. URLs (shown the ones from the list above)
  2. Result (shown the results for verifying URLs)
  3. Redirected_URL (shows the last redirected URL if the URL is redirected)

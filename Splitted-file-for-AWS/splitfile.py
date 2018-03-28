import codecs
import codecs
import requests
import socket
import urllib
import boto3
import json
import glob

global lines_per_file
global smallfile 

def split_file(file):
	lines_per_file = 80
	smallfile = None

	with open(file) as bigfile:
	    for lineno, line in enumerate(bigfile):
	        if lineno % lines_per_file == 0:
	            if smallfile:
	                smallfile.close()
	            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
	            smallfile = open(small_filename, "w")
	        smallfile.write(line)
	    if smallfile:
	        smallfile.close()

split_file('file_urls.txt')


urls = codecs.open('small_file_80.txt')


# with open('small_file_*[0-9].txt') as f:
#     urls = f.readlines()
#     content = [x.strip() for x in urls] 
#     # print(urls)

for name in glob.glob('small_file_*[0-9].txt'):
    try:
	    for url in urls:
	        print("__________")
	        try:
	            socket.setdefaulttimeout(8000)
	            req = requests.head("http://" + url[:-1])
	            # print(url)
	            print(req.status_code)
	            r = req.status_code
	            request = str(r)
	            if(request[0] == '3'):
	                print(url,": redirect")
	            elif(request[0] == '2'):
	                 print(url,": working")
	            elif(request[0] == '4'):
	                print(url,": not working")
	            # return req.status_code
	        except urllib.error.URLError as e:
	            print(e.reason)
	        except:
	            print(url,": invalid url")

    except:
        print(ex)

# for name in glob.glob('small_file_*[0-9].txt'):
# 	print(name)

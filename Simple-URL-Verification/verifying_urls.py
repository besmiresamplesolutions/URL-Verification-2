import codecs
import requests
import socket
import urllib
import json


urls = codecs.open('file_urls.txt', 'r', 'utf-8')

for url in urls:
    print("__________")

    try:
        socket.setdefaulttimeout(8000)
        req = requests.head("http://" + url[:-2])
        print(url)
        print(req.status_code)
        r = req.status_code
        request = str(r)
        if(request[0] == '3'):
            print("Redirect")
        elif(request[0] == '2'):
             print("Working")
        elif(request[0] == '4'):
            print("Not working")
        # return req.status_code
    except urllib.error.URLError as e:
        print(e.reason)
    except:
        print("Exception: our program couldn't get the IP from website")


# print(validator.validate_website_url("e--l,34lm234--gps.nl"))rijke.biz

# if __name__ == '__main__':
# 	for i in range(4):
# 		p = mp.Process(target=verify_url)
# 		urllist = []
# 		urllist.append(p)
# 		p.start()
# 		print(p)
# 		# print(urllist)
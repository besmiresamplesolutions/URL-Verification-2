import codecs
import requests
import socket
import urllib
import json
import pandas as pd


urls = codecs.open('file_urls.csv', 'r', 'utf-8')

given_urls = []
results = []

filename = "verified_urls.csv"

try:
    f = open(filename, "a")
    f.seek(0)
    f.truncate()
except:
    print("Please close the .csv file in order for changes to append")

def verify_urls():
    # Going through each URL in the file
    for url in urls:

        # given_urls.append(url[:-2])

        print("__________")

        try:
            socket.setdefaulttimeout(8000)
            req = requests.get("http://" + url[:-2])

            # At first we print the URL
            print(url)

            print(req.status_code)

            # Saving the status code in a variable to String 
            r = req.status_code
            request = str(r)

            if(request[0] == '2'):
                if(req.history):
                    # This is for checking the redirect URLs
                    for i, response in enumerate(req.history, 1):
                        print("Redirect: ", response.url)
                    result = "Redirect"
                    results.append(result)
                    given_urls.append(url[:-2])
                else:
                    result = "Working"
                    print(result)
                    results.append(result)
                    given_urls.append(url[:-2])

            elif(request[0] == '4'):
                result = "Not working"
                print(result)
                results.append(result)
                given_urls.append(url[:-2])

            elif(request[0] == '5'):
                result = "Internal server problems"
                print(result)
                results.append(result)
                given_urls.append(url[:-2])

            else:
                result = " "
                print(result)
                # results.append(result)

        except urllib.error.URLError as e:
            print(e.reason)
            continue

        except requests.exceptions.SSLError as q:
            print(url)
            print("SSL Error")
            pass
   
    # print(given_urls)
    # print(results)

    raw_data = {'urls': given_urls,
                'result': results}

    df = pd.DataFrame(raw_data, columns = ['urls','result'])
    df.to_csv(f)

verify_urls()

f.close()
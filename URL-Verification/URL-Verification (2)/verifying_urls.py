import codecs
import requests
import socket
import urllib
import pandas as pd
from time import sleep
import sys

# proxy_support = urllib.request.ProxyHandler({"http":"http://61.233.25.166:80"})
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)

# urls = codecs.open('urls.csv', 'r', 'utf-8')

given_urls = []
redirect_urls = []
results = []

filename = "verified_urls.csv"

def verify_urls(csv_file):
    # Going through each URL in the file
    with open(csv_file) as csvfile:
        for url in csvfile:
            try:
                url = url.strip()
                print(url)
                socket.setdefaulttimeout(8000)
                req = requests.get("http://" + url)
                # req = urllib.request.("http://" + url[:-2])

                # At first we print the URL and the status code
                # print(url,req.status_code)
                # print(req.status_code)

                # Saving the status code in a variable to String 
                r = req.status_code
                request = str(r)

                if(request[0] == '2'):
                    # This is for checking the redirect URLs
                    if(req.history):
                        # for i, response in enumerate(req.history, 1):
                            # print("Redirect: ", response.url)
                        result = "Redirect"
                        redirect_urls.append(req.url)
                        results.append(result)
                        given_urls.append(url)

                    else:
                        result = "Working"
                        # print(result)
                        redirect_urls.append(" ")
                        results.append(result)
                        given_urls.append(url)

                elif(request[0] == '4'):
                    result = "Not working"
                    # print(result)
                    redirect_urls.append(" ")
                    results.append(result)
                    given_urls.append(url)

                elif(request[0] == '5'):
                    result = "Internal server problems"
                    # print(result)
                    redirect_urls.append(" ")
                    results.append(result)
                    given_urls.append(url)

                else:
                    result = " "
                    # print(result)
                    # results.append(result)

            except urllib.error.URLError as e:
                print(e.reason)
                continue

            except requests.exceptions.SSLError as q:
                print(url)
                print("SSL Error")
                continue

            except requests.exceptions.ConnectionError:
                # print(url)
                # r.status_code = "Connection Refused"
                continue

    try:
        f = open(output_file, "a")
        f.seek(0)
        f.truncate()
    except IOError:
        print("Please close the .csv file in order for changes to append")

    raw_data = {'urls': given_urls,
                'result': results,
                'redirect_urls': redirect_urls}

    df = pd.DataFrame(raw_data, columns = ['urls','result','redirect_urls'])
    df = df.drop_duplicates('urls')
    df.to_csv(f, index=False)
    f.close()

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    verify_urls(input_file)

print("Processing succeeded")
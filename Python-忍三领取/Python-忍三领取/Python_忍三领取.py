
import urllib
import http.client as httplib
import json

uidlist = [202224897,607467589,400196835]
urlAddr = "statistics.pandadastudio.com"
print("Please input the gift code:")
code = input()

conn = httplib.HTTPConnection(urlAddr)
for i in uidlist:
    paramCODE = urllib.parse.urlencode({'uid': i, 'code':code})
    paramUID = urllib.parse.urlencode({'uid': i})
    failure = []

    conn.request("GET", "/player/simpleInfo?" + paramUID)
    response = conn.getresponse()
    data = json.load(response)
    print("user load status: ",data['msg'])
    if data['code'] == 0:
        print(data['data']['name'], "<-   NAME¦¦¦RANK   ->" ,data['data']['title'])
        conn.request("GET", "/player/giftCode?" + paramCODE)
        response = conn.getresponse()
        data = json.load(response)
        print("gift code status: ",data['msg'])
    else:
        failure.append(i)
    print("-----------------------------------------")

print("Failure:", failure)


    
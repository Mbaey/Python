import urllib.request
import urllib.response
import json

url = "http://www.tuling123.com/openapi/api"
postdata =urllib.parse.urlencode({
    "key":"e904088025004ef4af76481e91b7d1da",
    "info":"你爸是谁？"
 }).encode('utf-8')

req = urllib.request.Request(url, postdata)

print(urllib.request.urlopen(req).read().decode('utf-8'))
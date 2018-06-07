import urllib.request
import urllib.response
import json

url = "http://www.tuling123.com/openapi/api"
postdata =urllib.parse.urlencode({
    "key":"e904088025004ef4af76481e91b7d1da",
    "info":"我会努力的"
 }).encode('utf-8')
# header = {
#  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#  "Accept-Encoding":"utf-8",
# "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
#  "Connection":"keep-alive",
#  "Host":"c.highpin.cn",
#  "Referer":"http://c.highpin.cn/",
#  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
#  }
# request = urllib.request(url, body_value,header)
req = urllib.request.Request(url, postdata)

print(urllib.request.urlopen(req).read().decode('utf-8'))
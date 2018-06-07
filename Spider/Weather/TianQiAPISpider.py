import time
import urllib.request
import urllib.response
import json

t = time.time()
# http://d1.weather.com.cn/dingzhi/101160101.html?_=1509784667168
# http://d1.weather.com.cn/dingzhi/101160101.html?_=1509784667168
url= 'http://d1.weather.com.cn/dingzhi/101160101.html?_=1509786317042'
# header = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
he = {'Host':'d1.weather.com.cn',
'Referer':'http://www.weather.com.cn/weather1dn/101160101.shtml',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
request = urllib.request.Request(url,headers=he)
# urllib.request.urlopen({api_url}, data=bytes(json.dumps(headers), encoding="utf-8"))  #我没有写headers=he， 所以一开始的he被认为是data的参数了。而它貌似需要bytes

# try:
page = urllib.request.urlopen(request)
s = page.read().decode('utf-8')
print(url)
print(s)
# s = s[s.find('{'):]
# result = json.loads(s)
# print(result)
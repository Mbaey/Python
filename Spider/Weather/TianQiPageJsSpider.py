import time
import urllib.request
import urllib.response
import json
from bs4 import BeautifulSoup

t = time.time()
url= 'http://forecast.weather.com.cn/town/weather1dn/101160101002.shtml'
# header = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
he = {'Host':'d1.weather.com.cn',
'Referer':'http://www.weather.com.cn/weather1dn/101160101.shtml',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
request = urllib.request.Request(url,headers=he)
response = urllib.request.urlopen(request)
html = response.read()
# print(html.decode('utf-8',errors='ignore'))
soup = BeautifulSoup(html, 'lxml')

# 当时学的时候还不知道
info = soup.select('div.todayLeft')
print(info)


# 直接返回的就是一个beautifulsoup的对象啊。。。
# info = html.select('#info')[0]
# info = info.get_text().split('\n')


# 提取字段，只要冒号后面的文本内容
# director = info[1].split(':')[-1].strip()
# composer = info[2].split(':')[-1].strip()
# actor = info[3].split(':')[-1].strip()
# category = info[4].split(':')[-1].strip()
# district = info[6].split(':')[-1].strip()
# language = info[7].split(':')[-1].strip()
# showtime = info[8].split(':')[-1].strip()
# length = info[9].split(':')[-1].strip()
# othername = info[10].split(':')[-1].strip()

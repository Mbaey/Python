import requests
import re

#感谢 https://github.com/LiuXingMing/Tmall1212
id='531688551059'
#商品详情接口
url = 'https://detail.m.tmall.com/item.htm?id=%s' % id
#property 接口
#url = 'https://mdetail.tmall.com/mobile/itemPackage.do?itemId=%s' % sid
r = requests.get(url, timeout=10)
context = r.content.decode('gbk', 'ignore')
data_detail = re.findall('_DATA_Detail = (.*?);</script>', context )
print(data_detail)

f=open(id+'.json', 'w')
for i in data_detail:
	f.write(i+'\r\n')
f.flush()
f.close()
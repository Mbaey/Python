import re
import urllib.request


def getHtml(path):
    page = urllib.request.urlopen(path)
    html = page.read()
    return html

def getImg(html):
    pImg = r'src="(http.+\.jpg)" pic'
    imgRe = re.compile(pImg)
    return re.findall(imgRe, html.decode('utf-8'))
    

html = getHtml("https://tieba.baidu.com/p/2460150866?pn=2")
imglist = getImg(html)

x = 0
for imgurl in imglist:
    urllib.request.urlretrieve(imgurl, '%s.jpg'%x)
    x+=1


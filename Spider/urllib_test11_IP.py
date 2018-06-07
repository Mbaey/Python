from urllib import request
# 参考文章
# http://blog.csdn.net/c406495762/article/details/60137956
if __name__ == "__main__":
    #访问网址
    url = 'http://www.whatismyip.com.tw/'
    #这是代理IP
    proxy = {'http':'61.135.217.7:80'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    headers = {'referer': 'https://translate.google.cn/',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    #添加User Angent
    # opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)

    req = request.Request(url, headers=headers)

    #使用自己安装好的Opener
    response = request.urlopen(req)
    print(url)

    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)
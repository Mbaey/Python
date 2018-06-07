# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
url = "http://news.nwnu.edu.cn/Index.php/guangyingshida/index-9.html"
#
# http://blog.csdn.net/c406495762/article/details/69817490
url_head = "http://news.nwnu.edu.cn/"
count = 1
if __name__ == '__main__':
    for i in range(1, 9):
        url = 'http://news.nwnu.edu.cn/Index.php/guangyingshida/index-'+str(i)+'.html'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

        req = request.Request(url, headers=headers)

        # 使用自己安装好的Opener
        response = request.urlopen(req)

        # 读取相应信息并解码
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, 'lxml')
        select = soup.select("div.meitu_pic")
        # 打印信息
        find_all = select[0].select("div")[1].find_all('img')
        for url_rear in  find_all:
            img_url = url_head + url_rear.get('src')
            try:
                print(img_url)
                response = request.urlopen(img_url)
                cat_img = response.read()

                with open('nwnu'+str(count)+'.jpg', 'wb') as f:
                    f.write(cat_img)
                count += 1
            except Exception as e:
                print(e)



import time

from http import cookiejar
from bs4 import BeautifulSoup
import json



if __name__ == '__main__':


# print(html.decode('utf-8',errors='ignore'))
    html = open(r'1.txt', encoding='utf-8').read()
    res = open(r'2.txt', mode='w', encoding='utf-8')
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    #
    info = soup.get_text()
    print(info)
    res.write(info)
    res.flush()

    res.close()
    # info = soup.select('div.todayLeft')[0]
    # lifeHelper = soup.select('div.lv')[0]
    # print(lifeHelper)


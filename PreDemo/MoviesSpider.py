#coding: utf-8
import urllib.request
import urllib.response
import json
from bs4 import BeautifulSoup

tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie&tag=%E7%83%AD%E9%97%A8&source=index'

page = urllib.request.urlopen(url)
result = json.loads(page.read().decode('utf-8'))

tags = result['tags']
# https://movie.douban.com/j/search_tags?type=movie&tag=%E7%83%AD%E9%97%A8&source=index
movies = []
for tag in tags:
    limit = 0
    while 1 :
        url=  'https://movie.douban.com/j/search_subjects?type=movie&tag='+ urllib.parse.quote(tag) + '&page_limit=40&page_start=' + str(limit)
        page = urllib.request.urlopen(url)
        result = json.loads(page.read().decode('utf-8'))
        print(url)

        result = result['subjects']
        if(len(result) == 0):
            break
        limit += 20
        for item in result:
            movies.append(item)

        ##
        break
    ##
    break
for x in range(len(movies)):
    item = movies[x]
    page = urllib.request.urlopen(item['url'])
    result = page.read().decode('utf-8')
    html = BeautifulSoup(result, "html.parser")
    title = html.select('h1')[0]
    text = title.select('span')[0].get_text()
    print(text)


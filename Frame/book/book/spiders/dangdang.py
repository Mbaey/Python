# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    # allowed_domains = ['http://category.dangdang.com/pg100-cp01.05.16.00.00.00.html']
    start_urls = [
        'http://category.dangdang.com/pg1-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg2-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg3-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg4-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg5-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg6-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg7-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg8-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg9-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg10-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg11-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg12-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg13-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg14-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg15-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg16-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg17-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg18-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg19-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg20-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg21-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg22-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg23-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg24-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg25-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg26-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg27-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg28-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg29-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg30-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg31-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg32-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg33-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg34-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg35-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg36-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg37-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg38-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg39-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg40-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg41-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg42-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg43-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg44-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg45-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg46-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg47-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg48-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg49-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg50-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg51-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg52-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg53-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg54-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg55-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg56-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg57-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg58-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg59-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg60-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg61-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg62-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg63-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg64-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg65-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg66-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg67-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg68-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg69-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg70-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg71-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg72-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg73-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg74-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg75-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg76-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg77-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg78-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg79-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg80-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg81-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg82-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg83-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg84-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg85-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg86-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg87-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg88-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg89-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg90-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg91-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg92-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg93-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg94-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg95-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg96-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg97-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg98-cp01.05.16.00.00.00.html',
'http://category.dangdang.com/pg99-cp01.05.16.00.00.00.html'
    ]
    # def __init__(self):
    #     for i in range(1, 100):
    #         self.start_urls.append('category.dangdang.com/pg'+str(i)+'-cp01.05.16.00.00.00.html/')
    #     print(self.start_urls)


    def parse(self, response):
        ul = response.css('ul.bigimg')
        a = ul.css('a[name="itemlist-title"]::attr(href)').extract()
        for bookDataUrl in a:
            # yield scrapy.Request(url=bookDataUrl, callback=self.parseBookData)
            return scrapy.Request(url=bookDataUrl, callback=self.parseBookData)

    def parseBookData(self, response):
        book = BookItem()
        
        print("到啦")
        return

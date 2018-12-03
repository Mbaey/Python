# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    书名 = scrapy.Field()
    简介 = scrapy.Field()
    作者 = scrapy.Field()
    出版社 = scrapy.Field()
    出版时间 = scrapy.Field()
    版次 = scrapy.Field()
    页数 = scrapy.Field()
    字数 = scrapy.Field()
    印刷时间 = scrapy.Field()
    开本 = scrapy.Field()
    纸张 = scrapy.Field()
    包装 = scrapy.Field()
    是否套装 = scrapy.Field()
    国际标准书号ISBN = scrapy.Field()
    所属分类 = scrapy.Field()
    内容简介 = scrapy.Field()
    作者简介 = scrapy.Field()
    目录 = scrapy.Field()
    媒体评论 = scrapy.Field()
    imgURL = scrapy.Field()
    pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AiraqiItem(scrapy.Item):
    # define the fields for your item here like:
    城市 = scrapy.Field()
    日期 = scrapy.Field()
    质量等级 = scrapy.Field()
    AQI = scrapy.Field()
    AQI排名 = scrapy.Field()
    PM25 = scrapy.Field()
    PM10 = scrapy.Field()
    So2 = scrapy.Field()
    No2 = scrapy.Field()
    Co = scrapy.Field()
    O3 = scrapy.Field()
    pass

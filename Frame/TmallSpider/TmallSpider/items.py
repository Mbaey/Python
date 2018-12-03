# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GoodsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # id = scrapy.Field()
    id = scrapy.Field()
    # store_name = scrapy.Field() #不插入goods
    # name = scrapy.Field()
    # month_sun = scrapy.Field()
    # comment_sum = scrapy.Field()
    # goods_type = scrapy.Field()
    # price_high = scrapy.Field()
    # price_low = scrapy.Field()
    # sales_id = scrapy.Field()#先写入sales 再找到sales_id
    # froms = scrapy.Field()
    # yunfei = scrapy.Field()
    # display = scrapy.Field()
    # level = scrapy.Field()
    # desc = scrapy.Field()
    # img1 = scrapy.Field()
    # img2 = scrapy.Field()
    # img3 = scrapy.Field()
    # img4 = scrapy.Field()
    # img5 = scrapy.Field()
    pass

# class ShopItem(scrapy.Item):
#     id = scrapy.Field()
#     shop = scrapy.Field()
#     pass
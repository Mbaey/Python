# -*- coding: utf-8 -*-
import scrapy


class AirSpider(scrapy.Spider):
    name = 'air'
    allowed_domains = ['http://www.tianqihoubao.com/aqi/']
    start_urls = ['http://http://www.tianqihoubao.com/aqi//']

    def parse(self, response):
        pass

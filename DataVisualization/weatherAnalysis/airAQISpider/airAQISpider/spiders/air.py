# -*- coding: utf-8 -*-
import scrapy

from airAQISpider.items import AiraqiItem


class AirSpider(scrapy.Spider):
    name = 'air'
    # allowed_domains = ['http://www.tianqihoubao.com/aqi/']
    bas_url=  "http://www.tianqihoubao.com"
    # start_urls = ['http://www.tianqihoubao.com/aqi/beijin.html']
    start_urls = ['http://www.tianqihoubao.com/aqi']
    row = ['日期', '质量等级', 'AQI', 'AQI排名', 'PM25', 'PM10', 'So2', 'No2', 'Co', 'O3']
    # def parse(self, response):
    #     Li = response.css('div.box.pcity ul li')  # 所有城市
    #     urlList  = Li.css('li a::attr(href)').extract()
    #     print('response.url： ***********'+response.url)
    #     for url in urlList:
    #         url  = self.bas_url+url
    #         print(url)
    #         return scrapy.Request(url=url, callback=self.parseUrlList)
    #         # yield scrapy.Request(url=url, callback=self.parseUrlList)
    #     pass
    #
    def parse(self, response):
        dl = response.css('div.citychk dl')

        for i in range(1, len(dl)):
            for a in dl[i].css('dd a::attr(href)'):
                url = a.extract()
                url  = self.bas_url+url
                print(url)
                # return scrapy.Request(url=url, callback=self.parseUrlList)
                yield scrapy.Request(url=url, callback=self.parseUrlList)
        pass

    def parseUrlList(self, response):
        LI = response.css('div.box.p ul li')  # 所以历史记录的URL
        DataUrlList = LI.css('a::attr(href)').extract()
        for url in DataUrlList:
            url = self.bas_url + url
            print(url)
            # return scrapy.Request(url, self.parseAqiData)
            yield scrapy.Request(url, self.parseAqiData)
        # '/aqi/beijing-201806.html'
        pass

    def parseAqiData(self, response):
        trs = response.css("table.b tr")
        data = AiraqiItem()
        data['城市'] = response.css("div.box h3::text").extract_first().strip()[0:-4]
        for i in range(1, len(trs)):
            tr = trs[i]
            td = tr.css('td::text').extract()
            for i in range(10):
                data[self.row[i]] = td[i].strip()
            yield data
            # print(data)
        pass

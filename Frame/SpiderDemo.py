import scrapy

# from Frame.airAQISpider.airAQISpider.items import AiraqiItem


class QuotesSpider(scrapy.Spider):
    name = "air"
    start_urls = [
        'http://www.tianqihoubao.com/aqi/beijing-201806.html',
    ]

    def parse(self, response):
        print(len(response.css("table.b tr")) , "\n\n\n\n")
        trs = response.css("table.b tr")
        data= {}
        data['城市'] = response.css("div.box h3::text").extract_first().strip()[0:-4]
        for i in range(1, len(trs)) :
            tr = trs[i]
            row = ['日期','质量等级','AQI','AQI排名','PM2.5','PM10','So2','No2','Co','O3']
            td = tr.css('td::text').extract()
            for i in range(10):
                data[row[i]] = td[i].strip()
            yield data
            print(data)

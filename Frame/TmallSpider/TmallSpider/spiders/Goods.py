# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from TmallSpider.items import GoodsItem
from TmallSpider.spiders.goodsList import goodslist
import re
import requests
# from Frame.TmallSpider.TmallSpider.items import GoodsItem
from scrapy.http import HtmlResponse
class GoodsSpider(scrapy.Spider):
    name = 'Goods'
    allowed_domains = ['tmall.com']
    # start_urls = goodslist
    start_urls = ['https://list.tmall.com/search_product.htm?spm=875.7789098.2015148.95.E9N2SH&pos=14&cat=50039580&style=g&acm=2016031510.1003.2.721902&from=sn_1_rightnav&sort=s&search_condition=23&tmhkmain=0&scm=1003.2.2016031510.OTHER_1501656449192_721902&aldid=4LNHmpMY&industryCatId=50039482']

    def parse(self, response):
        prodects = response.css('div.product')
        print("哈哈list list")
        for prodect in prodects:
            href = prodect.css('p.productTitle a::attr(href)').extract_first()
            id= re.findall('id=(.*?)&', href)[0]
            detailUrl = 'https://detail.m.tmall.com/item.htm?id=%s'% id
            print(detailUrl)
            # print(goods['id'])
            goods = GoodsItem()
            r = requests.get(detailUrl, timeout=10)
            context = r.content.decode('gbk', 'ignore')
            goods['id'] = re.findall('_DATA_Detail = (.*?);</script>', context)
            print(goods)
            return goods

    # def parseGoods(self, response):
    #
    #     print(response.text)
    #     goods['id']=re.findall('_DATA_Detail = (.*?);</script>', response.text )
    #     yield goods
    #     goods['store_name']=response.css('a.slogo-shopname strong::text').extract_first()
    #     info1=response.css('div.tb-wrap')
    #     goods['name'] = info1.css('h1::text').extract_first()
    #
    #     count = info1.css('span.tm-count::text').extract()
    #     print(count)
    #     goods['month_sun'] = None
    #     goods['comment_sum'] = None
    #     goods['goods_type'] = None
    #
    #     price = info1.css('span.tm-price::text').extract()
    #     if(len(price) == 1):
    #         goods['price_high'] = None
    #         goods['price_low'] = price[0]
    #     else:
    #         goods['price_high'] = price[0]
    #         goods['price_low'] = price[1]
    #     goods['sales_id'] = None
    #     goods['froms'] = None
    #     goods['yunfei'] = None
    #     goods['display'] = None
    #     goods['level'] = None
    #     goods['img1'] = None
    #     goods['img2'] = None
    #     goods['img3'] = None
    #     goods['img4'] = None
    #     goods['img5'] = None
    #
    #
    #     goods['desc'] = None
    #     print("哈哈prodect")
    #     yield goods
    #     pass
        # return



# if __name__  == "__main__":
#     listlist =  open(r"list's list1.txt", "r", encoding='UTF-8')
#     response  = listlist.read()
#     listlist.close()
#     txt = open("GoodsList.txt", "w", encoding="UTF-8")
#     print(response)
#     res  = Selector(text=response).get.css('a.hot-word::attr(href)').extract()
#
#     for url in res:
#         txt.writelines(url+'\n')
#     print(len(res))
#     txt.flush()
#     txt.close()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'db_weather',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

# Connect to the database



from airAQISpider.items import AiraqiItem
#insert to DB
class AiraqispiderPipeline(object):
    connection = pymysql.connect(**config)
    connection.autocommit(True)
    cursor = connection.cursor()
    def process_item(self, AiraqiItem, spider):
        print(AiraqiItem['城市']+"  "+ AiraqiItem['日期'])
        sql = "insert into tb_airAll values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql, [AiraqiItem['城市'], AiraqiItem['日期'], AiraqiItem['质量等级'], AiraqiItem['AQI'], AiraqiItem['AQI排名'], AiraqiItem['PM25'], AiraqiItem['PM10'], AiraqiItem['So2'], AiraqiItem['No2'], AiraqiItem['Co'], AiraqiItem['O3'] ] )
        except Exception as e:
            print(e)
        return AiraqiItem

    def __del__(self):
        print("我被析构啦")
        self.cursor.close()
        self.connection.close()
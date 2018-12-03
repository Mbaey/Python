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
    'db': 'db_emall',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
from TmallSpider.items import GoodsItem
class TmallspiderPipeline(object):
    connection = pymysql.connect(**config)
    connection.autocommit(True)
    cursor = connection.cursor()

    def process_item(self, goods, spider):
        #1.查询store
        # sql1= "select id from tb_store where name=%s"
        # self.cursor.execute(sql1, goods['store_name'])
        # goods['store_id'] = self.cursor.fetchone()
        # if(goods['store_id'] is None):
        #     self.cursor.execute("insert into tb_store (id, name) values (%s, %s)", [None,goods['store_name']])
        #     self.cursor.execute(sql1, goods['store_name'])
        #     goods['store_id'] = self.cursor.fetchone()
        #2.建造sales表？？？

        #3.插入goods
        sql3 = "insert into tb_goods_json values (%s)"
        try:
            self.cursor.execute(sql3, [goods['id']])
        except Exception as e:
            print(e)
        return goods


    def close_spider(self, spider):
        print("我被析构啦")
        self.cursor.close()
        self.connection.close()
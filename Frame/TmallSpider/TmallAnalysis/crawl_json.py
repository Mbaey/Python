import requests
import json
import pymysql
import re
from multiprocessing import Pool, cpu_count

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'db_emall',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
connection = pymysql.connect(**config)
connection.autocommit(True)
cursor = connection.cursor()

def run(sid):

    print(sid['id'])
    url = 'https://detail.m.tmall.com/item.htm?id=%s' % sid['id']

    failure = 0
    while failure < 10:
        try:
            r = requests.get(url, timeout=10)
            context = r.content.decode('gbk', 'ignore')
            # print(context)
            js = re.findall('_DATA_Detail = (.*?);</script>',context)
            print(js)
        except Exception as e:
            print(e)
            failure += 1
            continue

        try:
            cursor.execute('insert into tb_goods_json values (%s)', js)
        except Exception as e:
            print( e)
        break
    if failure >= 10:
        print ('Failed: %s' % sid)
        with open('failure.txt', 'a') as f:
            f.write('%s erroe\n' % sid)


if __name__ == '__main__':

    cursor.execute('select * from tb_goodsid')
    sids = cursor.fetchall()
    # print(sids)

    # for i in sids:
    #     print(i['id'])
    pool = Pool(cpu_count())
    pool.map(run, sids)
    pool.close()
    pool.join()


    cursor.close()
    connection.close()
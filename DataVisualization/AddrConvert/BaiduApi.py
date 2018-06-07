from urllib import request
from urllib import parse
import json
import time
import random
import pymysql
import pymysql.cursors
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'db_oj',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
if __name__ == "__main__":
    connection = pymysql.connect(**config)
    connection.autocommit(True)
    cursor = connection.cursor()
    # 访问网址
    cursor.execute("select _sid,name from PAT_schools")
    fetchall = cursor.fetchall()
    for all in fetchall:
        name = all['name']
        _sid = all['_sid']

        url = 'http://api.map.baidu.com/geocoder/v2/?address='+parse.quote(name)+'&output=json&ak=R5O1nVWz9FiqrZEPXedQZzGRu1DjnAre'
        print(url)
        try:
            response = request.urlopen(url, timeout=3)
            # 读取相应信息并解码
            html = response.read().decode("utf-8")
            # 打印信息
            result = json.loads(html)
            type(result) == type({})

            db = []
            # print(result)
            db.append(result['result']['location']['lng'])
            db.append(result['result']['location']['lat'])
            db.append(_sid)
            print(db)
            try:
                cursor.execute("update PAT_schools set lng=%s, lat=%s where _sid=%s; ", db)
            except Exception as e:
                print(e)

            time.sleep(random.random())
        except Exception as e:
            print(e)
    cursor.close()
    connection.close()




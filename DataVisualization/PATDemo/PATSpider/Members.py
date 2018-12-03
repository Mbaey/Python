from urllib import request
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
    #访问网址
    cursor.execute("select _tid from PAT_teams")
    fetchall = cursor.fetchall()
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    for _tid in fetchall:
        _tid = _tid['_tid']
        url = 'http://gplt.patest.cn/api/cached/board/team/'+_tid+'?timestamp=1523318564797'
        print(url)
        try:
            req = request.Request(url, headers=headers)

            #使用自己安装好的Opener
            response = request.urlopen(req, timeout=3)
            #读取相应信息并解码
            html = response.read().decode("utf-8")
            #打印信息
            result = json.loads(html)
            type(result) == type({})

            db = []
            # print(result['data']['data'])
            db.append(_tid)
            db.append(result['data']['data']['name'])
            db.append(result['data']['data']['schoolName'])
            for member in result['data']['data']['members']:
                # _tid,tname,sname,_id,name,L1-01,L1-02,L1-03,L1-04,L1-05,L1-06,L1-07,L1-08,
                # L2-01,L2-02,L2-03,L2-04,L3-01,L3-02,L3-03,tScore
                # print(schoolStr)
                dbtemp = []
                for item in db:
                    dbtemp.append(item)
                # print(member)
                type(member) == type({})

                dbtemp.insert(0, member['_id'])
                dbtemp.append(member['name'])
                print(member['name'])
                for level in member['v']['s']:
                    # print(level)
                    for score in level:
                        dbtemp.append(score)
                dbtemp.append(member['v']['tScore'])
                # print(dbtemp)
                # print(len(dbtemp))
                try:
                    cursor.execute(
                        "insert into PAT_members values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); ",
                        dbtemp)
                except Exception as e:
                    print(e)

            time.sleep(random.random())
        except Exception as e:
            print(e)
    cursor.close()
    connection.close()




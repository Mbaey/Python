from urllib import request
import json
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
    url = 'http://gplt.patest.cn/api/cached/board?timestamp=1523316646881'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    req = request.Request(url, headers=headers)

    #使用自己安装好的Opener
    response = request.urlopen(req)
    print(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    result = json.loads(html)
    type(result) == type({})
    # print(result['data']['rawData']['score']['schools'])
    for schoolStr in result['data']['rawData']['score']['schools']:
        db = []
        # _sid, name, s0, s1, s2, tScore
        # print(schoolStr)
        school = result['data']['rawData']['score']['schools'][schoolStr]
        print(school['name'])
        type(school) == type({})

        db.append(school['_id'])
        db.append(school['name'])
        db.append(school['s'][0])
        db.append(school['s'][1])
        db.append(school['s'][2])
        db.append(school['tScore'])
        cursor.execute("insert into PAT_schools (_sid,name,s0,s1,s2,tScore) values (%s, %s,%s, %s,%s, %s); ",
                       db)

    cursor.close()
    connection.close()




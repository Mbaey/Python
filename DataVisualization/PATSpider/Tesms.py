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
    for teamsStr in result['data']['rawData']['score']['teams']:
        db = []
        # _tid,_sid,name,s0,s1,s2,tPass,tScore
        # print(schoolStr)
        team = result['data']['rawData']['score']['teams'][teamsStr]
        print(team['name'])
        type(team) == type({})

        db.append(team['_id'])
        db.append(team['_sid'])
        db.append(team['name'])
        db.append(team['s'][0][0])
        db.append(team['s'][1][0])
        db.append(team['s'][2][0])
        db.append(team['tPass'])
        db.append(team['tScore'])
        # print(db)
        try:
            cursor.execute(
                "insert into PAT_teams (_tid,_sid,name,s0,s1,s2,tPass,tScore) values (%s, %s,%s, %s,%s, %s,%s, %s); ",
                db)
        except Exception as e:
            print(e)



    cursor.close()
    connection.close()




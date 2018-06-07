import time
import urllib.request
import urllib.response
from http import cookiejar
from bs4 import BeautifulSoup
import json
import pymysql
import pymysql.cursors
# config = {
#     'host': '115.28.231.119',
#     'port': 3306,
#     'user': 'xddev',
#     'password': 'xddev@xiaodou',
#     'db': 'db_weather',
#     'charset': 'utf8',
#     'cursorclass': pymysql.cursors.DictCursor,
# }
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'db_weather',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}


if __name__ == '__main__':
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = urllib.request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = urllib.request.build_opener(cookie_support)
    # 创建Request对象

    villages = [{"id": "101160101001", "name": "安宁堡街道"}, {"id": "101160101002", "name": "孔家崖街道"},
                {"id": "101160101003", "name": "刘家堡街道"}, {"id": "101160101004", "name": "培黎街道"},
                {"id": "101160101005", "name": "沙井驿街道"}, {"id": "101160101006", "name": "十里店街道"},
                {"id": "101160101007", "name": "西路街道"}, {"id": "101160101008", "name": "银滩路街道"},
                {"id": "101160101009", "name": "白银路街道"}, {"id": "101160101010", "name": "草场街街道"},
                {"id": "101160101011", "name": "东岗街道"}, {"id": "101160101012", "name": "东岗西路街道"},
                {"id": "101160101013", "name": "伏龙坪街道"}, {"id": "101160101014", "name": "皋兰路街道"},
                {"id": "101160101015", "name": "高新区"}, {"id": "101160101016", "name": "拱星墩街道"},
                {"id": "101160101017", "name": "广武门街道"}, {"id": "101160101018", "name": "火车站街道"},
                {"id": "101160101019", "name": "嘉峪关路街道"}, {"id": "101160101020", "name": "焦家湾街道"},
                {"id": "101160101021", "name": "靖远路街道"}, {"id": "101160101022", "name": "酒泉路街道"},
                {"id": "101160101023", "name": "临夏路街道"}, {"id": "101160101024", "name": "青白石街道"},
                {"id": "101160101025", "name": "铁路东村街道"}, {"id": "101160101026", "name": "铁路西村街道"},
                {"id": "101160101027", "name": "团结新村街道"}, {"id": "101160101028", "name": "渭源路街道"},
                {"id": "101160101029", "name": "五泉街道"}, {"id": "101160101030", "name": "盐场路街道"},
                {"id": "101160101031", "name": "雁北街道"}, {"id": "101160101032", "name": "雁南街道"},
                {"id": "101160101033", "name": "张掖路街道"}, {"id": "101160101035", "name": "红古乡"},
                {"id": "101160101036", "name": "花庄镇"}, {"id": "101160101037", "name": "矿区街道"},
                {"id": "101160101038", "name": "平安镇"}, {"id": "101160101039", "name": "下窑街道"},
                {"id": "101160101040", "name": "窑街街道"}, {"id": "101160101041", "name": "阿干镇"},
                {"id": "101160101042", "name": "八里镇"}, {"id": "101160101043", "name": "敦煌路街道"},
                {"id": "101160101044", "name": "龚家湾街道"}, {"id": "101160101045", "name": "黄峪乡"},
                {"id": "101160101046", "name": "建兰路街道"}, {"id": "101160101047", "name": "彭家坪镇"},
                {"id": "101160101048", "name": "土门墩街道"}, {"id": "101160101049", "name": "魏岭乡"},
                {"id": "101160101051", "name": "西湖街道"}, {"id": "101160101052", "name": "西园街道"},
                {"id": "101160101053", "name": "西站街道"}, {"id": "101160101054", "name": "秀川街道"},
                {"id": "101160101055", "name": "晏家坪街道"}, {"id": "101160101056", "name": "陈坪街道"},
                {"id": "101160101057", "name": "达川乡"}, {"id": "101160101058", "name": "东川镇"},
                {"id": "101160101059", "name": "福利路街道"}, {"id": "101160101060", "name": "河口乡"},
                {"id": "101160101061", "name": "金沟乡"}, {"id": "101160101062", "name": "临洮街街道"},
                {"id": "101160101063", "name": "柳泉乡"}, {"id": "101160101064", "name": "四季青街道"},
                {"id": "101160101065", "name": "西固城街道"}, {"id": "101160101066", "name": "西柳沟街道"},
                {"id": "101160101067", "name": "先锋路街道"}, {"id": "101160101068", "name": "新安路街道"},
                {"id": "101160101069", "name": "新城镇"}, {"id": "101160101070", "name": "新和路街道"},
                {"id": "101160101034", "name": "海石湾镇"}, {"id": "101160101050", "name": "西果园镇"}]
    while 1:
        connection = pymysql.connect(**config)
        connection.autocommit(True)
        cursor = connection.cursor()
        for id in villages:
            url= 'http://forecast.weather.com.cn/town/weather1dn/'+id['id']+'.shtml'
            data = []
            data.append(id['id'])
            he = {'Host':'forecast.weather.com.cn',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
            request = urllib.request.Request(url)
            try:
                response = opener.open(request)

            # print(html.decode('utf-8',errors='ignore'))
                html = response.read()
                soup = BeautifulSoup(html, 'lxml')

                info = soup.select('div.todayLeft')[0]
                lifeHelper = soup.select('div.lv')[0]
                # print(lifeHelper)
                suggest = lifeHelper.find_all('dd')
                suggest2 = lifeHelper.find_all('em')
                # print(info)
                timeStr = time.strftime("%Y-%m-%d ", time.localtime())
                timeStr2 = info.select('div.topBar')[0].get_text().strip()[:5]
                timeStr = timeStr + timeStr2 + ":00"

                data.append(timeStr)

                dis = soup.find_all(attrs={"class": "weather dis"})[0].get_text()
                data.append(dis)
                temp = info.select('span.temp')[0].get_text()
                data.append(temp)
                maxtemp = info.select('div#maxTempDiv')[0].get_text()
                data.append(maxtemp)
                mintemp = info.select('div#minTempDiv')[0].get_text()
                data.append(mintemp)
                lastFour = info.select('p')#.get_text().split('\n')
                wind = lastFour[0].get_text().split(' ')
                data.append(wind[0])
                data.append(wind[1])
                data.append(lastFour[1].get_text()[5:])
                data.append(lastFour[2].get_text()[2:])
                for s in suggest:
                    data.append(s.get_text())
                for s in suggest2:
                    data.append(s.get_text())
                # print(data)
                try:
                    cursor.execute("insert into weather_history_hour (id,CollectTime,weatherDis,temp,tempMax,tempMin,windDir,windForce,湿度,限行,紫外线,感冒,穿衣,洗车,运动,空气污染扩散,紫外线指数,感冒指数,穿衣指数,洗车指数,运动指数,空气污染指数) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
                except Exception as e:
                    print(e)
                print("success: " + id['name'])
            except Exception as e:
                print(e)
        time.sleep(3600)
        cursor.close()
        connection.close()

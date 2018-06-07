import time
import urllib.request
import urllib.response
import requests
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

connection = pymysql.connect(**config)
connection.autocommit(True)
cursor = connection.cursor()

key="9951f4f728a44e723ce5ecb8a67adf6b"
#!/usr/bin/python
import sys
if __name__  == "__main__":
    if(len(sys.argv) == 2 ):
        print("hello： "+ sys.argv[1])
        key = sys.argv[1]
    i=1
    print(key)
    cursor.execute("select STATIONID,STATIONNAME from site_name")
    fetchall = cursor.fetchall()
    for data in fetchall:
        print(data['STATIONID'])
        url = 'http://43.254.1.229:8021/ServiceHandler.ashx?Type=GetStationHourDataByID&stationid='+str(data['STATIONID'])+'&key='+key
        result2 = requests.get(url).json()
        for messageDay in result2['datalist']:
            try:
                cursor.execute("insert into history_hour (stationid,CollectTime, SO2_V, NO2_V, CO_V, O3_V, PM10_V, PM25_V, AQI, primePollute) values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",[ data['STATIONID'], messageDay['COLLECTTIME'], messageDay['SO2_V'], messageDay['NO2_V'], messageDay['CO_V'], messageDay['O3_V'], messageDay['PM10_V'], messageDay['PM25_V'], messageDay['AQI'], messageDay['PRIPOLLUTE']])
            except Exception as e:
                print(e)
        url = 'http://43.254.1.229:8021/ServiceHandler.ashx?Type=GetStationDayDataByID&stationid=' + str(data['STATIONID']) + '&key=' + key
        result2 = requests.get(url).json()
        for messageDay in result2['datalist']:
            try:
                cursor.execute("insert into history_day (stationid,CollectTime, SO2_V, NO2_V, CO_V, O3_V, PM10_V, PM25_V, AQI) values (%s, %s,%s, %s,%s, %s,%s, %s,%s)",[ data['STATIONID'], messageDay['CollectTime'], messageDay['SO2_V'], messageDay['NO2_V'], messageDay['CO_V'], messageDay['O3_V'], messageDay['PM10_V'], messageDay['PM25_V'], messageDay['AQI']])
            except Exception as e:
                print(e)

        print(str(i) + " insert succsee： "+data['STATIONNAME'])
        i=i+1
        time.sleep(1)
    cursor.close()
    connection.close()

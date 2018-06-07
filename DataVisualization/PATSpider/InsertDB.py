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

connection = pymysql.connect(**config)
connection.autocommit(True)
cursor = connection.cursor()

cursor.execute("update PAT_schools set lng=%s, lat=%s where _sid=%s; ", ['2','3.2', '571229d1f7f0c5a215de7af9'])

cursor.close()
connection.close()

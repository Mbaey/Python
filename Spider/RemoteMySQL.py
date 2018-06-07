import pymysql
import pymysql.cursors
config = {
    'host': '202.201.60.128',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'db_spj',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

connection = pymysql.connect(**config)
connection.autocommit(True)
cursor = connection.cursor()
cursor.execute("select * from spj")

for r in cursor.fetchall():
    print(r)
cursor.close()
connection.close()

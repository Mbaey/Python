import pymysql
import pymysql.cursors

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'douban',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

# Connect to the database

connection = pymysql.connect(**config)
connection.autocommit(True)
cursor = connection.cursor()

fr = open(r'data/douban_movie_clean.txt', 'br')
# Create
# count = 0
# for line in fr:
#     count += 1
#     print(count)
#     if(count == 1):
#         continue
#
#     line = line.decode('utf-8').strip().split('^')
#     cursor.execute("insert into movie (title, url, summary, score) values ( %s, %s, %s, %s)", [line[1], line[2], line[-1], line[4]])

# Update
# cursor.execute("update movie set title=%s where id=1", ['Mbaey'])

# Read1
# cursor.execute("select * from movie")
# movies = cursor.fetchall()
# print(len(movies))
# print(movies[0])
# Read2
# cursor.execute("select title, score from movie")
# movies = cursor.fetchone()
# print(movies)

# Delete
# cursor.execute("delete from movie where id=2")


fr.close()

cursor.close()
connection.close()

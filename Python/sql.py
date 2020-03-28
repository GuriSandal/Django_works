import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='python'
)

print(db)
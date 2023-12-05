import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost',user='root',passwd='',db='world',charset='utf8')
cur = conn.cursor()

# #crate table
# qr = """CREATE TABLE stu (
#     uid int PRIMARY KEY AUTO_INCREMENT,
#     nick varchar(20) not null,
#     pwd varchar(20) not null,
#     phone varchar(20) not null,
#     addr varchar(20) not null
# )
# """
#cur.execute(qr)

#sql = "INSERT INTO stu VALUES(0,'goo','goopawd','010','cat city');"
#sql = "INSERT INTO stu VALUES(1,'goo','goopawd','010','cat city');"
#cur.execute(sql)
conn.commit()

sql = "SELECT * FROM stu"

cur.execute(sql)
data = cur.fetchall()
#print(data)

_data = pd.DataFrame(data)
#print(_data)

sql = "select * from country limit 10"
cur.execute(sql)
data = cur.fetchall()
cols = [desc[0] for desc in cur.description]
data = pd.DataFrame(data,columns=cols)

print(data)

sql = "select * from city"
cur.execute(sql)
data = cur.fetchall()
cols = [desc[0] for desc in cur.description]
data = pd.DataFrame(data,columns=cols)
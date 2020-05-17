import MySQLdb
ip = '18.191.216.222'
user = 'admin'
password = 'abc@123'
db_name = 'db_thuy'
conn = MySQLdb.connect(ip, user, password, db_name, charset='utf8')
print("Connected successfully!")
keyword = "ABC' OR 1=1 OR 1=1'"
# sql = f"select * from student where name like '%{keyword}%'"
sql = "select * from student where name like %s"
print('sql=', sql)
cursor = conn.cursor()
cursor.execute(sql, [keyword])
result = cursor.fetchall()
print(result)
for st in result: print(st)

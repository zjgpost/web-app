#导入MySQL驱动:
import mysql.connector
import pymysql

conn = mysql.connector.connect(user='root',password='root',database='mytestdb')
cursor = conn.cursor()

#运行查询:
cursor.execute('select * from alluser where id = %s',('1',))
values = cursor.fetchall()
print(values)

try:
    conn1 = pymysql.connect('127.0.0.1','root','root','mytestdb',use_unicode=True, charset="utf8")
    cursor = conn1.cursor()
    #namestr = '王波'
    #username =namestr.encode("utf-8").decode("latin1")
    insert_sql = "insert into alluser(name,age) values('王小波',18)"
    line = cursor.execute(insert_sql)
    print(line)
finally:
    if conn1:
        conn1.close()
import pymysql
import datetime

database=pymysql.connect('localhost','root','123456','sunck')
cursor=database.cursor()

# 在表中插入数据,插入字符串时，sql语句要用三双引号括起来"""""",内部字符串用双引号括起来即可
now_address=str(input("请输入文件地址："))
gl=str(input("请输入隔离开关编号："))
xiang=str(input("请输入相："))
xiang_number=str(input("请输入第几支绝缘子："))
gr=gl+xiang+xiang_number

sql="""select  count(*) from rew_insulator_record;"""
try:
    cursor.execute (sql)
    row_number = cursor.fetchall()
    row_number=row_number[0][0]+1
    print ('Successful1')
    database.commit()  # 增删改查时必须db.commit一下
except:
    # 如果提交失败，回滚到上一次数据
    print ('Failed1')
    database.rollback()

sql="""select  count(number) from rew_insulator_record where number="%s";""" % gr
try:
    cursor.execute (sql)
    now_test_number = cursor.fetchall()
    now_test_number=now_test_number[0][0]+1
    print ('Successful2')
    database.commit()  # 增删改查时必须db.commit一下
except:
    # 如果提交失败，回滚到上一次数据
    print ('Failed2')
    database.rollback()

now_time=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')

data={"id":"0",
      "time":now_time,
      "sum_number":row_number,
      "number":gr,
      "test_number":now_test_number,
      "address":now_address,
      "remarks":"母线侧"}
table="rew_insulator_record"
keys=", ".join(data.keys())
values= ", ".join(["%s"] * len(data))
sql="""insert into {table}({keys}) values ({values})""".format(table=table, keys=keys, values=values)

try:
    cursor.execute (sql, tuple(data.values()))
    print ('Successful3')
    database.commit()  # 增删改查时必须db.commit一下
except:
    # 如果提交失败，回滚到上一次数据
    print ('Failed3')
    database.rollback()

cursor.close()
database.close()


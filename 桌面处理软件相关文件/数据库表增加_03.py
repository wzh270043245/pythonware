import pymysql
import datetime

database=pymysql.connect('localhost','root','123456','sunck')
cursor=database.cursor()

# 在表中插入数据,插入字符串时，sql语句要用三双引号括起来"""""",内部字符串用双引号括起来即可
sql="""select  count(*) from insulator_record;"""
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

now_time=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
address=str(input("请输入地址："))
rank=str(input("请输入电压等级："))
data={"id":"0",
      "time":now_time,
      "address":address,
      "rank":rank,
      "number":row_number,
      "result":"0",
      "isDelete":0,
      "judge":"0"}
table="insulator_record"
keys=", ".join(data.keys())
values= ", ".join(["%s"] * len(data))
sql="""insert into {table}({keys}) values ({values})""".format(table=table, keys=keys, values=values)

try:
    cursor.execute (sql, tuple(data.values()))
    print ('Successful2')
    database.commit()  # 增删改查时必须db.commit一下
except:
    # 如果提交失败，回滚到上一次数据
    print ('Failed2')
    database.rollback()

sql="""select result from insulator_record where number=%s;""" % row_number   #一律用%s，无论传入什么类型的变量
try:
    cursor.execute(sql)
    result=cursor.fetchall()
    result=result[0][0]   # 经过select查询的数据均为元组的形式，需要提取才可使用
    print ('Successful3')
except:
    database.rollback()
    print ('Failed3')

sql="""select judge from insulator_record where number=%s;""" % row_number
try:
    cursor.execute (sql)
    judge=cursor.fetchall()
    judge=judge[0][0]   # 经过select查询的数据均为元组的形式，需要提取才可使用
    print ('Successful4')
except:
    database.rollback()
    print ('Failed4')

cursor.close()
database.close()

if judge==0:
    print("编号为%s-%s-%d-%02d的瓷支柱绝缘子，峰值频率为%dHz，经寻峰算法智能判断为：正常绝缘子" % (now_time,address,rank,row_number,result))
else:
    print("编号为%s-%s-%d-%02d的瓷支柱绝缘子，峰值频率为%dHz，经寻峰算法智能判断为：故障绝缘子" % (now_time,address,rank,row_number,result))

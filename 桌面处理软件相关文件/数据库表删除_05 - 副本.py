import pymysql

database=pymysql.connect('localhost','root','123456','sunck')
cursor=database.cursor()

sql="""select  count(*) from rew_insulator_record;"""
try:
    cursor.execute (sql)
    row_number = cursor.fetchall()
    row_number=row_number[0][0]
    print ('Successful1')
    database.commit()  # 增删改查时必须db.commit一下
except:
    # 如果提交失败，回滚到上一次数据
    print ('Failed1')
    database.rollback()

de_sum_number=int(input("请输入要删除的序号："))
# 在表中插入数据,插入字符串时，sql语句要用三双引号括起来"""""",内部字符串用双引号括起来即可
sql="""delete from rew_insulator_record where sum_number="%s";""" % de_sum_number

try:
    cursor.execute (sql)
    database.commit()  # 增删改查时必须db.commit一下
    print ('Successful2')
except:
    # 如果提交失败，回滚到上一次数据
    print ('Failed2')
    database.rollback()

cursor.close()
database.close()
import pymysql

database=pymysql.connect('localhost','root','123456','sunck')
cursor=database.cursor()

# 重命名number
gl=str(input("请输入原始隔离开关编号："))
xiang=str(input("请输入原始相："))
xiang_number=str(input("请输入原始第几支绝缘子："))
gr=gl+xiang+xiang_number
old_test_number=str(input("请输入原始检测次数："))
new_gl=str(input("请输入新隔离开关编号："))
new_xiang=str(input("请输入新相："))
new_xiang_number=str(input("请新输入第几支绝缘子："))
new_gr=new_gl+new_xiang+new_xiang_number

sql="""update rew_insulator_record set number="%s"  where number="%s" and test_number="%s";"""  % (new_gr,gr,old_test_number)
try:
    cursor.execute (sql)
    database.commit()  # 增删改查时必须db.commit一下
except:
    # 如果提交失败，回滚到上一次数据
    database.rollback()

cursor.close()
database.close()

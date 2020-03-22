"""
fetchone()
    功能：获取下一个查询结果，结果是一个对象
    
fetchall()
    功能：接受全部返回的行
    
rowcount()  是一个只读属性，返回execute()方法影响的行数

"""
import pymysql

database=pymysql.connect('localhost','root','123456','sunck')
cursor=database.cursor()

sql="""select time,address,rank,number,result,judge,remarks from insulator_record where address="丽江" and rank=32 and number=5;"""
try:
    cursor.execute (sql)
    recall=cursor.fetchall()
    print ("成功")
    for row in recall:
        print("%s,%s,%s,%d,%d,%d,%s" % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
except:
    print("失败")
    database.rollback()

cursor.close()
database.close()
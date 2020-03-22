import pymysql

database=pymysql.connect('localhost','root','123456','sunck')
cursor=database.cursor()

# 建立表之前，应该先检查所建立的表是否存在，若存在则删除后再新建表
cursor.execute('drop table if EXISTS new_insulator_record')

# 建表语句
sql="""create table new_insulator_record (id int auto_increment primary key ,time varchar(20) default "",number varchar(20) default 0,sum_number int default 0,number1 varchar(20) default 0,number2 varchar(20) default 0,number3 varchar(20) default 0,test_number int default 0,address varchar(255) default "",remark1 varchar(255) default "",remark2 varchar(255) default "",remark3 varchar(255) default "");"""
cursor.execute(sql)

cursor.close()
database.close()

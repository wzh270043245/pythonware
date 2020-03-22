import pymysql

# 连接数据库  pymysql.connect('','','','')
#db作为mysql连接到python中的操作对象
#参数1：''内输入mysql服务所在的主机IP，利用cmd->ipconfig查看本机ipv4地址
#参数2：''内输入用户名
#参数3：''内输入密码
#参数4：''内输入要连接的数据库名字，而不是图像化操作界面中连接的名字
# database=pymysql.connect('localhost','root','123456','sunck')
database=pymysql.connect('192.168.3.6','root','123456','sunck')

# 创建一个cursor对象,类似于操作对象。(光标)这是一个数据库在python中的操作对象
cursor=database.cursor()

#查看当前mysql数据库版本的语句,cursor.execute用来类似于在cmd中执行sql语句
see_version='select version()'
cursor.execute(see_version)
#用cursor.fetchone（）来获取查看数据库版本的信息
data_see_version=cursor.fetchone()
print(data_see_version)

#查看完成后要断开数据库
cursor.close()
database.close()


print(pymysql)
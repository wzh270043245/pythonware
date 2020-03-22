from python_mysql_together import SunckSql

s=SunckSql('192.168.3.6','root','123456','sunck')
# 增
# s.Sql_insert(s.sql_in("1222","B","1","C:\\Users\\wzh\\Desktop\\000001.Wav","母线")[0],s.sql_in("1222","B","1","C:\\Users\\wzh\\Desktop\\000001.Wav","母线")[1])

# 删除
# s.Sql_delete(3)

# 改
"""
gl=str(input("请输入原始隔离开关编号："))   参数说明文档
xiang=str(input("请输入原始相："))    
xiang_number=str(input("请输入原始第几支绝缘子："))
gr=gl+xiang+xiang_number
old_test_number=str(input("请输入原始检测次数："))
new_gl=str(input("请输入新隔离开关编号："))
new_xiang=str(input("请输入新相："))
new_xiang_number=str(input("请新输入第几支绝缘子："))
new_gr=new_gl+new_xiang+new_xiang_number
"""
# s.Sql_update("1222","B","1","1","1225","B","1")


# 查
a=s.Sql_getall(s.sql_getthree("1222","B","1"))
if a==():
    print("无记录！")
else:
    print(a)


# 全部输出
# result=s.Sql_all()
# print(len(result))   #行数
# for i in result:
#     print(i[0],end="")
#     print(i[1],end="")
#     print(i[2],end="")
#     print(i[3],end="")
#     print(i[4],end="")
#     print(i[5],end="")
#     print("\n")


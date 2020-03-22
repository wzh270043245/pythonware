import pymysql
import datetime

class SunckSql():
    def __init__(self,host,user,passwd,dbName):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.dbName=dbName

    def SqlConnet(self):
        self.db=pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor=self.db.cursor()

    def SqlClose(self):
        self.cursor.close()
        self.db.close()

    def Sql_getone(self,sql):
        res=None
        try:
            self.SqlConnet()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
            self.SqlClose()
        except:
            print("查询失败！")
        return res

    def sql_get(self,gl , xiang ,xiang_number):
        gr = gl + xiang + xiang_number
        sql="""select number,test_number,address from rew_insulator_record where number="%s" ;""" % gr
        return sql

    def Sql_getall(self,sql):
        try:
            self.SqlConnet ()
            self.cursor.execute (sql)
            recall = self.cursor.fetchall ()
            self.SqlClose ()
            return recall  # 返回的res为元组
        except:
            print ("查询失败！")


    def sql_in(self,gl,xiang,xiang_number,now_address,now_remarks):   #后期寻峰以及寻峰判断算法写完后，直接在末尾加上两个形参即可，对应的data中的形参要做相应改变
        gr = gl + xiang + xiang_number
        now_time = datetime.datetime.now ().strftime ('%Y-%m-%d-%H:%M')
        # try:
        #     sql="""select  max(test_number) from rew_insulator_record where number="%s";""" % gr
        sql1 = """select  max(test_number) from rew_insulator_record where number="%s";""" % gr  # 计算test_number已有数量
        try:
            self.SqlConnet ()
            self.cursor.execute (sql1)
            now_test_number = self.cursor.fetchall ()
            if now_test_number[0][0]==None:
                now_test_number=((1,0),)
                now_test_number=now_test_number[0][0]
            else:
                now_test_number = now_test_number[0][0] + 1

            print ('Successful1')
            self.db.commit ()
            self.SqlClose ()
        except:
            # 如果提交失败，回滚到上一次数据
            print ('Failed1')
            self.db.rollback ()

        sql2 = """select  count(*) from rew_insulator_record;"""   # 计算sum_number总数
        try:
            self.SqlConnet ()
            self.cursor.execute (sql2)
            now_sum_number = self.cursor.fetchall ()
            now_sum_number = now_sum_number[0][0] + 1
            print ('Successful2')
            self.db.commit ()
            self.SqlClose ()
        except:
            print ('Failed2')
            self.db.rollback ()

        data = {"id": "0",
                "time": now_time,
                "sum_number": now_sum_number,
                "number":gr,
                "address": now_address,
                "test_number": now_test_number,
                "remarks":now_remarks}
        table = "rew_insulator_record"
        keys = ", ".join (data.keys ())
        values = ", ".join (["%s"] * len (data))
        sql3 = """insert into {table}({keys}) values ({values})""".format (table=table, keys=keys, values=values)
        a=tuple(data.values())
        return sql3,a

    def Sql_insert(self,sql,a):
        return self.__edit_insert(sql,a)

    def Sql_update(self,gl,xiang,xiang_number,old_test_number,new_gl,new_xiang,new_xiang_number):
        gr = gl + xiang + xiang_number
        new_gr = new_gl + new_xiang + new_xiang_number
        sql1 = """select  max(test_number) from rew_insulator_record where number="%s";""" % new_gr  # 计算test_number已有数量
        try:
            self.SqlConnet ()
            self.cursor.execute (sql1)
            new_test_number = self.cursor.fetchall ()
            if new_test_number[0][0] == None:
                new_test_number = ((1, 0),)
                new_test_number = new_test_number[0][0]
            else:
                new_test_number = new_test_number[0][0] + 1

            print ('Successful1')
            self.db.commit ()
            self.SqlClose ()
        except:
            # 如果提交失败，回滚到上一次数据
            print ('Failed1')
            self.db.rollback ()
        sql3 = """update rew_insulator_record set number="%s",test_number="%s"   where number="%s" and test_number="%s";""" % (new_gr, new_test_number,gr, old_test_number)
        # sql2 = """update rew_insulator_record set test_number="%s"  where number="%s" and test_number="%s";""" % (new_test_number, gr, old_test_number)

        return self.__edit (sql3)

    def Sql_delete(self,de_sum_number):
        sql="""delete from rew_insulator_record where sum_number="%s";""" % de_sum_number
        return self.__edit_de (sql)

    def __edit_insert(self,sql,a):
        count=0
        try:
            self.SqlConnet()
            count=self.cursor.execute(sql,a)
            self.db.commit()
            self.SqlClose()
            print("Successful2")
        except:
            print("事件提交失败22！")
            self.db.rollback()
        return count

    def __edit_de(self,sql):
        count=0
        try:
            self.SqlConnet()
            count=self.cursor.execute(sql)
            self.db.commit ()
            try:
                re_number =self.cursor.execute("select  sum_number from rew_insulator_record;")
                re_number = self.cursor.fetchall ()
            except:
                print ("事件提交失败2.1！")
                self.db.rollback ()
            for row1 in range (len (re_number)):
                try:
                    sql1 = """update rew_insulator_record set sum_number=%s  where sum_number=%s;""" % (row1+1, re_number[row1][0])
                    self.cursor.execute (sql1)
                    self.db.commit ()
                except:
                    print("事件提交失败2.1.1！")
                    self.db.rollback ()
            self.SqlClose()
            print("Successful2")
        except:
            print("事件提交失败2！")
            self.db.rollback()
        return count

    def __edit_up(self,sql):
        try:
            # self.SqlConnet ()
            # self.cursor.execute (sql2)
            # self.db.commit ()
            self.cursor.execute (sql)
            self.db.commit ()
            self.SqlClose ()
            print ("Successful211")
        except:
            print("事件提交失败211！")
            self.db.rollback()


    def __edit(self,sql):
        count=0
        try:
            self.SqlConnet()
            count=self.cursor.execute(sql)
            self.db.commit()
            self.SqlClose()
            print("Successful2")
        except:
            print("事件提交失败2！")
            self.db.rollback()
        return count

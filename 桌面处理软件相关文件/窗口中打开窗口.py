from PyQt5.Qt import *
from PyQt5.QtCore import pyqtSignal
from 窗口中打开窗口测试 import Ui_Form1
# from save import Ui_Form3
from savetest import Window3
from python_mysql_together import SunckSql
import pymysql
import datetime
class Window1(QWidget,Ui_Form1):
    Singal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button2=QPushButton(self)
        self.button2.move(200,200)
        self.button2.clicked.connect(self.progress2)
        self.w2= Window2()
        self.address = "C:\\Users\\wzh\\Desktop\\000001.Wav"
        self.Singal.connect (self.recv2)  # 父窗体向子窗体传数据的“信号与槽连接”

    def progress1(self):  # 发送
        # address = "C"
        self.w2.show ()
        self.Singal.emit (self.address)

    def progress2(self):
        self.w2.show ()

    def recv2(self,s):
        print(type(s))
        try:
            self.w2.label100.setText(s)
            print ("success")
        except:
            print("fail")
        pass




# class Window2(QWidget,Ui_Form3):
#     # singal=QtCore.pyqtSingal(str)
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.setWindowFlags (Qt.WindowStaysOnTopHint)
#         self.setWindowFlags (Qt.WindowCloseButtonHint)
#         self.rb1.setShortcut ("Ctrl+A")
#         self.rb1.setChecked (True)
#         self.rb2.setShortcut ("Ctrl+B")
#         self.rb3.setShortcut ("Ctrl+C")
#         # self.setSizeGripEnabled(False)
#         self.setFixedSize(280, 235)
#         self.address2 = ""
#
#     def  progress1(self):
#         self.address2 = ""
#         rb1_ischecked = self.rb1.isChecked ()
#         rb2_ischecked = self.rb2.isChecked ()
#         rb3_ischecked = self.rb3.isChecked ()
#         if rb1_ischecked == True:
#             rb_text = "A"
#         elif rb2_ischecked == True:
#             rb_text = "B"
#         elif rb3_ischecked == True:
#             rb_text = "C"
#         access = SunckSql ('192.168.3.6', 'root', '123456', 'sunck')
#         a, b = access.sql_in (self.line1.text (), rb_text, self.combobox1.currentText(),
#                               self.address2, self.line2.text (), "3700", self.line3.text ())
#         access.Sql_insert (a, b)
#         self.close()
#         pass
#
#     def progress2(self):
#         self.close ()
#         pass



#
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window1()
    window.show()
    sys.exit(app.exec_())

from PyQt5.Qt import *
from  save import Ui_Form3
from python_mysql_together import SunckSql
import pymysql
import datetime
from PyQt5.QtCore import pyqtSignal

class Window3(QWidget,Ui_Form3):
    childclicked = pyqtSignal (str,int)
    def __init__(self):
        super( ).__init__()
        self.setupUi(self)
        self.setWindowFlags (Qt.WindowStaysOnTopHint|Qt.WindowCloseButtonHint)
        self.setWindowIcon (QIcon ("xy.ico"))
        self.rb1.setShortcut ("Ctrl+A")
        self.rb1.setChecked (True)
        self.rb2.setShortcut ("Ctrl+B")
        self.rb3.setShortcut ("Ctrl+C")
        # self.setSizeGripEnabled(False)
        self.setFixedSize(280, 235)
        self.label20.setVisible(False)
        self.label21.setVisible (False)
        self.savenumber = 0

    def keyPressEvent(self, event):
        if event.key () == Qt.Key_Enter:
            self.progress1()
        if event.key () == Qt.Key_Escape:
            self.progress2()


    def  progress1(self):
        a = 0
        self.obj1 = QObject()
        if self.line1.text () != "":  # 防止保存空数据
            a += 1
            rb1_ischecked = self.rb1.isChecked ()
            rb2_ischecked = self.rb2.isChecked ()
            rb3_ischecked = self.rb3.isChecked ()
            if rb1_ischecked == True:
                rb_text = "A"
            elif rb2_ischecked == True:
                rb_text = "B"
            elif rb3_ischecked == True:
                rb_text = "C"
            access = SunckSql ('localhost', 'root', '123456', 'sunck')
            a, b = access.sql_in (self.line1.text (), rb_text, self.combobox1.currentText(),
                                  self.label20.text (), self.line2.text (), self.label21.text (), self.line3.text ())
            access.Sql_insert (a, b)
            self.savenumber +=1
            self.obj1.objectNameChanged.connect (self.childsend)
            self.obj1.setObjectName (str(a))

            self.close ()
            pass

    def childsend(self):
        childstr = "1"
        self.childclicked.emit (childstr,self.savenumber)

    def progress2(self):
        self.close ()
        pass



# if __name__ == '__main__':
#     import sys
#     app=QApplication(sys.argv)
#     window=Window3()
#     window.show()
#     sys.exit(app.exec_())

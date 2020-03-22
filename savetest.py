from PyQt5.Qt import *
from  save import Ui_Form3
from python_mysql_together import SunckSql
import pymysql
import datetime
from PyQt5.QtCore import pyqtSignal


class Window3(QWidget,Ui_Form3):
    def __init__(self):
        super( ).__init__()
        self.setupUi(self)
        self.setWindowFlags (Qt.WindowStaysOnTopHint|Qt.WindowCloseButtonHint)
        self.rb1.setShortcut ("Ctrl+A")
        self.rb1.setChecked (True)
        self.rb2.setShortcut ("Ctrl+B")
        self.rb3.setShortcut ("Ctrl+C")
        # self.setSizeGripEnabled(False)
        self.setFixedSize(280, 235)
        self.label20.setVisible(False)
        self.label21.setVisible (False)

    def  progress1(self):
        rb1_ischecked = self.rb1.isChecked ()
        rb2_ischecked = self.rb2.isChecked ()
        rb3_ischecked = self.rb3.isChecked ()
        if rb1_ischecked == True:
            rb_text = "A"
        elif rb2_ischecked == True:
            rb_text = "B"
        elif rb3_ischecked == True:
            rb_text = "C"
        access = SunckSql ('192.168.3.6', 'root', '123456', 'sunck')
        a, b = access.sql_in (self.line1.text (), rb_text, self.combobox1.currentText(),
                              self.label20.text (), self.line2.text (), self.label21.text (), self.line3.text ())
        access.Sql_insert (a, b)
        self.close ()
        pass

    def progress2(self):
        self.close ()
        pass



# if __name__ == '__main__':
#     import sys
#     app=QApplication(sys.argv)
#     window=Window3()
#     window.show()
#     sys.exit(app.exec_())

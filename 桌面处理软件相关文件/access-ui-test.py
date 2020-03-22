from PyQt5.Qt import *
import time
from access import Ui_Form
class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags (Qt.WindowStaysOnTopHint)
        self.setWindowFlags (Qt.WindowCloseButtonHint)
        self.line2.setEchoMode(QLineEdit.Password)
        self.label3.setVisible(False)

    def progress1 (self):
        zhanghao = "123456"
        password = "654321"
        self.zhanghao = self.line1.text ()
        self.password = self.line2.text ()
        print (self.zhanghao)
        print (self.password)
        if self.zhanghao == zhanghao  and self.password == password:
            self.label3.setVisible (False)
            self.label3.setText ("登录成功！")
            self.label3.setAlignment (Qt.AlignCenter)
            self.label3.setVisible (True)
            time.sleep(1)
            pass
        elif self.zhanghao == zhanghao and self.password != password:
            self.label3.setText("密码错误！请重新输入...")
            self.label3.setAlignment (Qt.AlignCenter)
            self.label3.setVisible (True)
            pass
        elif self.zhanghao != zhanghao and self.password != password:
            self.label3.setText ("账号以及密码错误！请重新输入...")
            self.label3.setAlignment (Qt.AlignCenter)
            self.label3.setVisible (True)
            pass
        pass

    def progress2 (self):
        self.close()
        pass







if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

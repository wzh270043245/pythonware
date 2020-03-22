from PyQt5.Qt import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):

        #创建窗口的状态栏
        self.statusBar()
        self.setStatusTip("这是状态栏的提示信息")
        print (self.statusTip ())  #获取当前窗口状态栏字符串

        #在状态栏上显示控件提示信息
        self.button1=QPushButton(self)
        self.button1.move(50,50)
        self.button1.setText("button1")
        self.button1.setStatusTip("这是按钮")

        #在控件上显示工具的提示信息
        self.button1.setToolTip("这是控件的工具提示信息")
        self.button1.setToolTipDuration(1000) #还可以设置提示时间，ms单位
        print(self.button1.toolTip())





if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
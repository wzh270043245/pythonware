from PyQt5.Qt import *
from test4 import Ui_Form
class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setupUi(self)


    def ccc (self):
        pass



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject继承结构测试()
        self.QObject对象名称和属性的操作 ()

    def QObject继承结构测试(self):
        mros=QObject.mro()
        for mro in mros:
            print(mro)

    def QObject对象名称和属性的操作(self):
        #测试API
        obj = QObject()
        obj.setObjectName ("notice")
        print (obj.objectName ())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
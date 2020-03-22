from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        inputdialog = QInputDialog(self)
        # print(inputdialog.width(),inputdialog.height())
        inputdialog.setFixedSize(100,150)
        inputdialog.resize(100,100)
        button1=QPushButton(inputdialog)
        button1.move(200,50)
        inputdialog.show()



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
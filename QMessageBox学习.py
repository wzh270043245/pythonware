from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        mb = QMessageBox(self)   #这个还要用到子窗口
        mb.setIcon(QMessageBox.Information)
        mb.setText ("<h3>当前文件没有被保存！</h3>")
        mb.setInformativeText("请确认是否保存")
        mb.setCheckBox(QCheckBox("下次不再提醒",mb))
        mb.setDetailedText("请先保存然后在导入新数据,或者你也可以忽略这个问题继续")
        btn1 = mb.addButton ("忽略", QMessageBox.YesRole)
        btn2 = mb.addButton ("否", QMessageBox.NoRole)
        def test(btn):
            if btn == btn1:
                print("点击了忽略")
            else:
                print("点击了否")
        mb.buttonClicked.connect(test)
        mb.open()



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
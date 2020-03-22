from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        combobox=QComboBox(self)
        # combobox.addItem ("1")
        # combobox.addItem ("2")
        # combobox.addItem ("3")
        combobox.addItems(["1","2","3"])
        combobox.move (100, 100)

        button1=QPushButton(self)
        button1.move(100,150)
        button1.setText("监听")
        def jianting():
            print(combobox.currentText())
            pass
        button1.clicked.connect(jianting)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
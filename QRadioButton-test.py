from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        rb1 = QRadioButton ("A", self)
        rb1.setShortcut("Ctrl+A")
        rb1.setChecked (True)
        rb2 = QRadioButton ("B", self)
        rb2.setShortcut ("Ctrl+B")
        rb3 = QRadioButton ("C", self)
        rb3.setShortcut ("Ctrl+C")
        rb1.move (100, 100)
        rb2.move (100, 150)
        rb3.move (100, 200)
        # rb1.toggled.connect (lambda ischecked: print ("A"))
        # rb2.toggled.connect (lambda ischecked: print ("B"))
        # rb3.toggled.connect (lambda ischecked: print ("C")
        button1=QPushButton(self)
        button1.setText("监听")
        button1.move(100,250)
        def jianting():
            rb1_ischecked = rb1.isChecked ()
            rb2_ischecked = rb2.isChecked ()
            rb3_ischecked = rb3.isChecked ()
            if rb1_ischecked == True:
                print("A")
            elif rb2_ischecked == True:
                print("B")
            elif rb3_ischecked == True:
                print("C")
        button1.clicked.connect(jianting)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
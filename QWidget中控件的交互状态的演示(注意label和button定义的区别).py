from PyQt5.Qt import *
import sys

# class Window (QWidget):
class Window (QMainWindow):
    def __init__(self):
        super ().__init__ ()
        self.setWindowTitle ("用去测试各个控件的模板的标题")
        self.resize (1000, 700)
        self.setup_ui ()




    def setup_ui(self):
        self.label1 =  QLabel (self)
        self.label1.move (50, 100)
        self.label1.setText ("这是label1")
        self.label1.setVisible(False)

        button1 = QPushButton (self)
        button1.setText ("登录")
        button1.move (150, 100)
        button1.setEnabled(False)

        lineedit1 = QLineEdit (self)
        lineedit1.move (250, 100)
        lineedit1.setText("")

        def text_cao(text):
            button1.setEnabled (True)
            self.label1.setVisible (True)
            self.label1.setText (text)
            self.label1.adjustSize ()
            # if len(text)>0:
            #     #将上述代码抄下来
            #     pass
            # else:
            #     button1.setEnabled(False)   #button1.setEnabled(len(text)>0)
            print(lineedit1.text())


        # def F_button1():
        #
        #     if lineedit1.text() == "王志欢":
        #         label1.setText ("登录成功")
        #     else:
        #         label1.setText ("登录失败")
        #         button1.setEnabled(False)
        #     label1.adjustSize ()
        def F_button1():
            if lineedit1.text () == "王志欢":
                self.label1.setText ("登录成功")
            else:
                self.label1.setText ("登录失败")
                button1.setEnabled (False)
            self.label1.adjustSize ()

        button1.clicked.connect(F_button1)
        lineedit1.textChanged.connect (text_cao)


if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = Window ()



    window.show ()
    sys.exit (app.exec_ ())
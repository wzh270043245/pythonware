#通过类获得整个屏幕的尺寸  QDesktopWidget
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon

class centerform(QMainWindow):
    def __init__(self):
            super(centerform,self).__init__()

            #设置主窗口标题
            self.setWindowTitle("窗口居中")

            #设置窗口尺寸
            self.resize(400,300)

    def center(self):
         #获取屏幕坐标
        screen=QDesktopWidget().screenGeometry()
        #获取窗口坐标
        size= self.geometry()
        print(screen.width)
        print(screen.height)
        newleft=(screen.width()-size.width())/2
        newtop=(screen.height()-size.height())/2
        self.move(newleft,newtop)

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=centerform()
    main.center()
    main.show()
    sys.exit(app.exec_())
import sys
import 信号槽
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv)  #引入主程序
    mainWindow=QMainWindow()   # 创建窗口
    ui=信号槽.Ui_MainWindow()  #将ui生成的py文件在程序中创建
    ui.setupUi(mainWindow)  #在程序中开始ui文件的窗口
    mainWindow.show()   #显示窗口
    sys.exit(app.exec_())   #窗口的循环
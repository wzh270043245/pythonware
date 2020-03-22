"""
QLabel
setAligment()  设置文本的对齐方式
setIndent()   设置文本缩进
text（）获取文本内容
setBuddy()   设置伙伴关系
setText（）设置文本内容
selectedText（）返回所选择的字符
setWordWrap（）设置是否允许换行

QLabel常用的信号（事件）：
1.当鼠标滑过QLabel控件时触发：linkHovered
2.当鼠标单击QLabel控制时触发：linkActivated
"""
# import sys
# from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QVBoxLayout,QLabel,QWidget
# from PyQt5.QtGui import QPalette ,QPixmap #调色板
# from PyQt5.QtCore import Qt
#
# class QLabel_PyQt5(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#
#     def initUI(self):
#         label1 = QLabel (self)
#         label2 = QLabel (self)
#         label3 = QLabel (self)
#         label4 = QLabel (self)
#
#         label1.setText("<font color=yellow>这是一个文本标签.</font>")
#         #设置label1的背景
#         label1.setAutoFillBackground(True) #打开填充背景
#         palette=QPalette()  #创建调色板
#         palette.setColor(QPalette.Window,Qt.blue)#设置窗口中调色板的颜色
#         label1.setPalette(palette)#将调色板加入到label1的setPalette中
#         #设置label居中对齐
#         label1.setAlignment(Qt.AlignCenter)
#         label1.setText ("ertwerffwter")
#
#         #设置文本内容label2
#         # a="<a href='#'>欢迎使用python GUI程序</a>"
#         # label2.setText("%s"% a )
#         label2.setText ("ertwerter")
#
#         # 设置居中label3
#         label3.setAlignment(Qt.AlignCenter)
#         # b="这是label3的文本内容"
#         # label3.setText("%s" % b)
#         label3.setText ("这是label3的文本内容")
#
#         #设置label4
#         label4.setAlignment (Qt.AlignRight)
#         # c = "这是label4的文本内容"
#         # label4.setText ("%s" % c)
#         label4.setText ( "这是label4的文本内容")
#
#         #增加水平布局
#         vbox=QVBoxLayout()
#         vbox.addWidget (label1)
#         vbox.addWidget (label2)
#         vbox.addWidget (label3)
#         vbox.addWidget (label4)
#
#         #绑定
#         label2.linkHovered.connect(self,linkovered)
#         label4.linkActivated.connect(self,linkclicked)
#
#         #将布局放到主程序中
#         self.setLayout(vbox)
#         self.setWindowTitle("QLabel演示")
#
#     def linkHovered(self):
#         print("当鼠标滑过label2")
#
#     def linkclicked(self):
#         print("当鼠标点击label4")
#
#
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     main=QLabel_PyQt5()
#     main.show()
#     sys.exit(app.exec_())
#
#

from python_mysql_together import SunckSql

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QVBoxLayout,QLabel,QWidget
from PyQt5.QtGui import QPalette ,QPixmap #调色板
from PyQt5.QtCore import Qt

class QLabel_PyQt5(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        label1 = QLabel (self)
        label2 = QLabel (self)
        label3 = QLabel (self)
        label4 = QLabel (self)

        s = SunckSql ('192.168.3.6', 'root', '123456', 'sunck')

        b=s.Sql_getall(s.sql_get("1221","B","1"))
        if b==():
            print("无记录！")
        else:
            for row in range(len(b)):
                # a=a[row][0]+a[row][1]+a[row][2]
                print("编号%d：" %(row+1),end="")
                print(b[row][0],end="  ")
                print(b[row][1],end="  ")
                print(b[row][2],end="  ")
                print("\n")

        # a="<font color=yellow>这是一个文本标签.</font>"
        a="你好"
        label1.setText("%s" % a)
        #设置label1的背景
        label1.setAutoFillBackground(True) #打开填充背景
        palette=QPalette()  #创建调色板
        palette.setColor(QPalette.Window,Qt.blue)#设置窗口中调色板的颜色
        label1.setPalette(palette)#将调色板加入到label1的setPalette中
        #设置label居中对齐
        label1.setAlignment(Qt.AlignCenter)

        #设置文本内容label2
        # a="<a href='#'>欢迎使用python GUI程序</a>"
        # label2.setText("%s"% a )
        label2.setText ("<a href='#'>欢迎使用</a>")

        # 设置居中label3
        label3.setAlignment(Qt.AlignCenter)
        # b="这是label3的文本内容"
        # label3.setText("%s" % b)
        label3.setToolTip("这是图片")
        label3.setPixmap(QPixmap("./time.png"))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='www.baidu.com'>欢迎使用</a>")
        #设置label4
        label4.setAlignment (Qt.AlignRight)
        # c = "这是label4的文本内容"
        # label4.setText ("%s" % c)
        label4.setToolTip ( "这是超链接")

        #增加水平布局
        vbox=QVBoxLayout()
        vbox.addWidget (label1)
        vbox.addWidget (label2)
        vbox.addWidget (label3)
        vbox.addWidget (label4)

        #绑定
        label2.linkHovered.connect(self.a)
        label4.linkActivated.connect(self.linkclicked)

        #将布局放到主程序中
        self.setLayout(vbox)
        self.setWindowTitle("QLabel演示")

    def a(self):
        print("当鼠标滑过label2")

    def linkclicked(self):
        print("当鼠标点击label4")


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLabel_PyQt5()
    main.show()
    sys.exit(app.exec_())






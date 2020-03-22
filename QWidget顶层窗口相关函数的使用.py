from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        pass



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()

    #设置窗口显示图标
    icon=QIcon("fft.png")
    window.setWindowIcon(icon)
    # 设置窗口显示图标

    # 设置顶层窗口的标题
    window.setWindowTitle (" ")
    #设置顶层窗口的标题

    #设置不透明度
    window.setWindowOpacity(0.5)
    # 设置不透明度
    
    window.show()
    sys.exit(app.exec_())
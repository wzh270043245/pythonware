from PyQt5.Qt import *
# from PyQt5.QtWidgets import QWidget,QTableW/idget,QApplication,QTableWidgetItem, QTableWidgetyItem
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        self.table=QTableWidget(self)
        self.table.setRowCount(9)
        self.table.setColumnCount(5)
        self.table.resize(600,350)
        self.table.move(100,100)
        self.table.setHorizontalHeaderLabels(["数据库内部序号","时间","编号","检测序号","峰值带/Hz"])

        massage1 = QTableWidgetItem ("1")
        self.table.setItem (0,0,massage1)

        massage2 = QTableWidgetItem ("2020-02-01")
        self.table.setItem (0, 1, massage2)

        massage3 = QTableWidgetItem ("1221A1")
        self.table.setItem (0, 2, massage3)

        massage4 = QTableWidgetItem ("1")
        self.table.setItem (0, 3, massage4)

        massage5 = QTableWidgetItem ("3370")
        self.table.setItem (0, 4, massage5)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

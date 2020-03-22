from PyQt5.Qt import *
from test7 import Ui_Form
from python_mysql_together import SunckSql
import pymysql
import datetime


class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowFlags (Qt.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)


    def  progress1(self):
        access=SunckSql('192.168.3.6','root','123456','sunck')
        self.result=access.Sql_all()
        # print (len (self.result))  # 行数
        self.tableWidget.setRowCount(len (self.result))
        self.tableWidget.setColumnCount (6)
        font = QFont('微软雅黑', 10)
        font.setBold(True)  #设置字体加粗
        self.tableWidget.horizontalHeader().setFont(font) #设置表头字体
        self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
        self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
        self.tableWidget.horizontalHeader ().resizeSection (0, 150)
        # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
        self.tableWidget.setHorizontalHeaderLabels (["时间0", "编号1", "检测序号2", "备注4", "峰值带/Hz5","地址3"])
        for i,j in enumerate(self.result):
            massage0 = QTableWidgetItem (str(j[0]))
            self.tableWidget.setItem (i, 0, massage0)

            massage1 = QTableWidgetItem (str(j[1]))
            self.tableWidget.setItem (i, 1, massage1)

            massage2 = QTableWidgetItem (str(j[2]))
            self.tableWidget.setItem (i, 2, massage2)

            massage3 = QTableWidgetItem (str(j[4]))
            self.tableWidget.setItem (i, 3, massage3)

            massage4 = QTableWidgetItem (str(j[5]))
            self.tableWidget.setItem (i, 4, massage4)

            massage5= QTableWidgetItem (str(j[3]))
            self.tableWidget.setItem (i, 5, massage5)

        self.tableWidget.horizontalHeader ().setSectionResizeMode (5, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
        # self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
        self.tableWidget.horizontalHeader ().setStyleSheet ('QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
        # QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
        QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
        self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
        # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
        for x in range (len (self.result)):  #居中
            for y in range (6):
                if y != 1:
                    item = self.tableWidget.item (x, y)
                    item.setTextAlignment (Qt.AlignCenter)
                else:
                    pass
        pass


    def progress2(self):
        access = SunckSql ('192.168.3.6', 'root', '123456', 'sunck')
        a,b=access.sql_in(self.line1.text(),self.line2.text(),self.line3.text(),"C:\\Users\\wzh\\Desktop\\000001.Wav","母线","3700","")
        access.Sql_insert(a,b)
        pass



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())


class MyModel(QSqlTableModel):
    def __init__(self):
        QSqlTableModel.__init__(self)

    def data(self, index, role=None):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return QSqlTableModel.data(self, index, role)


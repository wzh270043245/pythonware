from PyQt5.Qt import *
from test8 import Ui_Form
import pyqtgraph as pg
import numpy as np
import WAV_read
from scipy.fftpack import fft
import pylab as plt
import pyqtgraph.exporters
from python_mysql_together import SunckSql
import pymysql
import datetime
pg.setConfigOption('background', 'w')

class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowFlags (Qt.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.pyqtgraph1.setVisible (False)
        self.button2.setVisible (False)
        self.button3.setVisible (False)
        self.button4.setVisible (False)
        self.button5.setVisible (False)
        self.tableWidget.setVisible (True)

    def progress1(self):
        a = QFileDialog (self)
        result = a.getOpenFileName (self, "选择一个Wav文件", "C:\\Users\\wzh\\Desktop.\\", "Wav(*.Wav)", "Wav文件(*.Wav)")
        if result[0] == "":
            pass
        else:
            self.label.setText ("打开的文件地址：" + result[0])
            self.label.setAlignment (Qt.AlignCenter)   #水平居中
            self.label.adjustSize ()
            self.button2.setVisible (True)
            self.button3.setVisible (True)
            self.button4.setVisible (True)
            self.button5.setVisible (True)
            self.label.setVisible (True)
            self.tableWidget.setVisible (False)
            self.address=result[0]

    def progress2 (self):
        self.pyqtgraph1.clear()#清空作图区域
        self.pyqtgraph1.setVisible (True)
        p1 =self.pyqtgraph1.addPlot(title="时域图像")
        if self.address=="":
            pass
        else:
            self.tableWidget.setVisible (False)
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (self.address)
            wav_numpy = np.frombuffer (wav_data, dtype=np.short)
            wav_numpy.shape = -1, 1
            wav_numpy = wav_numpy.T / max (wav_numpy[0])
            time = np.arange (0, wav_n) / wav_fs
            p1.plot (time, wav_numpy[0] * 1.0 / max (abs (wav_numpy[0])),pen=pg.mkPen(color="r",width=1))
            p1.showGrid(True,True, alpha=0.5)
            p1.setLabel (axis='left', text='振幅')
            p1.setLabel (axis='bottom', text='时间')
            p1.setRange (yRange=(-1, 1))

    def progress3(self):
        self.pyqtgraph1.setVisible (True)
        self.pyqtgraph1.clear ()  # 清空作图区域
        p2 = self.pyqtgraph1.addPlot (title="频域图像")
        if self.address=="":
            pass
        else:
            self.tableWidget.setVisible (False)
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (self.address)
            wav_numpy = np.frombuffer (wav_data, dtype=np.short)
            wav_numpy.shape = -1, 1
            wav_numpy = wav_numpy.T / max (wav_numpy[0])
            wav_numpy=wav_numpy[0]
            cor_wav = np.correlate (wav_numpy, wav_numpy, mode='full')
            abs_fft_wav = (abs (fft (cor_wav, wav_n)))
            idx = np.arange (0, round (wav_n / 2))
            x = idx * wav_fs / wav_n
            y = abs_fft_wav[0:8192]
            p2.plot (x, y/max(y[1000:10000]), pen=pg.mkPen (color="r", width=1))
            p2.showGrid (True, True)
            p2.setRange (xRange=(1000,10000),yRange=(0,1.1))
            p2.setLabel (axis='left', text='相对幅值')
            p2.setLabel (axis='bottom', text='频率/Hz')
            pass

    def progress4(self):
        self.pyqtgraph1.setVisible (True)
        self.pyqtgraph1.clear ()  # 清空作图区域
        p3 = self.pyqtgraph1.addPlot (title="滤波后频域图像")
        if self.address=="":
            pass
        else:
            self.tableWidget.setVisible (False)
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (self.address)
            wav_numpy = np.frombuffer (wav_data, dtype=np.short)
            wav_numpy.shape = -1, 1
            wav_numpy = wav_numpy.T / max (wav_numpy[0])
            wav_numpy = wav_numpy[0]
            cor_wav = np.correlate (wav_numpy, wav_numpy, mode='full')
            abs_fft_wav = (abs (fft (cor_wav, wav_n))) ** 2
            idx = np.arange (0, round (wav_n / 2))
            x = idx * wav_fs / wav_n
            y = abs_fft_wav[0:8192]
            p3.plot (x, y / max (y[1000:10000]), pen=pg.mkPen (color="r", width=1))
            p3.showGrid (True, True)
            p3.setRange (xRange=(1000, 10000), yRange=(0, 1.1))
            p3.setLabel (axis='left', text='相对幅值')
            p3.setLabel (axis='bottom', text='频率/Hz')
            pass

    def progress5(self):
        if self.address=="":
            pass
        else:
            self.tableWidget.setVisible (False)
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (self.address)
            wav_numpy = np.frombuffer (wav_data, dtype=np.short)
            wav_numpy.shape = -1, 1
            wav_numpy = wav_numpy.T / max (wav_numpy[0])
            wav_numpy = wav_numpy[0]
            plt.figure (1)
            plt.specgram (wav_numpy, Fs=wav_fs, scale_by_freq=True, sides='default')
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
            plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
            plt.ylabel ('Frequency/Hz')
            plt.xlabel ('Time/s')
            axes = plt.gca ()
            axes.set_ylim ([0, 10000])
            plt.show ()
            pass

    def progress6(self):
        self.tableWidget.setVisible (True)
        access = SunckSql ('192.168.3.6', 'root', '123456', 'sunck')
        self.result = access.Sql_all ()
        # print (len (self.result))  # 行数
        self.tableWidget.setRowCount (len (self.result))
        self.tableWidget.setColumnCount (6)
        font = QFont ('微软雅黑', 10)
        font.setBold (True)  # 设置字体加粗
        self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
        self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
        self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
        self.tableWidget.horizontalHeader ().resizeSection (0, 150)
        # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
        self.tableWidget.setHorizontalHeaderLabels (["时间0", "编号1", "检测序号2", "备注4", "峰值带/Hz5", "地址3"])
        for i, j in enumerate (self.result):
            massage0 = QTableWidgetItem (str (j[0]))
            self.tableWidget.setItem (i, 0, massage0)

            massage1 = QTableWidgetItem (str (j[1]))
            self.tableWidget.setItem (i, 1, massage1)

            massage2 = QTableWidgetItem (str (j[2]))
            self.tableWidget.setItem (i, 2, massage2)

            massage3 = QTableWidgetItem (str (j[4]))
            self.tableWidget.setItem (i, 3, massage3)

            massage4 = QTableWidgetItem (str (j[5]))
            self.tableWidget.setItem (i, 4, massage4)

            massage5 = QTableWidgetItem (str (j[3]))
            self.tableWidget.setItem (i, 5, massage5)
        self.tableWidget.setVisible (True)
        self.tableWidget.horizontalHeader ().setSectionResizeMode (5, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
        # self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
        self.tableWidget.horizontalHeader ().setStyleSheet ('QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
        # QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
        QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
        self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
        # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
        for x in range (len (self.result)):  # 居中
            for y in range (6):
                if y != 1:
                    item = self.tableWidget.item (x, y)
                    item.setTextAlignment (Qt.AlignCenter)
                else:
                    pass
        self.tableWidget.setVisible (True)
        pass

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

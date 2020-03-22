from PyQt5.Qt import *
from test6 import Ui_Form
import pyqtgraph as pg
import numpy as np
import WAV_read
from scipy.fftpack import fft
import pylab as plt
import pyqtgraph.exporters
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

    def progress1(self):
        a=QFileDialog(self)
        a.setDirectory("C:\\Users\\wzh\\Desktop.\\")
        # b="Wav文件(*.Wav)"
        # a.setFilter (b)
        # a.setFilter ("Wav")
        a.setFileMode(QFileDialog.AnyFile)
        if a.exec():
            self.result=a.selectedFiles()
            self.label.setText ("打开的文件地址：" + self.result[0])
            self.label.setAlignment (Qt.AlignCenter)  # 水平居中
            self.label.adjustSize ()
            self.button2.setVisible (True)
            self.button3.setVisible (True)
            self.button4.setVisible (True)
            self.button5.setVisible (True)
            self.label.setVisible (True)

        # a = QFileDialog (self)
        # self.result = a.getOpenFileName (self, "选择一个Wav文件", "C:\\Users\\wzh\\Desktop.\\", "Wav(*.Wav)", "Wav文件(*.Wav)")
        # if self.result[0] == "":
        #     self.pyqtgraph1.setVisible (False)
        #     self.button2.setVisible (False)
        #     self.button3.setVisible (False)
        #     self.button4.setVisible (False)
        #     self.button5.setVisible (False)
        #     self.label.setVisible (False)
        #     pass
        # else:
        #     self.label.setText ("打开的文件地址：" + self.result[0])
        #     self.label.setAlignment (Qt.AlignCenter)   #水平居中
        #     self.label.adjustSize ()
        #     self.button2.setVisible (True)
        #     self.button3.setVisible (True)
        #     self.button4.setVisible (True)
        #     self.button5.setVisible (True)
        #     self.label.setVisible (True)


    def progress2 (self):
        self.pyqtgraph1.setVisible (True)
        self.pyqtgraph1.clear()#清空作图区域
        p1 =self.pyqtgraph1.addPlot(title="时域图像")
        if self.result[0]=="":
            pass
        else:
            address=self.result[0]
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (address)
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
        if self.result[0]=="":
            pass
        else:
            address = self.result[0]
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (address)
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
        if self.result[0]=="":
            pass
        else:
            address = self.result[0]
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (address)
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
        if self.result[0]=="":
            pass
        else:
            address = self.result[0]
            (wav_fs, wav_n, wav_data) = WAV_read.wav_read (address)
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
            # plt.savefig ('voice', dpi=300)
            plt.show ()
            pass

    def progress6(self):
        pg.setConfigOption ('foreground', (255, 255, 255))
        w = pg.GraphicsWindow ()
        p = w.addPlot ()
        p.plot (np.linspace (0.0, 20.0, 20), pen={'color': 'w'})
        p.setXRange (0, 20)
        p.setYRange (-10, 20)
        app = pg.mkQApp ()
        app.processEvents ()
        ex = pyqtgraph.exporters.ImageExporter (w.scene ())
        ex.export (fileName=self.result[0])
        pass



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

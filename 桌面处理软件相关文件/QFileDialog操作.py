from PyQt5.Qt import *
import sys

import WAV_read
import TIME_domain
import FFT_domain
import VOICE
from time import process_time


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用去测试各个控件的模板的标题")
        self.resize(1000,700)
        self.setup_ui()

    def setup_ui(self):
        button1=QPushButton(self)
        button1.setText("打开文件")
        button1.clicked.connect(self.openfile_dialog)
        self.label1=QLabel(self)
        self.label1.move(100,100)
        self.label1.setText("")




    def openfile_dialog(self):
        a=QFileDialog(self)
        a.setLabelText(QFileDialog.FileName,"nihao")
        self.result=a.getOpenFileName(self,"选择一个Wav文件","C:\\Users\\wzh\\Desktop.\\","Wav(*.Wav)","Wav文件(*.Wav)")

        print(a.accept())
        print(a.reject())
        self.label1.setText (self.result[0])
        self.label1.adjustSize()
        # def opencaozuo():
        #     self.label1.setText (self.result[0])
        #     self.label1.adjustSize ()
        # def closecaozuo(seff):
        #     self.label1.setText ("你没打开")
        #     self.label1.adjustSize ()


        # a.accepted.connect (opencaozuo)
        # a.rejected.connect (closecaozuo)

        # if int(a.accept())==1:
        #     self.label1.setText(self.result[0])
        #     self.label1.adjustSize()
        #     print(self.result)
        # elif int(a.reject())==0:
        #     self.label1.setText ("你没打开")
        #     self.label1.adjustSize ()
        # if self.label1.text()!="":
        #     self.process()
        if self.label1.text()!="":
            self.process ()

    def process(self):
        begin_time = process_time ()
        address = self.result[0]
        (wav_fs, wav_n, wav_data) = WAV_read.wav_read (address)
        wav_numpy = TIME_domain.time_domain (wav_fs, wav_n, wav_data)
        FFT_domain.fft_domain (wav_numpy, wav_fs, wav_n)
        VOICE.voice (wav_numpy, wav_fs)
        end_time = process_time ()
        run_time = end_time - begin_time
        print ('程序运行时间：', run_time)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
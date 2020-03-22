#通过类获得整个屏幕的尺寸  QDesktopWidget
# import WAV_read
# import TIME_domain
# import FFT_domain
# import VOICE
# from time import process_time

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QHBoxLayout,QPushButton,QWidget
# from PyQt5.Qt import *
class quitapp(QMainWindow):
    def __init__(self):
        super(quitapp,self).__init__()

        #设置主窗口标题
        self.setWindowTitle("退出应用程序")

        #添加button
        self.button1=QPushButton("退出程序")
        #将信号与槽关联
        self.button1.clicked.connect(self.onclick_button)

        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe=QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)

    #按钮单击事件的方法(槽)
    def onclick_button(self):
        sender=self.sender()
        print(sender.text()+"被按下")
        app=QApplication.instance()
        app.quit()

        # begin_time = process_time ()
        # # address=input('请输入WAV文件格式地址：')
        # address = "C:\\Users\\wzh\\Desktop\\000001.Wav"
        # (wav_fs, wav_n, wav_data) = WAV_read.wav_read (address)
        # wav_numpy = TIME_domain.time_domain (wav_fs, wav_n, wav_data)
        # FFT_domain.fft_domain (wav_numpy, wav_fs, wav_n)
        # VOICE.voice (wav_numpy, wav_fs)
        #
        # end_time = process_time ()
        # run_time = end_time - begin_time
        # print ('程序运行时间：', run_time)






if __name__=="__main__":
    app=QApplication(sys.argv)
    main=quitapp()
    main.show()
    sys.exit(app.exec_())
from PyQt5.Qt import *
from PyQt5.QtCore import pyqtSignal, QTimer,QDateTime
from PyQt5.QtGui import QIntValidator
from access import Ui_Form  #导入登录窗口（不是严格意义上的子窗口）的布局文件，这里的1可以不加，因为已经将主窗口改为QMainWindow类型
from test93 import Ui_MainWindow #导入主窗口的布局文件，文件名为test93.ui文件
from savetest import Window3 #导入保存对话框的子窗口，这里的3也可以不用加，因为类型已经不冲突
import pyqtgraph as pg  #画图的工具包
import numpy as np   #wav打开后需要用到numpy
import WAV_read  #自己封装的导入wav文件的函数
from scipy.fftpack import fft #图像处理需要用到fft
import pylab as plt #语谱图需要用到pylab
# import pyqtgraph.exporters
from python_mysql_together import SunckSql  #自己封装的mysql数据库函数，直接调用即可
pg.setConfigOption('background', [210, 236, 255])
class Window1(QWidget,Ui_Form):   #这是登录的窗口
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags (Qt.MSWindowsFixedSizeDialogHint)  #关闭放大按钮
        self.setWindowIcon (QIcon ("xy.ico"))#设置登录窗口的图标
        self.line1.setPlaceholderText ("请输入账号...")#设置lineedit默认的文本
        self.line2.setPlaceholderText ("请输入密码...")
        self.line2.setEchoMode(QLineEdit.Password)#设置密码为密码格式展示
        self.label3.setVisible(False)#label3用于提示输入的账号密码是否正确
        int_validato = QIntValidator (self)  # 实例化整型验证器
        self.line1.setValidator (int_validato)  # 只输入数字
        self.line2.setValidator (int_validato)  # 只输入数字

    def keyPressEvent(self, event):
        if event.key () == Qt.Key_Enter:
            self.progress1()
        if event.key () == Qt.Key_Escape:
            self.progress2()

    def progress1 (self):
        zhanghao = "1"#账号密码
        password = "1"
        self.zhanghao = self.line1.text ()#提取输入的账号和密码
        self.password = self.line2.text ()
        if self.zhanghao == zhanghao and self.password == password:#判断输入的账号密码是否正确
            self.label3.setVisible (False)
            self.label3.setText ("登录成功！")
            self.label3.setStyleSheet ('color:red')
            self.label3.setAlignment (Qt.AlignCenter)
            self.label3.setVisible (True)
            add1()#打开主窗口关闭登录窗口的全局函数
            pass
        elif self.zhanghao == zhanghao and self.password != password:
            self.label3.setText("密码错误！请重新输入...")
            self.label3.setStyleSheet ('color:red')
            self.label3.setAlignment (Qt.AlignCenter)
            self.label3.setVisible (True)
            self.line2.setText("")
            pass
        elif (self.zhanghao != zhanghao and self.password != password) or (self.zhanghao != zhanghao and self.password == password):
            self.label3.setText ("账号以及密码错误！请重新输入...")
            self.label3.setStyleSheet ('color:red')
            self.label3.setAlignment (Qt.AlignCenter)
            self.label3.setVisible (True)
            self.line1.setText ("")
            self.line2.setText ("")
            pass
        pass

    def progress2 (self):#关闭登录窗口
        self.close()
        pass

    def progress3(self):#预留出的槽函数
        pass

class Window2(QMainWindow,Ui_MainWindow):#主窗口
    Singal = pyqtSignal (str,str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags (Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon (QIcon ("xy.ico"))  # 设置窗口图标
        self.setWindowTitle ("振动信号处理程序")

        self.groupBox2.setVisible (False)#设置删除、更改、查询按钮组的不可见
        self.groupBox3.setVisible (False)
        self.groupBox4.setVisible (False)


        self.pyqtgraph1.setVisible (False)
        self.button2.setVisible (False)
        self.button3.setVisible (False)
        self.button4.setVisible (False)
        self.button5.setVisible (False)
        self.tableWidget.setVisible (False)
        self.button7.setEnabled (False)
        self.action2.setEnabled (False)
        self.action5_1.setEnabled (False)
        self.action5_2.setEnabled (False)
        self.action5_3.setEnabled (False)
        self.action5_4.setEnabled (False)
        int_validato = QIntValidator (self)  # 实例化整型验证器
        self.line4_1.setValidator (int_validato)  # 只输入数字
        self.line2_1.setValidator (int_validato)  # 只输入数字
        self.line3_2_1.setValidator (int_validato)  # 只输入数字
        self.line4_2.setValidator (int_validato)  # 只输入数字
        self.save = Window3 () #在主窗口中实例化保存的子窗口
        self.Singal.connect (self.recv)  # 父窗体向子窗体传数据的“信号与槽连接”
        self.button1.clicked.connect (self.child) # 子窗口向父窗口传递数据的信号与槽连接
        self.action1.triggered.connect (self.child)  # 子窗口向父窗口传递数据的信号与槽连接

        pix = QPixmap ('x.png').scaled(self.label_photo.width(), self.label_photo.height())
        self.label_photo.setPixmap (pix) #设置图标

        self.timer = QTimer (self)#设置显示的时间
        self.timer.timeout.connect (self.showtime)
        self.timer.start ()

        self.judgesignal = "0"  # 判断保存标志的变量
        self.judgesignal_first = 1  # 第一次执行导入文件命令的判断变量
        self.Savenumber = 0  #计数保存成功的数量
        self.Opennumber = 0  #计数导入的wav文件的总数目
        self.address = ""
        self.judge_new_old = 0 #判断是新数据导入还是历史数据导入，0是旧数据，此时设置保存按钮的setEnabled按钮为False

    def closeEvent(self, event):
        # 创建一个消息盒子（提示框）
        quitMsgBox = QMessageBox (self)
        # 设置提示框的标题
        quitMsgBox.setIcon (QMessageBox.Information)
        quitMsgBox.setWindowTitle ('确认提示')
        # 设置提示框的内容
        quitMsgBox.setText ("<h3>你确定退出吗？</h3>")
        quitMsgBox.setInformativeText ("请确定是否退出...")
        # 设置按钮标准，一个yes一个no
        quitMsgBox.setStandardButtons (QMessageBox.Yes | QMessageBox.No)
        # 获取两个按钮并且修改显示文本
        buttonY = quitMsgBox.button (QMessageBox.Yes)
        buttonY.setText ('确定')
        buttonN = quitMsgBox.button (QMessageBox.No)
        buttonN.setText ('取消')
        quitMsgBox.exec_ ()
        # 判断返回值，如果点击的是Yes按钮，关闭组件和应用，否则就忽略关闭事件
        if quitMsgBox.clickedButton () == buttonY:
            event.accept ()
        else:
            event.ignore ()

    # def keyPressEvent(self, event):   # 组合按键
    #     if event.key () == Qt.Key_F4:
    #         if QApplication.keyboardModifiers () == Qt.AltModifier:
    #             # 创建一个消息盒子（提示框）
    #             quitMsgBox = QMessageBox ()
    #             # 设置提示框的标题
    #             quitMsgBox.setIcon (QMessageBox.Information)
    #             quitMsgBox.setWindowTitle ('确认提示')
    #             # 设置提示框的内容
    #             quitMsgBox.setText ("<h3>你确定退出吗？</h3>")
    #             quitMsgBox.setInformativeText ("请确定是否退出")
    #             # 设置按钮标准，一个yes一个no
    #             quitMsgBox.setStandardButtons (QMessageBox.Yes | QMessageBox.No)
    #             # 获取两个按钮并且修改显示文本
    #             buttonY = quitMsgBox.button (QMessageBox.Yes)
    #             buttonY.setText ('确定')
    #             buttonN = quitMsgBox.button (QMessageBox.No)
    #             buttonN.setText ('取消')
    #             quitMsgBox.exec_ ()
    #             # 判断返回值，如果点击的是Yes按钮，就关闭组件和应用，否则就忽略关闭事件
    #             if quitMsgBox.clickedButton () == buttonY:
    #                 event.accept ()
    #             else:
    #                 event.ignore ()

    def showtime(self):#显示时间的函数
        datetime = QDateTime.currentDateTime()
        text = datetime.toString ('yyyy-MM-dd  hh:mm:ss  dddd')
        self.label_time.setText (text)

    def child(self):
        self.save.childclicked.connect (self.recv1)  # 子窗体向父窗体传数据的“信号与槽连接”

    def recv1(self, s1,s2):  #用于接收子窗口的判断标志的函数
        self.judgesignal = s1
        self.Savenumber = s2
        print(self.judgesignal,"成功接收")

    def opendata(self):
        a = QFileDialog (self)
        result = a.getOpenFileName (self, "选择一个Wav文件", "C:\\Users\\wzh\\Desktop.\\", "Wav(*.Wav)", "Wav文件(*.Wav)")
        if result[0] == "":
            pass
        else:
            self.address = result[0]
            self.Opennumber += 1
            self.button7.setEnabled (False)
            self.action2.setEnabled (False)
            self.label.setText ("本次检测共导入 %s 个文件，成功保存 %s 组，当前导入文件的地址为：%s"  % (str(self.Opennumber),str(self.Savenumber),self.address) )
            self.label.setAlignment (Qt.AlignCenter)  # 水平居中
            self.label.adjustSize ()
            self.button2.setVisible (True)
            self.button3.setVisible (True)
            self.button4.setVisible (True)
            self.button5.setVisible (True)
            self.label.setVisible (True)
            self.tableWidget.setVisible (False)
            self.groupBox2.setVisible (False)
            self.groupBox3.setVisible (False)
            self.groupBox4.setVisible (False)
            self.action5_1.setEnabled (True)
            self.action5_2.setEnabled (True)
            self.action5_3.setEnabled (True)
            self.action5_4.setEnabled (True)
            self.judgesignal = "0"
            self.judgesignal_first = 0   #判断是否是打开程序后第一次点击导入按钮
            self.judge_new_old = 1
            self.progress2()

    def progress1(self):#导入按钮
        if  self.judgesignal == "0" and self.judgesignal_first != 1:
            mb = QMessageBox (self)
            mb.setIcon (QMessageBox.Information)
            mb.setText ("<h3>当前文件没有被保存！</h3>")
            mb.setInformativeText ("请确认是否保存")
            # mb.setCheckBox (QCheckBox ("下次不再提醒", mb))
            mb.setWindowTitle("未保存提示")
            mb.setDetailedText ("请先保存然后再导入新数据,或者你也可以忽略这个问题继续...")
            btn1 = mb.addButton ("忽略", QMessageBox.YesRole)
            btn2 = mb.addButton ("返回保存", QMessageBox.NoRole)
            def test(btn):
                if btn == btn1:
                    print ("点击了忽略")
                    self.opendata ()
                else:
                    print ("点击了返回保存")
            mb.buttonClicked.connect (test)
            mb.open ()
        elif self.judgesignal == "1" and self.judgesignal_first != 1:
            self.opendata ()
        elif self.button7.isEnabled() == False and self.judgesignal_first == 1:  #第一次导入
            self.opendata ()

    def progress2(self):#时域图像
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
            # p1.disableAutoRange ()
            p1.showGrid(True,True, alpha=0.5)
            p1.setLabel (axis='left', text='振幅')
            p1.setLabel (axis='bottom', text='时间')
            p1.setRange (yRange=(-1, 1))
            self.groupBox2.setVisible (False)
            self.groupBox3.setVisible (False)
            self.groupBox4.setVisible (False)

    def progress3(self):#频域图像
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
            cor_wav = np.correlate (wav_numpy, wav_numpy, mode='full')  #注意：如果后期为TXT数据，则只需将txt转化为一维数组，进行自相关即可
            abs_fft_wav = (abs (fft (cor_wav, wav_n)))  #针对自相关的结果以及点数进行fft，并取绝对值，取了绝对值后图像关于x=某个值对称，因此至于取一半点数分析即可
            #这里表示取0~wav_n=16384一半的值为索引idx    注意！！！为啥除以2：因为取了上一步取了绝对值后，图像关于x=某一值对称，为消除这个现象，取一半点数分析即可，因此取了0~8192个点
            idx = np.arange (0, round (wav_n /2))    #这里仅取了时域图像的一半来分析8192个点，原本是不用除2，除了2，所以是8192个点
            #对横坐标x划分区间，分法为idx=8192份个点
            x = idx * wav_fs / wav_n
            y = (abs_fft_wav[0:8192])   #y = (abs_fft_wav[0:16384])
            p2.plot (x, y/ max (y[100:8192]), pen=pg.mkPen (color="r", width=1))  #8192>>16384
            y = y / max (y[100:8192])  #请切记x，y分别有8192个点   #8192>>16384
            y_max = max (y[100:8192])     #8192>>16384
            x_index = np.where (y == y_max)
            self.max_x = round(x[x_index[0][0]], 2)
            p2.showGrid (True, True)
            p2.setRange (xRange=(1000,10000),yRange=(0,1.1))
            p2.setLabel (axis='left', text='相对幅值')
            p2.setLabel (axis='bottom', text='频率/Hz')
            self.groupBox2.setVisible (False)
            self.groupBox3.setVisible (False)
            self.groupBox4.setVisible (False)
            if self.judge_new_old == 1:
                self.button7.setEnabled (True)
                self.action2.setEnabled (True)
            pass

    def progress4(self):#滤波后频域图像
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
            p3.plot (x, y / max (y[100:10000]), pen=pg.mkPen (color="r", width=1))
            y = y / max (y[100:10000])
            y_max = max (y[100:10000])
            x_index = np.where (y == y_max)
            self.max_x = round (x[x_index[0][0]], 2)
            p3.showGrid (True, True)
            p3.setRange (xRange=(1000, 10000), yRange=(0, 1.1))
            p3.setLabel (axis='left', text='相对幅值')
            p3.setLabel (axis='bottom', text='频率/Hz')
            self.groupBox2.setVisible (False)
            self.groupBox3.setVisible (False)
            self.groupBox4.setVisible (False)
            if self.judge_new_old == 1:
                self.button7.setEnabled (True)
                self.action2.setEnabled (True)
            pass

    def progress5(self):#外挂的语谱图
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
            plt.title("语谱图")
            plt.specgram (wav_numpy, Fs=wav_fs, scale_by_freq=True, sides='default')
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
            plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
            plt.ylabel ('Frequency/Hz')
            plt.xlabel ('Time/s')
            axes = plt.gca ()
            axes.set_ylim ([0, 10000])
            plt.show ()
            self.groupBox2.setVisible (False)
            self.groupBox3.setVisible (False)
            self.groupBox4.setVisible (False)
            pass

    def buttonForRow(self,tableaddress):   #在表格中创建按钮的函数
        def test1( tableaddress1):
            try:
                self.address = tableaddress1
                self.label.setText (
                    "当前导入文件的地址为：%s" % (self.address))
                self.label.setAlignment (Qt.AlignCenter)  # 水平居中
                # self.label.adjustSize ()
                self.progress2 ()
                self.address = tableaddress1
                self.button2.setVisible (True)
                self.button3.setVisible (True)
                self.button4.setVisible (True)
                self.button5.setVisible (True)
                self.action5_1.setEnabled (True)
                self.action5_2.setEnabled (True)
                self.action5_3.setEnabled (True)
                self.action5_4.setEnabled (True)
                self.button7.setEnabled (False)
                self.action2.setEnabled (False)
                self.judge_new_old = 0   #判断是旧文件，目的是使两个保存button7和action2按钮失效
                self.judgesignal_first = 1   #若查看失败，则导入按钮回归原始状态
            except:
                self.judgesignal_first = 1 #若查看失败，则导入按钮回归原始状态
                self.button7.setEnabled (False)
                self.action2.setEnabled (False)
                self.address = ""
                self.tableWidget.setVisible (True)
                print("请确认文件是否删除")
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Information)
                mb.setText ("<h3>文件导入失败！</h3>")
                mb.setInformativeText ("请确认文件是否在原始位置...")
                mb.setWindowTitle ("文件不存在")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
        viewBtn = QPushButton ('查看')
        viewBtn.setStyleSheet (''' text-align : center;
                                          background-color : DarkSeaGreen;
                                          border-style: outset;''')
        viewBtn.clicked.connect (lambda : test1(tableaddress))
        return viewBtn

    def progress6(self):#历史记录按钮
        self.pyqtgraph1.setVisible (False)
        self.tableWidget.setVisible (True)
        access = SunckSql ('localhost', 'root', '123456', 'sunck')
        self.result = access.Sql_all ()
        # print (len (self.result))  # 行数
        self.tableWidget.setRowCount (len (self.result))
        self.tableWidget.setColumnCount (9)
        font = QFont ('微软雅黑', 10)
        font.setBold (True)  # 设置字体加粗
        self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
        self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
        self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
        self.tableWidget.horizontalHeader ().resizeSection (0, 150)
        # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
        self.tableWidget.setHorizontalHeaderLabels (["序号","时间", "编号", "次数", "峰值带/Hz","备注（1）","备注（3）", "地址","查看按钮"])
        for i, j in enumerate (self.result):
            massage0 = QTableWidgetItem (str (j[0]))
            self.tableWidget.setItem (i, 0, massage0)

            massage1 = QTableWidgetItem (str (j[1]))
            self.tableWidget.setItem (i, 1, massage1)

            massage2 = QTableWidgetItem (str (j[2]))
            self.tableWidget.setItem (i, 2, massage2)

            massage3 = QTableWidgetItem (str (j[3]))
            self.tableWidget.setItem (i, 3, massage3)

            massage4 = QTableWidgetItem (str (j[4]))
            self.tableWidget.setItem (i, 4, massage4)

            massage5 = QTableWidgetItem (str (j[5]))
            self.tableWidget.setItem (i, 5, massage5)

            massage6 = QTableWidgetItem (str (j[6]))
            self.tableWidget.setItem (i, 6, massage6)

            massage7 = QTableWidgetItem (str (j[7]))
            self.tableWidget.setItem (i, 7, massage7)

            btn = self.buttonForRow (str (j[7]))
            self.tableWidget.setCellWidget (i, 8, btn)

        self.tableWidget.setVisible (True)
        self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
        QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
        self.tableWidget.horizontalHeader ().setStyleSheet ('QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
        self.tableWidget.horizontalHeader ().setSectionResizeMode (8, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
        self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
        # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
        for x in range (len (self.result)):  # 居中
            for y in range (8):
                if y != 1:
                    item = self.tableWidget.item (x, y)
                    item.setTextAlignment (Qt.AlignCenter)
                else:
                    pass
        self.tableWidget.setVisible (True)
        self.groupBox2.setVisible (False)
        self.groupBox3.setVisible (False)
        self.groupBox4.setVisible (False)
        self.tableWidget.setFixedSize (1300, 700)
        mb = QMessageBox (self)
        mb.setIcon (QMessageBox.Information)
        mb.setText ("<h3>数据库连接成功！</h3>")
        mb.setInformativeText ("点击确定或取消...")
        mb.setWindowTitle ("数据库连接提示")
        mb.addButton ("确定", QMessageBox.YesRole)
        mb.addButton ("取消", QMessageBox.NoRole)
        mb.open ()
        # print(self.tableWidget.item(19,7).text())  #用于读取QTableWidget中每一行的元素
        pass

    def datelabel(self):#保存后，标签的更新延迟一步  """*****"""
        self.label.setText (
            "本次检测共导入 %s 个文件，成功保存 %s 组，当前导入文件的地址为：%s" % (str (self.Opennumber), str (self.Savenumber), self.address))
        self.label.setText (
            "本次检测共导入 %s 个文件，成功保存 %s 组，当前导入文件的地址为：%s" % (str(self.Opennumber), str(self.Savenumber), self.address))

    def progress7(self):#打开保存子窗口
        self.save.setWindowModality (Qt.ApplicationModal)#使打开的子窗口模态化显示
        self.save.show()
        self.Singal.emit (self.address,str(self.max_x))#向子窗口中传递地址以及寻峰得到的最大值
        self.datelabel()
        pass

    def recv(self,s1,s2):#主窗口以及子窗口的槽函数，父窗口向子窗口传递值的槽函数
        try:
            self.save.label20.setText (s1)
            self.save.label21.setText (str(s2))
            print ("success")
        except:
            print("fail")
        pass

    def progress8(self):#查询、删除、更改的按钮
        self.pyqtgraph1.setVisible (False)
        self.groupBox2.setVisible (True)
        self.groupBox3.setVisible (True)
        self.groupBox4.setVisible (True)
        self.tableWidget.setVisible (True)
        self.tableWidget.setFixedSize (740, 700)
        access = SunckSql ('localhost', 'root', '123456', 'sunck')
        result = access.Sql_all ()
        # print (len (self.result))  # 行数
        self.tableWidget.setRowCount (len (result))
        self.tableWidget.setColumnCount (8)
        font = QFont ('微软雅黑', 10)
        font.setBold (True)  # 设置字体加粗
        self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
        self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
        self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
        self.tableWidget.horizontalHeader ().resizeSection (0, 150)
        # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
        self.tableWidget.setHorizontalHeaderLabels (["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
        for i, j in enumerate (result):
            massage0 = QTableWidgetItem (str (j[0]))
            self.tableWidget.setItem (i, 0, massage0)

            massage1 = QTableWidgetItem (str (j[1]))
            self.tableWidget.setItem (i, 1, massage1)

            massage2 = QTableWidgetItem (str (j[2]))
            self.tableWidget.setItem (i, 2, massage2)

            massage3 = QTableWidgetItem (str (j[3]))
            self.tableWidget.setItem (i, 3, massage3)

            massage4 = QTableWidgetItem (str (j[4]))
            self.tableWidget.setItem (i, 4, massage4)

            massage5 = QTableWidgetItem (str (j[5]))
            self.tableWidget.setItem (i, 5, massage5)

            massage6 = QTableWidgetItem (str (j[6]))
            self.tableWidget.setItem (i, 6, massage6)

            massage7 = QTableWidgetItem (str (j[7]))
            self.tableWidget.setItem (i, 7, massage7)

        self.tableWidget.setVisible (True)
        self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
        self.tableWidget.horizontalHeader ().setStyleSheet ('QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
        QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
        self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
        QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
        self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
        # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
        for x in range (len (result)):  # 居中
            for y in range (8):
                if y != 1:
                    item = self.tableWidget.item (x, y)
                    item.setTextAlignment (Qt.AlignCenter)
                else:
                    pass
        self.tableWidget.setVisible (True)
        pass

    def progress9(self):# 查询
        rb1_ischecked = self.rb2_1.isChecked ()
        rb2_ischecked = self.rb2_2.isChecked ()
        rb3_ischecked = self.rb2_3.isChecked ()
        if self.line2_1.text() != "" and rb1_ischecked == False and rb2_ischecked == False and rb3_ischecked == False and self.combobox2_1.currentText() == "全部":
            access = SunckSql ('localhost', 'root', '123456', 'sunck')
            results_one = access.Sql_getall (access.sql_getone (self.line2_1.text()))
            if results_one == ():
                self.tableWidget.setRowCount (0)
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (
                    ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                print ("无记录！")
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Warning)
                mb.setText ("<h3>查询失败！</h3>")
                mb.setInformativeText ("无此筛选项数据...")
                mb.setWindowTitle ("查询失败提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
            else:
                self.tableWidget.setRowCount (len (results_one))
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                for i, j in enumerate (results_one):
                    massage0 = QTableWidgetItem (str (j[0]))
                    self.tableWidget.setItem (i, 0, massage0)

                    massage1 = QTableWidgetItem (str (j[1]))
                    self.tableWidget.setItem (i, 1, massage1)

                    massage2 = QTableWidgetItem (str (j[2]))
                    self.tableWidget.setItem (i, 2, massage2)

                    massage3 = QTableWidgetItem (str (j[3]))
                    self.tableWidget.setItem (i, 3, massage3)

                    massage4 = QTableWidgetItem (str (j[4]))
                    self.tableWidget.setItem (i, 4, massage4)

                    massage5 = QTableWidgetItem (str (j[5]))
                    self.tableWidget.setItem (i, 5, massage5)

                    massage6 = QTableWidgetItem (str (j[6]))
                    self.tableWidget.setItem (i, 6, massage6)

                    massage7 = QTableWidgetItem (str (j[7]))
                    self.tableWidget.setItem (i, 7, massage7)

                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                for x in range (len (results_one)):  # 居中
                    for y in range (8):
                        if y != 1:
                            item = self.tableWidget.item (x, y)
                            item.setTextAlignment (Qt.AlignCenter)
                        else:
                            pass
                self.tableWidget.setVisible (True)
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Information)
                mb.setText ("<h3>查询成功！</h3>")
                mb.setInformativeText ("点击确定或取消...")
                mb.setWindowTitle ("查询成功提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
        elif self.line2_1.text() != "" and rb1_ischecked == True and self.combobox2_1.currentText() == "全部":
            access = SunckSql ('localhost', 'root', '123456', 'sunck')
            results_two = access.Sql_getall (access.sql_gettwo (self.line2_1.text (),"A"))
            if results_two == ():
                self.tableWidget.setRowCount (0)
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (
                    ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                print ("无记录！")
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Warning)
                mb.setText ("<h3>查询失败！</h3>")
                mb.setInformativeText ("无此筛选项数据...")
                mb.setWindowTitle ("查询失败提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
            else:
                self.tableWidget.setRowCount (len (results_two))
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                for i, j in enumerate (results_two):
                    massage0 = QTableWidgetItem (str (j[0]))
                    self.tableWidget.setItem (i, 0, massage0)

                    massage1 = QTableWidgetItem (str (j[1]))
                    self.tableWidget.setItem (i, 1, massage1)

                    massage2 = QTableWidgetItem (str (j[2]))
                    self.tableWidget.setItem (i, 2, massage2)

                    massage3 = QTableWidgetItem (str (j[3]))
                    self.tableWidget.setItem (i, 3, massage3)

                    massage4 = QTableWidgetItem (str (j[4]))
                    self.tableWidget.setItem (i, 4, massage4)

                    massage5 = QTableWidgetItem (str (j[5]))
                    self.tableWidget.setItem (i, 5, massage5)

                    massage6 = QTableWidgetItem (str (j[6]))
                    self.tableWidget.setItem (i, 6, massage6)

                    massage7 = QTableWidgetItem (str (j[7]))
                    self.tableWidget.setItem (i, 7, massage7)

                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                for x in range (len (results_two)):  # 居中
                    for y in range (8):
                        if y != 1:
                            item = self.tableWidget.item (x, y)
                            item.setTextAlignment (Qt.AlignCenter)
                        else:
                            pass
                self.tableWidget.setVisible (True)
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Information)
                mb.setText ("<h3>查询成功！</h3>")
                mb.setInformativeText ("点击确定或取消...")
                mb.setWindowTitle ("查询成功提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
        elif self.line2_1.text() != "" and rb2_ischecked == True and self.combobox2_1.currentText() == "全部":
            access = SunckSql ('localhost', 'root', '123456', 'sunck')
            results_two = access.Sql_getall (access.sql_gettwo (self.line2_1.text (),"B"))
            if results_two == ():
                self.tableWidget.setRowCount (0)
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (
                    ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                print ("无记录！")
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Warning)
                mb.setText ("<h3>查询失败！</h3>")
                mb.setInformativeText ("无此筛选项数据...")
                mb.setWindowTitle ("查询失败提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
            else:
                self.tableWidget.setRowCount (len (results_two))
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                for i, j in enumerate (results_two):
                    massage0 = QTableWidgetItem (str (j[0]))
                    self.tableWidget.setItem (i, 0, massage0)

                    massage1 = QTableWidgetItem (str (j[1]))
                    self.tableWidget.setItem (i, 1, massage1)

                    massage2 = QTableWidgetItem (str (j[2]))
                    self.tableWidget.setItem (i, 2, massage2)

                    massage3 = QTableWidgetItem (str (j[3]))
                    self.tableWidget.setItem (i, 3, massage3)

                    massage4 = QTableWidgetItem (str (j[4]))
                    self.tableWidget.setItem (i, 4, massage4)

                    massage5 = QTableWidgetItem (str (j[5]))
                    self.tableWidget.setItem (i, 5, massage5)

                    massage6 = QTableWidgetItem (str (j[6]))
                    self.tableWidget.setItem (i, 6, massage6)

                    massage7 = QTableWidgetItem (str (j[7]))
                    self.tableWidget.setItem (i, 7, massage7)

                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                for x in range (len (results_two)):  # 居中
                    for y in range (8):
                        if y != 1:
                            item = self.tableWidget.item (x, y)
                            item.setTextAlignment (Qt.AlignCenter)
                        else:
                            pass
                self.tableWidget.setVisible (True)
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Information)
                mb.setText ("<h3>查询成功！</h3>")
                mb.setInformativeText ("点击确定或取消...")
                mb.setWindowTitle ("查询成功提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
        elif self.line2_1.text() != "" and rb3_ischecked == True and self.combobox2_1.currentText() == "全部":
            access = SunckSql ('localhost', 'root', '123456', 'sunck')
            results_two = access.Sql_getall (access.sql_gettwo (self.line2_1.text (),"C"))
            if results_two == ():
                self.tableWidget.setRowCount (0)
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (
                    ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                print ("无记录！")
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Warning)
                mb.setText ("<h3>查询失败！</h3>")
                mb.setInformativeText ("无此筛选项数据...")
                mb.setWindowTitle ("查询失败提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
            else:
                self.tableWidget.setRowCount (len (results_two))
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                for i, j in enumerate (results_two):
                    massage0 = QTableWidgetItem (str (j[0]))
                    self.tableWidget.setItem (i, 0, massage0)

                    massage1 = QTableWidgetItem (str (j[1]))
                    self.tableWidget.setItem (i, 1, massage1)

                    massage2 = QTableWidgetItem (str (j[2]))
                    self.tableWidget.setItem (i, 2, massage2)

                    massage3 = QTableWidgetItem (str (j[3]))
                    self.tableWidget.setItem (i, 3, massage3)

                    massage4 = QTableWidgetItem (str (j[4]))
                    self.tableWidget.setItem (i, 4, massage4)

                    massage5 = QTableWidgetItem (str (j[5]))
                    self.tableWidget.setItem (i, 5, massage5)

                    massage6 = QTableWidgetItem (str (j[6]))
                    self.tableWidget.setItem (i, 6, massage6)

                    massage7 = QTableWidgetItem (str (j[7]))
                    self.tableWidget.setItem (i, 7, massage7)

                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                for x in range (len (results_two)):  # 居中
                    for y in range (8):
                        if y != 1:
                            item = self.tableWidget.item (x, y)
                            item.setTextAlignment (Qt.AlignCenter)
                        else:
                            pass
                self.tableWidget.setVisible (True)
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Information)
                mb.setText ("<h3>查询成功！</h3>")
                mb.setInformativeText ("点击确定或取消...")
                mb.setWindowTitle ("查询成功提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
        else:
            if self.line2_1.text() != "" and (rb1_ischecked == True or rb2_ischecked == True or rb3_ischecked == True) and self.combobox2_1.currentText() != "全部":
                access = SunckSql ('localhost', 'root', '123456', 'sunck')
                if rb1_ischecked == True:
                    xiang = "A"
                elif rb2_ischecked == True:
                    xiang = "B"
                elif rb3_ischecked == True:
                    xiang = "C"
                results_three = access.Sql_getall (access.sql_getthree (self.line2_1.text (), xiang, self.combobox2_1.currentText ()))
                if results_three == ():
                    self.tableWidget.setRowCount (0)
                    self.tableWidget.setColumnCount (8)
                    font = QFont ('微软雅黑', 10)
                    font.setBold (True)  # 设置字体加粗
                    self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                    self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                    self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                    self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                    # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                    self.tableWidget.setHorizontalHeaderLabels (
                        ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                    print ("无记录！")
                    mb = QMessageBox (self)
                    mb.setIcon (QMessageBox.Warning)
                    mb.setText ("<h3>查询失败！</h3>")
                    mb.setInformativeText ("无此筛选项数据...")
                    mb.setWindowTitle ("查询失败提示")
                    mb.addButton ("确定", QMessageBox.YesRole)
                    mb.addButton ("取消", QMessageBox.NoRole)
                    mb.open ()
                else:
                    self.tableWidget.setRowCount (len (results_three))
                    self.tableWidget.setColumnCount (8)
                    font = QFont ('微软雅黑', 10)
                    font.setBold (True)  # 设置字体加粗
                    self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                    self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                    self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                    self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                    # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                    self.tableWidget.setHorizontalHeaderLabels (
                        ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                    for i, j in enumerate (results_three):
                        massage0 = QTableWidgetItem (str (j[0]))
                        self.tableWidget.setItem (i, 0, massage0)

                        massage1 = QTableWidgetItem (str (j[1]))
                        self.tableWidget.setItem (i, 1, massage1)

                        massage2 = QTableWidgetItem (str (j[2]))
                        self.tableWidget.setItem (i, 2, massage2)

                        massage3 = QTableWidgetItem (str (j[3]))
                        self.tableWidget.setItem (i, 3, massage3)

                        massage4 = QTableWidgetItem (str (j[4]))
                        self.tableWidget.setItem (i, 4, massage4)

                        massage5 = QTableWidgetItem (str (j[5]))
                        self.tableWidget.setItem (i, 5, massage5)

                        massage6 = QTableWidgetItem (str (j[6]))
                        self.tableWidget.setItem (i, 6, massage6)

                        massage7 = QTableWidgetItem (str (j[7]))
                        self.tableWidget.setItem (i, 7, massage7)

                    self.tableWidget.setVisible (True)
                    self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                    self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                    self.tableWidget.horizontalHeader ().setStyleSheet (
                        'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                    QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                    QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                    self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                    # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                    for x in range (len (results_three)):  # 居中
                        for y in range (8):
                            if y != 1:
                                item = self.tableWidget.item (x, y)
                                item.setTextAlignment (Qt.AlignCenter)
                            else:
                                pass
                    self.tableWidget.setVisible (True)
                    mb = QMessageBox (self)
                    mb.setIcon (QMessageBox.Information)
                    mb.setText ("<h3>查询成功！</h3>")
                    mb.setInformativeText ("点击确定或取消...")
                    mb.setWindowTitle ("查询成功提示")
                    mb.addButton ("确定", QMessageBox.YesRole)
                    mb.addButton ("取消", QMessageBox.NoRole)
                    mb.open ()

            else:
                self.tableWidget.setRowCount (0)
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (
                    ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                print ("无记录！")
                print ("请输入正确的查询条件！")
                mb = QMessageBox (self)
                mb.setIcon (QMessageBox.Warning)
                mb.setText ("<h3>查询失败！</h3>")
                mb.setInformativeText ("无此筛选项数据...")
                mb.setWindowTitle ("查询失败提示")
                mb.addButton ("确定", QMessageBox.YesRole)
                mb.addButton ("取消", QMessageBox.NoRole)
                mb.open ()
        pass

    def progress10(self):# 清空查询groupbox中填写的信息
        self.line2_1.setText("")
        self.rb2_1.setCheckable (False)
        self.rb2_2.setCheckable (False)
        self.rb2_3.setCheckable (False)
        self.rb2_1.setCheckable (True)
        self.rb2_2.setCheckable (True)
        self.rb2_3.setCheckable (True)
        self.combobox2_1.setCurrentIndex (0)
        pass

    def progress11(self):# 更改
        xiang1 = ""
        rb11_ischecked = self.rb3_2_1.isChecked ()
        rb22_ischecked = self.rb3_2_2.isChecked ()
        rb33_ischecked = self.rb3_2_3.isChecked ()
        if rb11_ischecked == True:
            xiang1 = "A"
        elif rb22_ischecked == True:
            xiang1 = "B"
        elif rb33_ischecked == True:
            xiang1 = "C"
        if self.line4_2.text () != ""  and xiang1 != "" and self.line3_2_1.text () != "" :
            access = SunckSql ('localhost', 'root', '123456', 'sunck')
            results = access.Sql_getall (access.sql_update (self.line4_2.text (),self.line3_2_1.text (),xiang1,self.combobox3_2_1.currentText(),self.line3_2_2.text (),self.line3_3_3.text ()))
            if results == ():#未执行此代码
                self.tableWidget.setRowCount (0)
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (
                    ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                print ("无记录！")
            else:
                self.tableWidget.setRowCount (len (results))
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                for i, j in enumerate (results):
                    massage0 = QTableWidgetItem (str (j[0]))
                    self.tableWidget.setItem (i, 0, massage0)

                    massage1 = QTableWidgetItem (str (j[1]))
                    self.tableWidget.setItem (i, 1, massage1)

                    massage2 = QTableWidgetItem (str (j[2]))
                    self.tableWidget.setItem (i, 2, massage2)

                    massage3 = QTableWidgetItem (str (j[3]))
                    self.tableWidget.setItem (i, 3, massage3)

                    massage4 = QTableWidgetItem (str (j[4]))
                    self.tableWidget.setItem (i, 4, massage4)

                    massage5 = QTableWidgetItem (str (j[5]))
                    self.tableWidget.setItem (i, 5, massage5)

                    massage6 = QTableWidgetItem (str (j[6]))
                    self.tableWidget.setItem (i, 6, massage6)

                    massage7 = QTableWidgetItem (str (j[7]))
                    self.tableWidget.setItem (i, 7, massage7)

                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                for x in range (len (results)):  # 居中
                    for y in range (8):
                        if y != 1:
                            item = self.tableWidget.item (x, y)
                            item.setTextAlignment (Qt.AlignCenter)
                        else:
                            pass
                self.tableWidget.setVisible (True)
        pass

    def progress12(self):# 删除
        if self.line4_1.text() == "":
            pass
        else:
            access = SunckSql ('localhost', 'root', '123456', 'sunck')
            results = access.Sql_getall (access.sql_del_xuhao (self.line4_1.text ()))
            if results == ():  #这个代码没有被执行
                self.tableWidget.setRowCount (0)
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (
                    ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                print ("无记录！")
            else:
                self.tableWidget.setRowCount (len (results))
                self.tableWidget.setColumnCount (8)
                font = QFont ('微软雅黑', 10)
                font.setBold (True)  # 设置字体加粗
                self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                self.tableWidget.setHorizontalHeaderLabels (["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                for i, j in enumerate (results):
                    massage0 = QTableWidgetItem (str (j[0]))
                    self.tableWidget.setItem (i, 0, massage0)

                    massage1 = QTableWidgetItem (str (j[1]))
                    self.tableWidget.setItem (i, 1, massage1)

                    massage2 = QTableWidgetItem (str (j[2]))
                    self.tableWidget.setItem (i, 2, massage2)

                    massage3 = QTableWidgetItem (str (j[3]))
                    self.tableWidget.setItem (i, 3, massage3)

                    massage4 = QTableWidgetItem (str (j[4]))
                    self.tableWidget.setItem (i, 4, massage4)

                    massage5 = QTableWidgetItem (str (j[5]))
                    self.tableWidget.setItem (i, 5, massage5)

                    massage6 = QTableWidgetItem (str (j[6]))
                    self.tableWidget.setItem (i, 6, massage6)

                    massage7 = QTableWidgetItem (str (j[7]))
                    self.tableWidget.setItem (i, 7, massage7)

                self.tableWidget.setVisible (True)
                self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                self.tableWidget.horizontalHeader ().setStyleSheet (
                    'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                self.tableWidget.horizontalHeader ().setSectionResizeMode (7, QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                for x in range (len (results)):  # 居中
                    for y in range (8):
                        if y != 1:
                            item = self.tableWidget.item (x, y)
                            item.setTextAlignment (Qt.AlignCenter)
                        else:
                            pass
                self.tableWidget.setVisible (True)
        pass

    def progress13(self):# 全部删除
        mb = QMessageBox (self)
        mb.setIcon (QMessageBox.Warning)
        mb.setText ("<h3>将清空数据库！</h3>")
        mb.setInformativeText ("请确认是否清空")
        # mb.setCheckBox (QCheckBox ("下次不再提醒", mb))
        mb.setWindowTitle ("全部删除警告")
        mb.setDetailedText ("全部删除将清空整个数据库，请慎重操作...")
        btn1 = mb.addButton ("确认", QMessageBox.YesRole)
        btn2 = mb.addButton ("取消", QMessageBox.NoRole)

        def test(btn):
            if btn == btn1:
                print ("点击了确认")
                access = SunckSql ('localhost', 'root', '123456', 'sunck')
                results = access.Sql_getall (access.sql_del_all ())
                if results == ():
                    self.tableWidget.setRowCount (0)
                    self.tableWidget.setColumnCount (8)
                    font = QFont ('微软雅黑', 10)
                    font.setBold (True)  # 设置字体加粗
                    self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                    self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                    self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                    self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                    # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                    self.tableWidget.setHorizontalHeaderLabels (
                        ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                    print ("无记录！")
                else:
                    self.tableWidget.setRowCount (len (results))
                    self.tableWidget.setColumnCount (8)
                    font = QFont ('微软雅黑', 10)
                    font.setBold (True)  # 设置字体加粗
                    self.tableWidget.horizontalHeader ().setFont (font)  # 设置表头字体
                    self.tableWidget.horizontalHeader ().setFixedHeight (40)  ##设置表头高度
                    self.tableWidget.horizontalHeader ().setSectionsClickable (False)  # 可以禁止点击表头的列
                    self.tableWidget.horizontalHeader ().resizeSection (0, 150)
                    # self.tableWidget.setFrameShape (QFrame.NoFrame)  ##设置无表格的外框
                    self.tableWidget.setHorizontalHeaderLabels (
                        ["序号", "时间", "编号", "次数", "峰值带/Hz", "备注（1）", "备注（3）", "地址"])
                    for i, j in enumerate (results):
                        massage0 = QTableWidgetItem (str (j[0]))
                        self.tableWidget.setItem (i, 0, massage0)

                        massage1 = QTableWidgetItem (str (j[1]))
                        self.tableWidget.setItem (i, 1, massage1)

                        massage2 = QTableWidgetItem (str (j[2]))
                        self.tableWidget.setItem (i, 2, massage2)

                        massage3 = QTableWidgetItem (str (j[3]))
                        self.tableWidget.setItem (i, 3, massage3)

                        massage4 = QTableWidgetItem (str (j[4]))
                        self.tableWidget.setItem (i, 4, massage4)

                        massage5 = QTableWidgetItem (str (j[5]))
                        self.tableWidget.setItem (i, 5, massage5)

                        massage6 = QTableWidgetItem (str (j[6]))
                        self.tableWidget.setItem (i, 6, massage6)

                        massage7 = QTableWidgetItem (str (j[7]))
                        self.tableWidget.setItem (i, 7, massage7)

                    self.tableWidget.setVisible (True)
                    self.tableWidget.horizontalHeader ().setStretchLastSection (True)  # 设置最后一列拉伸至最大
                    self.tableWidget.horizontalHeader ().setStyleSheet (
                        'QHeaderView::section{background:green}')  # 设置表头的背景色为绿色
                    QTableWidget.resizeColumnsToContents (self.tableWidget)  # 设置列宽高按照内容自适应
                    self.tableWidget.horizontalHeader ().setSectionResizeMode (7,
                                                                               QHeaderView.Stretch)  # 设置第五列宽度自动调整，充满屏幕
                    QTableWidget.resizeRowsToContents (self.tableWidget)  # 设置行宽和高按照内容自适应
                    self.tableWidget.setSelectionBehavior (QAbstractItemView.SelectRows)  # 不能选第一列
                    # self.tableWidget.horizontalHeader ().setSectionResizeMode (QHeaderView.Stretch)  # 列不能拉伸
                    for x in range (len (results)):  # 居中
                        for y in range (8):
                            if y != 1:
                                item = self.tableWidget.item (x, y)
                                item.setTextAlignment (Qt.AlignCenter)
                            else:
                                pass
                    self.tableWidget.setVisible (True)
            else:
                print ("点击了取消")
        mb.buttonClicked.connect (test)
        mb.open ()
        pass

    def progress14(self):   #关于
        mb = QMessageBox (self)
        mb.setIcon (QMessageBox.Information)
        mb.setText ("<h3>分体式瓷支柱绝缘子桌面处理程序</h3>")
        mb.setInformativeText ("如有疑问请联系：270043245@qq.com \n版权所有：华北电力大学（保定） \n版本 ：Version1.0")
        mb.setWindowTitle ("关于")
        mb.addButton ("确定", QMessageBox.YesRole)
        mb.addButton ("取消", QMessageBox.NoRole)
        mb.open ()
        pass


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window1=Window1()
    window1.show()
    window2 = Window2 ()
    def add1():
        window1.close()
        window2.show()
    sys.exit(app.exec_())

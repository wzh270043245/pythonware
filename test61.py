# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test61.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1119, 668)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xxx.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))")
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(20, 80, 151, 41))
        self.button1.setStyleSheet("\n"
"")
        self.button1.setObjectName("button1")
        self.pyqtgraph1 = GraphicsLayoutWidget(Form)
        self.pyqtgraph1.setGeometry(QtCore.QRect(190, 102, 901, 531))
        self.pyqtgraph1.setStyleSheet("border:1px solid rgb(90,214,231)")
        self.pyqtgraph1.setObjectName("pyqtgraph1")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(190, 30, 901, 91))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button2 = QtWidgets.QPushButton(self.layoutWidget)
        self.button2.setObjectName("button2")
        self.horizontalLayout.addWidget(self.button2)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.button3 = QtWidgets.QPushButton(self.layoutWidget)
        self.button3.setObjectName("button3")
        self.horizontalLayout.addWidget(self.button3)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.button4 = QtWidgets.QPushButton(self.layoutWidget)
        self.button4.setObjectName("button4")
        self.horizontalLayout.addWidget(self.button4)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.button5 = QtWidgets.QPushButton(self.layoutWidget)
        self.button5.setObjectName("button5")
        self.horizontalLayout.addWidget(self.button5)
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 151, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.button1.clicked.connect(Form.progress1)
        self.button3.clicked.connect(Form.progress3)
        self.button4.clicked.connect(Form.progress4)
        self.button5.clicked.connect(Form.progress5)
        self.button2.clicked.connect(Form.progress2)
        self.pushButton.clicked.connect(Form.progress6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像处理程序"))
        self.button1.setText(_translate("Form", "打开"))
        self.button2.setText(_translate("Form", "时域图像"))
        self.button3.setText(_translate("Form", "频域图像"))
        self.button4.setText(_translate("Form", "滤波后频域图像"))
        self.button5.setText(_translate("Form", "语谱图像"))
        self.pushButton.setText(_translate("Form", "保存图片"))

from pyqtgraph import GraphicsLayoutWidget

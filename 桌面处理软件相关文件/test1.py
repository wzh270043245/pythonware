# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

###########################################
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
############################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(190, 280, 191, 71))
        self.pushButton1.setObjectName("pushButton1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setEnabled(False)
        self.label1.setGeometry(QtCore.QRect(300, 130, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(590, 280, 191, 71))
        self.pushButton2.setObjectName("pushButton2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

############################################
        self.label1.setVisible(False)
        self.label1.setEnabled (True)
        self.c()
        # self.pushButton1.clicked.connect (self.a)
        # self.pushButton2.clicked.connect (self.b)
    def c(self):
        self.pushButton1.clicked.connect (self.a)
        self.pushButton2.clicked.connect (self.b)
    def a(self):
        address = "C:\\Users\\wzh\\Desktop\\000001.Wav"
        # self.label1.setEnabled(True)
        self.label1.setVisible (True)
        self.label1.setText(address)
    def b(self):
        # self.label1.setText ("")
        # self.label1.setEnabled (False)
        self.label1.setVisible (False)

############################################




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "点击输出WAV文件地址"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton2.setText(_translate("MainWindow", "不显示"))


if __name__ == '__main__':
    app = QApplication (sys.argv)  # 引入主程序
    mainWindow = QMainWindow ()  # 创建窗口
    ui = Ui_MainWindow ()  # 将ui生成的py文件在程序中创建
    ui.setupUi (mainWindow)  # 在程序中开始ui文件的窗口
    mainWindow.show ()  # 显示窗口
    sys.exit (app.exec_ ())  # 窗口的循环

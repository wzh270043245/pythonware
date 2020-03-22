# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1239, 696)
        Form.setAutoFillBackground(True)
        self.pyqtgraph1 = GraphicsLayoutWidget(Form)
        self.pyqtgraph1.setGeometry(QtCore.QRect(10, 200, 371, 241))
        self.pyqtgraph1.setObjectName("pyqtgraph1")
        self.pyqtgraph2 = GraphicsLayoutWidget(Form)
        self.pyqtgraph2.setGeometry(QtCore.QRect(410, 100, 351, 231))
        self.pyqtgraph2.setObjectName("pyqtgraph2")
        self.pyqtgraph3 = GraphicsLayoutWidget(Form)
        self.pyqtgraph3.setGeometry(QtCore.QRect(810, 90, 341, 221))
        self.pyqtgraph3.setObjectName("pyqtgraph3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 40, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 40, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 30, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 330, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pyqtgraph3_2 = GraphicsLayoutWidget(Form)
        self.pyqtgraph3_2.setGeometry(QtCore.QRect(740, 390, 391, 241))
        self.pyqtgraph3_2.setObjectName("pyqtgraph3_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.progress1)
        self.pushButton_2.clicked.connect(Form.progress2)
        self.pushButton_3.clicked.connect(Form.progress3)
        self.pushButton_4.clicked.connect(Form.progress4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "时域图像"))
        self.pushButton_2.setText(_translate("Form", "频域图像"))
        self.pushButton_3.setText(_translate("Form", "滤波后频域图像"))
        self.pushButton_4.setText(_translate("Form", "语谱图像"))

from pyqtgraph import GraphicsLayoutWidget

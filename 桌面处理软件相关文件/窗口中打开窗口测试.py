# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '窗口中打开窗口测试.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(628, 434)
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(130, 230, 75, 23))
        self.button1.setObjectName("button1")

        self.retranslateUi(Form)
        self.button1.clicked.connect(Form.progress1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button1.setText(_translate("Form", "PushButton"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test7.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1101, 543)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(250, 10, 841, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 70, 135, 359))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button1 = QtWidgets.QPushButton(self.widget)
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        self.line1 = QtWidgets.QLineEdit(self.widget)
        self.line1.setObjectName("line1")
        self.verticalLayout.addWidget(self.line1)
        self.line2 = QtWidgets.QLineEdit(self.widget)
        self.line2.setObjectName("line2")
        self.verticalLayout.addWidget(self.line2)
        self.line3 = QtWidgets.QLineEdit(self.widget)
        self.line3.setObjectName("line3")
        self.verticalLayout.addWidget(self.line3)
        self.line4 = QtWidgets.QLineEdit(self.widget)
        self.line4.setObjectName("line4")
        self.verticalLayout.addWidget(self.line4)
        self.button2 = QtWidgets.QPushButton(self.widget)
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2)

        self.retranslateUi(Form)
        self.button1.clicked.connect(Form.progress1)
        self.button2.clicked.connect(Form.progress2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button1.setText(_translate("Form", "历史记录"))
        self.button2.setText(_translate("Form", "存储"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test81.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1593, 881)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xxx.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pyqtgraph1 = GraphicsLayoutWidget(Form)
        self.pyqtgraph1.setGeometry(QtCore.QRect(276, 130, 1271, 701))
        self.pyqtgraph1.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pyqtgraph1.setObjectName("pyqtgraph1")
        self.tableWidget = QtWidgets.QTableWidget(self.pyqtgraph1)
        self.tableWidget.setGeometry(QtCore.QRect(-1, -1, 1271, 701))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget1 = QtWidgets.QWidget(self.pyqtgraph1)
        self.widget1.setGeometry(QtCore.QRect(300, 210, 661, 271))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.widget1.setPalette(palette)
        self.widget1.setObjectName("widget1")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget1)
        self.layoutWidget_2.setGeometry(QtCore.QRect(197, 209, 261, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button71 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.button71.setFont(font)
        self.button71.setObjectName("button71")
        self.horizontalLayout_2.addWidget(self.button71)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button72 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.button72.setFont(font)
        self.button72.setObjectName("button72")
        self.horizontalLayout_2.addWidget(self.button72)
        self.groupBox = QtWidgets.QGroupBox(self.widget1)
        self.groupBox.setGeometry(QtCore.QRect(196, 17, 261, 151))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(2, 13, 251, 131))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label1 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.line1 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rb1 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_3.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_3.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_3.addWidget(self.rb3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.label2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 2, 1, 1)
        self.label3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)
        self.combobox1 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.combobox1.setObjectName("combobox1")
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.gridLayout.addWidget(self.combobox1, 2, 1, 1, 1)
        self.label4 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 2, 2, 1, 1)
        self.layoutWidget_4 = QtWidgets.QWidget(self.widget1)
        self.layoutWidget_4.setGeometry(QtCore.QRect(196, 171, 261, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label1_2 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.horizontalLayout_4.addWidget(self.label1_2)
        self.line2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.line2.setFont(font)
        self.line2.setObjectName("line2")
        self.horizontalLayout_4.addWidget(self.line2)
        self.label1_3 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label1_3.setFont(font)
        self.label1_3.setObjectName("label1_3")
        self.horizontalLayout_4.addWidget(self.label1_3)
        self.line3 = QtWidgets.QLineEdit(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.line3.setFont(font)
        self.line3.setObjectName("line3")
        self.horizontalLayout_4.addWidget(self.line3)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 140, 181, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.button7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.verticalLayout.addWidget(self.button7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.button6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.verticalLayout.addWidget(self.button6)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(706, 100, 411, 20))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 10, 1141, 91))
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

        self.retranslateUi(Form)
        self.button1.clicked.connect(Form.progress1)
        self.button3.clicked.connect(Form.progress3)
        self.button4.clicked.connect(Form.progress4)
        self.button5.clicked.connect(Form.progress5)
        self.button2.clicked.connect(Form.progress2)
        self.button6.clicked.connect(Form.progress6)
        self.button7.clicked.connect(Form.progress7)
        self.button71.clicked.connect(Form.progress8)
        self.button72.clicked.connect(Form.progress9)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像处理程序"))
        self.button71.setText(_translate("Form", "保存"))
        self.button72.setText(_translate("Form", "取消"))
        self.groupBox.setTitle(_translate("Form", "保存选项"))
        self.label1.setText(_translate("Form", "隔离开关编号："))
        self.label_2.setText(_translate("Form", "号"))
        self.label_3.setText(_translate("Form", "            第"))
        self.rb1.setText(_translate("Form", "A"))
        self.rb2.setText(_translate("Form", "B"))
        self.rb3.setText(_translate("Form", "C"))
        self.label2.setText(_translate("Form", "相"))
        self.label3.setText(_translate("Form", "            第"))
        self.combobox1.setItemText(0, _translate("Form", "1"))
        self.combobox1.setItemText(1, _translate("Form", "2"))
        self.combobox1.setItemText(2, _translate("Form", "3"))
        self.label4.setText(_translate("Form", "支"))
        self.label1_2.setText(_translate("Form", "备注1："))
        self.label1_3.setText(_translate("Form", "备注2："))
        self.button1.setText(_translate("Form", "打开"))
        self.button7.setText(_translate("Form", "保存"))
        self.button6.setText(_translate("Form", "历史记录"))
        self.button2.setText(_translate("Form", "时域图像"))
        self.button3.setText(_translate("Form", "频域图像"))
        self.button4.setText(_translate("Form", "滤波后频域图像"))
        self.button5.setText(_translate("Form", "语谱图像"))

from pyqtgraph import GraphicsLayoutWidget

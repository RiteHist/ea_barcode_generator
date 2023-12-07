# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 100))
        MainWindow.setMaximumSize(QtCore.QSize(400, 100))
        MainWindow.setBaseSize(QtCore.QSize(400, 100))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.num_to_print_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.num_to_print_label.setObjectName("num_to_print_label")
        self.gridLayout.addWidget(self.num_to_print_label, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setGeometry(QtCore.QRect(0, 10, 192, 30))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.print_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.print_btn.setObjectName("print_btn")
        self.gridLayout.addWidget(self.print_btn, 2, 1, 1, 1)
        self.num_to_print_box = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.num_to_print_box.setFrame(True)
        self.num_to_print_box.setMinimum(1)
        self.num_to_print_box.setMaximum(10000)
        self.num_to_print_box.setObjectName("num_to_print_box")
        self.gridLayout.addWidget(self.num_to_print_box, 2, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Print Barcode"))
        self.num_to_print_label.setText(_translate("MainWindow", "Number to print:"))
        self.print_btn.setText(_translate("MainWindow", "PRINT IT"))
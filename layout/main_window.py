# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ShirokovAV\Documents\Dev\ea_barcode_generator\layout\layout.ui'
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
        MainWindow.resize(300, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 160))
        MainWindow.setMaximumSize(QtCore.QSize(300, 160))
        MainWindow.setBaseSize(QtCore.QSize(400, 100))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.code_num_box = QtWidgets.QSpinBox(self.centralwidget)
        self.code_num_box.setMinimum(1)
        self.code_num_box.setMaximum(999999)
        self.code_num_box.setObjectName("code_num_box")
        self.gridLayout.addWidget(self.code_num_box, 10, 0, 1, 1)
        self.code_label = QtWidgets.QLabel(self.centralwidget)
        self.code_label.setObjectName("code_label")
        self.gridLayout.addWidget(self.code_label, 6, 0, 1, 1)
        self.num_to_print_label = QtWidgets.QLabel(self.centralwidget)
        self.num_to_print_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.num_to_print_label.setObjectName("num_to_print_label")
        self.gridLayout.addWidget(self.num_to_print_label, 1, 0, 1, 1)
        self.code_num_label = QtWidgets.QLabel(self.centralwidget)
        self.code_num_label.setObjectName("code_num_label")
        self.gridLayout.addWidget(self.code_num_label, 9, 0, 1, 1)
        self.num_to_print_box = QtWidgets.QSpinBox(self.centralwidget)
        self.num_to_print_box.setFrame(True)
        self.num_to_print_box.setMinimum(1)
        self.num_to_print_box.setMaximum(1000)
        self.num_to_print_box.setObjectName("num_to_print_box")
        self.gridLayout.addWidget(self.num_to_print_box, 5, 0, 1, 1)
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_btn.setObjectName("print_btn")
        self.gridLayout.addWidget(self.print_btn, 8, 1, 1, 1)
        self.code_text = QtWidgets.QLineEdit(self.centralwidget)
        self.code_text.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.code_text.setObjectName("code_text")
        self.gridLayout.addWidget(self.code_text, 8, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Print Barcode"))
        self.code_label.setText(_translate("MainWindow", "Код площадки:"))
        self.num_to_print_label.setText(_translate("MainWindow", "Количество этикеток:"))
        self.code_num_label.setText(_translate("MainWindow", "Номер штрихкода:"))
        self.print_btn.setText(_translate("MainWindow", "ПЕЧАТЬ"))

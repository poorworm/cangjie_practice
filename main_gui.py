# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 494)
        font = QtGui.QFont()
        font.setFamily("細明體")
        font.setPointSize(150)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(590, 410, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        self.lbWord = QtWidgets.QLabel(self.centralwidget)
        self.lbWord.setGeometry(QtCore.QRect(50, 30, 381, 341))
        self.lbWord.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.lbWord.setAlignment(QtCore.Qt.AlignCenter)
        self.lbWord.setObjectName("lbWord")
        self.textInput = QtWidgets.QLineEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(520, 60, 221, 241))
        self.textInput.setObjectName("textInput")
        self.btnNextWord = QtWidgets.QPushButton(self.centralwidget)
        self.btnNextWord.setGeometry(QtCore.QRect(620, 330, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnNextWord.setFont(font)
        self.btnNextWord.setObjectName("btnNextWord")
        self.lbCodes = QtWidgets.QLabel(self.centralwidget)
        self.lbCodes.setGeometry(QtCore.QRect(150, 410, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lbCodes.setFont(font)
        self.lbCodes.setObjectName("lbCodes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "輸入法練習"))
        self.btnClose.setText(_translate("MainWindow", "離開"))
        self.lbWord.setText(_translate("MainWindow", "?"))
        self.btnNextWord.setText(_translate("MainWindow", "下一題"))
        self.lbCodes.setText(_translate("MainWindow", "????"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy import create_engine

from main_gui import Ui_MainWindow

DB_FILE = 'sqlite:///data\\cj.db'


class Ui_MainWindow_Sub(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.chk_word = ''      # 文字
        self.chk_code = ''      # 答案

    def set_word(self):
        self.chk_word, self.chk_code = self.get_one_word()
        self.lbWord.setText(self.chk_word)
        self.lbCodes.setText(self.chk_code)

    def get_one_word(self):
        db = create_engine(DB_FILE)
        db.echo = False  # True to see what happens

        codes = db.execute('SELECT * FROM codes')
        cnt = db.execute('SELECT COUNT(*) FROM codes').scalar()

        r = random.randint(1, cnt)

        chk_code = ''
        chk_word = ''

        # 查找
        idx = 0
        for _r in codes:
            if idx == r:
                chk_code = _r['code']
                chk_word = _r['word']
                print(_r['code'])
                print(_r['word'])
                return chk_word, chk_code
            idx += 1

    def on_click_close(self):
        sys.exit(0)

    def on_text_changed(self):
        print(self.textInput.text())
        new_word = self.textInput.text()

        # 如果比對是一樣的，題目就換成新的字
        if self.chk_word == new_word:
            # 下一題
            self.set_word()
        else:
            print("Not Match")

        self.textInput.clear()

    def on_next_word(self):
        self.textInput.clear()
        self.set_word()
        self.textInput.setFocus()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnClose.clicked.connect(self.on_click_close)
        self.btnNextWord.clicked.connect(self.on_next_word)
        self.textInput.editingFinished.connect(self.on_text_changed)
        # 啟動時先選一個字
        self.set_word()


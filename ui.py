#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QComboBox, QCheckBox, QApplication, QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QRadioButton)
from PyQt5.QtGui import QFont
import rail
import save

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('my window')
        self.setGeometry(300, 300, 1000 , 1000)

        formlayout = QFormLayout()
        self.setLayout(formlayout)

        self.browserlabel = QLabel('瀏覽器:', self)
        self.browser = QComboBox(self)
        self.browser.addItems(['Chrome', 'Firefox'])
        formlayout.addRow(self.browserlabel, self.browser)

        self.idCardlabel = QLabel('身分證字號:', self)
        self.idCard = QLineEdit(self)
        formlayout.addRow(self.idCardlabel, self.idCard)

        self.startStationlabel = QLabel('起始站:', self)
        self.startStation = QLineEdit(self)
        formlayout.addRow(self.startStationlabel, self.startStation)

        self.endStationLabel = QLabel('終點站:', self)
        self.endStation = QLineEdit(self)
        formlayout.addRow(self.endStationLabel, self.endStation)

        self.onewaySelect = QRadioButton('單程票', self)
        self.onewaySelect.setChecked(True)
        self.roundtripSelect = QRadioButton('來回票', self)
        formlayout.addRow(self.onewaySelect, self.roundtripSelect)

        self.ticketNumLabel = QLabel('張數:', self)
        self.ticketNum = QLineEdit(self)
        formlayout.addRow(self.ticketNumLabel, self.ticketNum)

        self.toLabel = QLabel('去程', self)
        formlayout.addRow(self.toLabel)

        self.date1Label = QLabel('日期:', self)
        self.date1 = QLineEdit(self)
        formlayout.addRow(self.date1Label, self.date1)

        self.trainNumber1Label = QLabel('班次:', self)
        self.trainNumber1 = QLineEdit(self)
        formlayout.addRow(self.trainNumber1Label, self.trainNumber1)

        self.fromLabel = QLabel('回程', self)
        formlayout.addRow(self.fromLabel)

        self.date2Label = QLabel('日期:', self)
        self.date2 = QLineEdit(self)
        formlayout.addRow(self.date2Label, self.date2)

        self.trainNumber2Label = QLabel('班次:', self)
        self.trainNumber2 = QLineEdit(self)
        formlayout.addRow(self.trainNumber2Label, self.trainNumber2)

        self.testSelect = QCheckBox('測試', self)
        self.autoSelect = QCheckBox('自動送出', self)
        formlayout.addRow(self.testSelect, self.autoSelect)

        self.messageLabel = QLabel('', self)
        self.messageLabel.resize(500,100)
        formlayout.addRow(self.messageLabel)

        self.mybutton = QPushButton('開始搶票', self)
        formlayout.addRow(self.mybutton)
        self.mybutton.clicked.connect(self.luckyBallGO)

        save.load_data(self)

    def luckyBallGO(self):
        self.messageLabel.setText("Lucky ball GO!!!")
        rail.get_web(self)
        save.save_data(self)

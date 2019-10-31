# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bigdemo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BigDemo(object):
    def setupUi(self, BigDemo):
        BigDemo.setObjectName("BigDemo")
        BigDemo.resize(601, 349)
        self.centralwidget = QtWidgets.QWidget(BigDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_vi = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_vi.setObjectName("radio_vi")
        self.verticalLayout.addWidget(self.radio_vi)
        self.radio_emacs = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_emacs.setObjectName("radio_emacs")
        self.verticalLayout.addWidget(self.radio_emacs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.le_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_name.setObjectName("le_name")
        self.horizontalLayout.addWidget(self.le_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.button_go = QtWidgets.QPushButton(self.centralwidget)
        self.button_go.setObjectName("button_go")
        self.gridLayout.addWidget(self.button_go, 1, 0, 1, 1)
        BigDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BigDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        BigDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BigDemo)
        self.statusbar.setObjectName("statusbar")
        BigDemo.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(BigDemo)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(BigDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(BigDemo)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(BigDemo)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(BigDemo)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(BigDemo)
        QtCore.QMetaObject.connectSlotsByName(BigDemo)

    def retranslateUi(self, BigDemo):
        _translate = QtCore.QCoreApplication.translate
        BigDemo.setWindowTitle(_translate("BigDemo", "MainWindow"))
        self.radio_vi.setText(_translate("BigDemo", "vi"))
        self.radio_emacs.setText(_translate("BigDemo", "emacs"))
        self.label_name.setText(_translate("BigDemo", "Name:"))
        self.button_go.setText(_translate("BigDemo", "GO"))
        self.menuFile.setTitle(_translate("BigDemo", "File"))
        self.menuEdit.setTitle(_translate("BigDemo", "Edit"))
        self.actionOpen.setText(_translate("BigDemo", "Open..."))
        self.actionQuit.setText(_translate("BigDemo", "Quit"))
        self.actionCut.setText(_translate("BigDemo", "Cut"))
        self.actionCopy.setText(_translate("BigDemo", "Copy"))
        self.actionPaste.setText(_translate("BigDemo", "Paste"))


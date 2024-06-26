# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Harry\Documents\GitHub\myourapi\Client.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(599, 467)
        self.verticalLayout = QtWidgets.QVBoxLayout(Client)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.functionButton = QtWidgets.QPushButton(Client)
        self.functionButton.setObjectName("functionButton")
        self.horizontalLayout.addWidget(self.functionButton)
        self.variableButton = QtWidgets.QPushButton(Client)
        self.variableButton.setObjectName("variableButton")
        self.horizontalLayout.addWidget(self.variableButton)
        self.resetButton = QtWidgets.QPushButton(Client)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.runButton = QtWidgets.QPushButton(Client)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("LM Mono Caps 10")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.urlText = QtWidgets.QLabel(Client)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(14)
        self.urlText.setFont(font)
        self.urlText.setObjectName("urlText")
        self.horizontalLayout_2.addWidget(self.urlText)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.functionText = QtWidgets.QPlainTextEdit(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.functionText.sizePolicy().hasHeightForWidth())
        self.functionText.setSizePolicy(sizePolicy)
        self.functionText.setMinimumSize(QtCore.QSize(200, 60))
        self.functionText.setMaximumSize(QtCore.QSize(400, 60))
        self.functionText.setObjectName("functionText")
        self.gridLayout.addWidget(self.functionText, 1, 0, 1, 1)
        self.results = QtWidgets.QTreeWidget(Client)
        self.results.setObjectName("results")
        self.results.headerItem().setText(0, "1")
        self.results.header().setVisible(False)
        self.gridLayout.addWidget(self.results, 1, 1, 3, 1)
        self.label_4 = QtWidgets.QLabel(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        self.label_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.variablesText = QtWidgets.QPlainTextEdit(Client)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variablesText.sizePolicy().hasHeightForWidth())
        self.variablesText.setSizePolicy(sizePolicy)
        self.variablesText.setMinimumSize(QtCore.QSize(200, 0))
        self.variablesText.setMaximumSize(QtCore.QSize(400, 16777215))
        self.variablesText.setObjectName("variablesText")
        self.gridLayout.addWidget(self.variablesText, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "Dialog"))
        self.functionButton.setText(_translate("Client", "Set Function"))
        self.variableButton.setText(_translate("Client", "Add Variable"))
        self.resetButton.setText(_translate("Client", "Reset"))
        self.runButton.setText(_translate("Client", "Run"))
        self.label.setText(_translate("Client", " URL : "))
        self.urlText.setText(_translate("Client", "/"))
        self.label_3.setText(_translate("Client", "Function"))
        self.label_4.setText(_translate("Client", "Variables"))

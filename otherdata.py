# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otherdata.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(645, 453)
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(16)
        Dialog.setFont(font)
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(170, 30, 281, 16))
        self.name.setText("")
        self.name.setObjectName("name")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(80, 80, 91, 16))
        self.status.setObjectName("status")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 170, 381, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label3.setObjectName("label3")
        self.verticalLayout.addWidget(self.label3)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gnf = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        self.gnf.setFont(font)
        self.gnf.setText("")
        self.gnf.setObjectName("gnf")
        self.verticalLayout_2.addWidget(self.gnf)
        self.abuzer = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        self.abuzer.setFont(font)
        self.abuzer.setText("")
        self.abuzer.setObjectName("abuzer")
        self.verticalLayout_2.addWidget(self.abuzer)
        self.gay = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        self.gay.setFont(font)
        self.gay.setText("")
        self.gay.setObjectName("gay")
        self.verticalLayout_2.addWidget(self.gay)
        self.cursed = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        self.cursed.setFont(font)
        self.cursed.setText("")
        self.cursed.setObjectName("cursed")
        self.verticalLayout_2.addWidget(self.cursed)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 70, 301, 87))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.status.setText(_translate("Dialog", "status"))
        self.label1.setText(_translate("Dialog", "got no friends?"))
        self.label_2.setText(_translate("Dialog", "abuzer?"))
        self.label3.setText(_translate("Dialog", "gay?"))
        self.label.setText(_translate("Dialog", "cursed?"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_banco.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela2(object):
    def setupUi(self, Janela2):
        Janela2.setObjectName("Janela2")
        Janela2.resize(541, 390)
        Janela2.setStyleSheet("\n"
"background-color: rgb(85, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(Janela2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, -70, 391, 211))
        self.label.setStyleSheet("font: 16pt \"Beyond The Mountains\";\n"
"font: 26pt \"Grand Aventure Text\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label_2.setStyleSheet("font: 18pt \"Bahnschrift SemiLight SemiConde\";")
        self.label_2.setObjectName("label_2")
        self.label_Saldo = QtWidgets.QLabel(self.centralwidget)
        self.label_Saldo.setGeometry(QtCore.QRect(130, 50, 241, 31))
        self.label_Saldo.setStyleSheet("font: 18pt \"Verdana\";")
        self.label_Saldo.setText("")
        self.label_Saldo.setObjectName("label_Saldo")
        self.button_FazerDeposito = QtWidgets.QPushButton(self.centralwidget)
        self.button_FazerDeposito.setGeometry(QtCore.QRect(30, 160, 161, 61))
        self.button_FazerDeposito.setStyleSheet("font: 75 16pt \"Reckoner Bold\";\n"
"background-color: rgb(255, 255, 255);")
        self.button_FazerDeposito.setObjectName("button_FazerDeposito")
        self.buttonTransferencia = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTransferencia.setGeometry(QtCore.QRect(30, 230, 161, 61))
        self.buttonTransferencia.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Reckoner Bold\";")
        self.buttonTransferencia.setObjectName("buttonTransferencia")
        self.buttonSacar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSacar.setGeometry(QtCore.QRect(30, 300, 161, 61))
        self.buttonSacar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Reckoner Bold\";")
        self.buttonSacar.setObjectName("buttonSacar")
        self.inputValor = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValor.setGeometry(QtCore.QRect(20, 110, 181, 41))
        self.inputValor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputValor.setObjectName("inputValor")
        self.label_DeErro = QtWidgets.QLabel(self.centralwidget)
        self.label_DeErro.setGeometry(QtCore.QRect(210, 180, 321, 131))
        self.label_DeErro.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.label_DeErro.setText("")
        self.label_DeErro.setObjectName("label_DeErro")
        self.button_verSaldo = QtWidgets.QPushButton(self.centralwidget)
        self.button_verSaldo.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.button_verSaldo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_verSaldo.setObjectName("button_verSaldo")
        Janela2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela2)
        QtCore.QMetaObject.connectSlotsByName(Janela2)

    def retranslateUi(self, Janela2):
        _translate = QtCore.QCoreApplication.translate
        Janela2.setWindowTitle(_translate("Janela2", "BANCO GUEEG GAMING"))
        self.label.setText(_translate("Janela2", "Bem vindo ao Sistema de Banco GG"))
        self.label_2.setText(_translate("Janela2", "SEU SALDO:"))
        self.button_FazerDeposito.setText(_translate("Janela2", "FAZER DEPOSITO"))
        self.buttonTransferencia.setText(_translate("Janela2", "FAZER TRANSFERENCIA"))
        self.buttonSacar.setText(_translate("Janela2", "SACAR"))
        self.button_verSaldo.setText(_translate("Janela2", "VER SALDO"))

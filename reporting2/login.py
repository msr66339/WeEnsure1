# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_self(QMainWindow):
    def setupUi(self):
        super(Ui_self, self).setupUi()
        self.setObjectName("self")
        self.resize(480, 620)
        self.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(190, 50, 121, 71))
        self.label.setStyleSheet("color:rgb(225, 225, 225); font-size:28pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 101, 31))
        self.label_2.setStyleSheet("font-size:15pt; color:rgb(255, 0, 127)")
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(self)
        self.email.setGeometry(QtCore.QRect(170, 150, 241, 51))
        self.email.setStyleSheet("font-size:14pt; color:rgb(243, 243, 243)")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(QtCore.QRect(170, 260, 241, 51))
        self.password.setStyleSheet("font-size:14pt; color:rgb(243, 243, 243)")
        self.password.setText("")
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(40, 270, 111, 31))
        self.label_3.setStyleSheet("font-size:15pt; color:rgb(255, 0, 127)")
        self.label_3.setObjectName("label_3")
        self.loginbutton = QtWidgets.QPushButton(self)
        self.loginbutton.setGeometry(QtCore.QRect(270, 390, 141, 41))
        self.loginbutton.setStyleSheet("background-color: rgb(167, 168, 167); font-size:14pt; color:rgb(255, 255, 255)")
        self.loginbutton.setObjectName("loginbutton")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(180, 350, 171, 16))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.createaccbutton = QtWidgets.QPushButton(self)
        self.createaccbutton.setGeometry(QtCore.QRect(320, 340, 93, 28))
        self.createaccbutton.setStyleSheet("color:rgb(255, 255, 255)")
        self.createaccbutton.setObjectName("createaccbutton")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "Login"))
        self.label_2.setText(_translate("self", "Email"))
        self.label_3.setText(_translate("self", "Password"))
        self.loginbutton.setText(_translate("self", "Login"))
        self.label_4.setText(_translate("self", "Don\'t have an account?"))
        self.createaccbutton.setText(_translate("self", "Create Account"))

if __name__ == "__main__":
    window=Ui_self()
    window.show()

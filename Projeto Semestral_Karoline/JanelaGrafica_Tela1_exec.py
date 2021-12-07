# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JanelaGrafica_Tela1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 477)
        Form.setStyleSheet("QFrame\n"
"{\n"
"background: #7FFFD4\n"
"}\n"
"\n"
"#Form\n"
"{\n"
"background: url(:/images/Foto Ruas.jpg);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(170, 255, 255);\n"
"border: none;\n"
"padding-top: 5px;\n"
"color:rgb(85, 255, 255)\n"
"border-left: 1px solid rgb(85, 255, 255);\n"
"border-right: 1px solid rgb(85, 255, 255);\n"
"border-bottom: 5px solid rgb(85, 255, 255);\n"
"}\n"
"")
        self.Fundo_verde = QtWidgets.QFrame(Form)
        self.Fundo_verde.setEnabled(True)
        self.Fundo_verde.setGeometry(QtCore.QRect(60, 250, 491, 171))
        self.Fundo_verde.setStyleSheet("border-radius: 10px;")
        self.Fundo_verde.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fundo_verde.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fundo_verde.setObjectName("Fundo_verde")
        self.BemVindo = QtWidgets.QLabel(self.Fundo_verde)
        self.BemVindo.setGeometry(QtCore.QRect(90, 40, 307, 25))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BemVindo.setFont(font)
        self.BemVindo.setObjectName("BemVindo")
        self.CarregarAba = QtWidgets.QLabel(self.Fundo_verde)
        self.CarregarAba.setGeometry(QtCore.QRect(70, 90, 354, 22))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.CarregarAba.setFont(font)
        self.CarregarAba.setObjectName("CarregarAba")
        self.Next = QtWidgets.QPushButton(self.Fundo_verde)
        self.Next.setGeometry(QtCore.QRect(220, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Next.setFont(font)
        self.Next.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(119, 239, 197);\n"
"border:none;\n"
"padding-top: 5px;\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-bottom-color: 5px solid rgb(85, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(58, 174, 179);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-bottom-color: 5px solid rgb(85, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 218, 178);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-top: 5px solid rgb(85, 255, 255);\n"
"border-bottom: none;\n"
"}\n"
"\n"
"")
        self.Next.setObjectName("Next")
        self.Logo = QtWidgets.QFrame(Form)
        self.Logo.setGeometry(QtCore.QRect(120, 40, 391, 171))
        self.Logo.setStyleSheet("image: url(:/images/Logo-removebg-preview.png);\n"
"background-color: transparent;\n"
"border:none;")
        self.Logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logo.setObjectName("Logo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.BemVindo.setText(_translate("Form", "Seja bem-vindo ao RoadClass"))
        self.CarregarAba.setText(_translate("Form", "Carregue seu arquivo na próxima aba"))
        self.Next.setText(_translate("Form", "Next"))

#import teste_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


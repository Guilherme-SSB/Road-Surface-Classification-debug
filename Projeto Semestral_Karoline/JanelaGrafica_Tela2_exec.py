# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JanelaGrafica_Tela2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(494, 416)
        Form.setStyleSheet("#Form\n"
"{\n"
"background-image: url(:/images/Foto_Rua.jpg);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(114, 229, 189);\n"
"border: none;\n"
"padding-top: 5px;\n"
"color: rgb(49, 98, 81);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-left: 1px solid rgb(88, 177, 146);\n"
"border-right: 1px solid rgb(88, 177, 146);\n"
"border-bottom: 3px solid rgb(88, 177, 146);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(58, 174, 179);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-bottom-color: 3px solid rgb(85, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 218, 178);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-top: 3px solid rgb(85, 255, 255);\n"
"border-bottom: none;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QToolButton{\n"
"background-color: rgb(114, 229, 189);\n"
"border: none;\n"
"padding-top: 5px;\n"
"color: rgb(49, 98, 81);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-left: 1px solid rgb(88, 177, 146);\n"
"border-right: 1px solid rgb(88, 177, 146);\n"
"border-bottom: 3px solid rgb(88, 177, 146);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgb(58, 174, 179);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-bottom-color: 3px solid rgb(85, 255, 255);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color: rgb(108, 218, 178);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-top: 3px solid rgb(85, 255, 255);\n"
"border-bottom: none;\n"
"}\n"
"\n"
"")
        self.Fundo_verde = QtWidgets.QFrame(Form)
        self.Fundo_verde.setGeometry(QtCore.QRect(100, 70, 291, 301))
        self.Fundo_verde.setStyleSheet("QFrame\n"
"{\n"
"background: #7FFFD4;\n"
"border-radius: 30px;\n"
"}\n"
"")
        self.Fundo_verde.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fundo_verde.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fundo_verde.setObjectName("Fundo_verde")
        self.RodarPrograma = QtWidgets.QPushButton(self.Fundo_verde)
        self.RodarPrograma.setGeometry(QtCore.QRect(30, 190, 231, 41))
        self.RodarPrograma.setObjectName("RodarPrograma")
        self.CarregarArquivo = QtWidgets.QPushButton(self.Fundo_verde)
        self.CarregarArquivo.setGeometry(QtCore.QRect(20, 70, 201, 41))
        self.CarregarArquivo.setStyleSheet("QPushButton_2\n"
"{\n"
"background-color: rgb(119, 239, 197);\n"
"border:none;\n"
"padding-top: 5px;\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-bottom-color: 3px solid rgb(85, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton_2:hover{\n"
"background-color: rgb(58, 174, 179);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-bottom-color: 3px solid rgb(85, 255, 255)\n"
"}\n"
"\n"
"QPushButton_2:pressed{\n"
"background-color: rgb(108, 218, 178);\n"
"border-left-color:1px solid rgb(85, 255, 255);\n"
"border-right-color:1px solid rgb(85, 255, 255);\n"
"border-top: 3px solid rgb(85, 255, 255);\n"
"border-bottom-color: 3px solid \n"
"    color: rgb(43, 121, 138);\n"
"border-bottom: none;\n"
"}\n"
"\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.CarregarArquivo.setObjectName("CarregarArquivo")
        self.TresPontinhos = QtWidgets.QToolButton(self.Fundo_verde)
        self.TresPontinhos.setGeometry(QtCore.QRect(230, 70, 41, 41))
        self.TresPontinhos.setObjectName("TresPontinhos")
        self.Cancelar = QtWidgets.QPushButton(Form)
        self.Cancelar.setGeometry(QtCore.QRect(410, 10, 71, 31))
        self.Cancelar.setObjectName("Cancelar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.RodarPrograma.setText(_translate("Form", "Rodar programa"))
        self.CarregarArquivo.setText(_translate("Form", "Carregar arquivo"))
        self.TresPontinhos.setText(_translate("Form", "..."))
        self.Cancelar.setText(_translate("Form", "Cancelar"))

#import teste

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


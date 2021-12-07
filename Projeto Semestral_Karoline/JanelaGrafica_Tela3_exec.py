# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JanelaGrafica_Tela3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(546, 408)
        Form.setStyleSheet("#Form\n"
"{\n"
"image: url(:/images/Foto_Rua.png);\n"
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
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 10, 81, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Fechar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Fechar.setObjectName("Fechar")
        self.verticalLayout.addWidget(self.Fechar)
        self.Voltar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Voltar.setObjectName("Voltar")
        self.verticalLayout.addWidget(self.Voltar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Fechar.setText(_translate("Form", "Fechar"))
        self.Voltar.setText(_translate("Form", "Voltar"))

#import teste_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


"""
@author: Karoline Duarte de Brito
"""


import JanelaGrafica_Tela1
import JanelaGrafica_Tela2
import JanelaGrafica_Tela3
from ui_functions import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Controller:
    def __init__(self):
        
        self.JanelaGrafica_Tela1_Window = QtWidgets.QMainWindow()
        self.JanelaGrafica_Tela1 = JanelaGrafica_Tela1.Ui_MainWindow
        self.JanelaGrafica_Tela1.setupUi(self.JanelaGrafica_Tela1_Window)
        
        self.JanelaGrafica_Tela1_ui.Next.clicked.connect(self.show_JanelaGrafica_Tela2)
        
        self.JanelaGrafica_Tela2_Window = QtWidgets.QMainWindow()
        self.JanelaGrafica_Tela2_ui = JanelaGrafica_Tela2.Ui_MainWindow()
        self.JanelaGrafica_Tela2_ui.setupUi(self.JanelaGrafica_Tela2_Window)
        
        self.JanelaGrafica_Tela2_ui.RodarPrograma.clicked.connect(self.show_JanelaGrafica_Tela3)
        
        self.JanelaGrafica_Tela3_Window = QtWidgets.QMainWindow()
        self.JanelaGrafica_Tela3_ui = JanelaGrafica_Tela3.Ui_MainWindow()
        self.JanelaGrafica_Tela3_ui.setupUi(self.JanelaGrafica_Tela3_Window)
            
        self.JanelaGrafica_Tela2_ui.Cancelar.clicked.connect(self.show_JanelaGrafica_Tela1)
        
        self.JanelaGrafica_Tela2_ui.Voltar.clicked.connect(self.show_JanelaGrafica_Tela2)
        self.JanelaGrafica_Tela3_ui.Fechar.clicked_connect(self._JanelaGrafica_Tela3_Window.close()) 

        
    ## FUNCOES PARA EXIBIR TODAS AS TELAS
    ########################################################################
    def show_JanelaGrafica_Tela1(self):
        self.JanelaGrafica_Tela1_Window.show()    
        self.JanelaGrafica_Tela2_Window.close()
        self.JanelaGrafica_Tela3_Window.close()    
        
    def show_JanelaGrafica_Tela2(self):
        # self.tela1_Window.close()
        self.JanelaGrafica_Tela2_Window.show()
            
    def show_JanelaGrafica_Tela3(self):
        # self.JanelaGrafica_Tela1_Window.close()
        self.JanelaGrafica_Tela3_Window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_JanelaGrafica_Tela1()
    sys.exit(app.exec_())
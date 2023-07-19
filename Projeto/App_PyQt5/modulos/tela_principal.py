from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tp_tela_principal import Ui_MainWindow
from modulos.cad_produtos import cad_produtos
from modulos.cad_categoria import cad_categoria

class main_window(QMainWindow):
    def __init__(self, *args, **argvs):
        super(main_window, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setDisabled(True)
        
        self.ui.actionCadastrar_Produto.triggered.connect(self.open_cad_prod)
        self.ui.actionCadastrar_Categoria.triggered.connect(self.open_cad_cate)
        
    def open_cad_prod(self):
        self.w_cad_prod = cad_produtos()
        self.w_cad_prod.show()
    
    def open_cad_cate(self):
        self.w_cad_cate = cad_categoria()
        self.w_cad_cate.show()
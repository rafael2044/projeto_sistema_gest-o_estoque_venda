from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tp_cad_prod import Ui_Cadastro
from modulos.pesq_produto import pesq_produto

class cad_produtos(QMainWindow):
    def __init__(self, *args, **argvs):
        super(cad_produtos, self).__init__(*args, **argvs)
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self)
        
        self.ui.bt_edit.clicked.connect(self.open_edit_prod)
        
    def open_edit_prod(self):
        self.w_edit_prod = pesq_produto()
        self.w_edit_prod.show()
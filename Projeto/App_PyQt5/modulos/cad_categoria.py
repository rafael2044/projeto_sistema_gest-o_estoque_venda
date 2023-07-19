from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tp_cad_cate import Ui_cad_categoria
from modulos.pesq_categoria import pesq_categoria
import modulos.cursors as cur

class cad_categoria(QMainWindow):
    def __init__(self, *args, **argvs):
        super(cad_categoria, self).__init__(*args, **argvs)
        self.ui = Ui_cad_categoria()
        self.ui.setupUi(self)
        
        self.ui.bt_pesq.clicked.connect(self.open_pesq_cate)
        self.ui.bt_cad.clicked.connect(self.cadastrar)
    def open_pesq_cate(self):
        self.w_pesq_cat = pesq_categoria()
        self.w_pesq_cat.show()
    
    def cadastrar(self):
        nome = self.ui.txt_nome.text()
        if cur.insert_categoria(nome):
            QMessageBox.information(QMessageBox(),  'Cadastro Categoria', 'Categoria cadastrada com Sucesso!')
        else:
            QMessageBox.information(QMessageBox(),  'Cadastro Categoria', 'A categoria ja esta cadastrada!')
        
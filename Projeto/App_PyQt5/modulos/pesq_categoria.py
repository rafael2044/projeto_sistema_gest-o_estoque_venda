from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot, QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tp_pesq_cat import Ui_pesq_cat
import modulos.cursors as cur

class pesq_categoria(QMainWindow):
    def __init__(self, *args, **argvs):
        super(pesq_categoria, self).__init__(*args, **argvs)
        self.ui = Ui_pesq_cat()
        self.ui.setupUi(self)
        self.ui.bt_pesquisar.clicked.connect(self.pesquisar)
        self.loader_all_categoria()
        self.ui.tb_categoria.itemClicked.connect(self.active_buttons)

    
        
    def pesquisar(self):
        result = cur.select_categoria(self.ui.txt_pesquisa.text())
        if result:
            self.ui.tb_categoria.setRowCount(0)
            for linha, dados in enumerate(result):
                self.ui.tb_categoria.insertRow(linha)
                for col, d in enumerate(dados.values()):
                    self.ui.tb_categoria.setItem(linha, col, QTableWidgetItem(str(d)))
    
    def loader_all_categoria(self):
        result = cur.select_all_categoria()
        if result:
            self.ui.tb_categoria.setRowCount(0)
            for linha, dados in enumerate(result):
                self.ui.tb_categoria.insertRow(linha)
                for col, d in enumerate(dados.values()):
                    self.ui.tb_categoria.setItem(linha, col, QTableWidgetItem(str(d)))

    def active_buttons(self):
        self.ui.bt_edit.setEnabled(True)
        self.ui.bt_del.setEnabled(True)
        
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tp_pesq_prod_v2 import Ui_Pes_prod

class pesq_produto(QMainWindow):
    def __init__(self, *args, **argvs):
        super(pesq_produto, self).__init__(*args, **argvs)
        self.ui = Ui_Pes_prod()
        self.ui.setupUi(self)
    
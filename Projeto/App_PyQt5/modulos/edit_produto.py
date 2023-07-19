from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tp_edit_prod import Ui_Editar

class edit_produto(QMainWindow):
    def __init__(self, *args, **argvs):
        super(edit_produto, self).__init__(*args, **argvs)
        self.ui = Ui_Editar()
        self.ui.setupUi(self)
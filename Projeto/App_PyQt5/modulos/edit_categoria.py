from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tp_edit_cat import Ui_edit_cat

class edit_categoria(QMainWindow):
    def __init__(self, *args, **argvs):
        super(edit_categoria, self).__init__(*args, **argvs)
        self.ui = Ui_edit_cat()
        self.ui.setupUi(self)
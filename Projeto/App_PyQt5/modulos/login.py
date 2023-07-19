from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from modulos.tela_principal import main_window
from template.tp_login import Ui_Login

import modulos.cursors as cursors

class login(QDialog):
    def __init__(self, *args, **argvs):
        super(login, self).__init__(*args, **argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.main_window = main_window()
        self.main_window.show()
        self.main_window.ui.actionLogout.triggered.connect(self.logout)
        
        self.ui.bt_entrar.clicked.connect(self.logar)
        self.ui.bt_sair.clicked.connect(self.sair)
    def logar(self):
        
        user = self.ui.txt_user.text()
        password_user = self.ui.txt_password.text()
        
        if cursors.validate_usuario(user, password_user):
            self.main_window.setEnabled(True)
            self.setVisible(False)
            self.main_window.ui.lb_user.setText(user)
            self.ui.txt_user.setText('')
            self.ui.txt_password.setText('')
            self.ui.txt_user.setFocus()
        else:
            QMessageBox.information(QMessageBox(),  'Login Invalido', 'Usuario ou Senha Invalido!')
    
    def sair(self):
        self.main_window.close()
        self.close()
    
    def logout(self):
        self.main_window.setDisabled(True)
        self.main_window.ui.lb_user.setText('')
        self.setVisible(True)
        self.ui.txt_user.setFocus()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tb_estoque = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_estoque.setGeometry(QtCore.QRect(10, 60, 781, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_estoque.sizePolicy().hasHeightForWidth())
        self.tb_estoque.setSizePolicy(sizePolicy)
        self.tb_estoque.setLineWidth(1)
        self.tb_estoque.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tb_estoque.setObjectName("tb_estoque")
        self.tb_estoque.setColumnCount(5)
        self.tb_estoque.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tb_estoque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        item.setFont(font)
        self.tb_estoque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        item.setFont(font)
        self.tb_estoque.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        item.setFont(font)
        self.tb_estoque.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        item.setFont(font)
        self.tb_estoque.setHorizontalHeaderItem(4, item)
        self.tb_estoque.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_estoque.horizontalHeader().setDefaultSectionSize(160)
        self.tb_estoque.horizontalHeader().setMinimumSectionSize(100)
        self.tb_estoque.verticalHeader().setCascadingSectionResizes(False)
        self.tb_estoque.verticalHeader().setDefaultSectionSize(50)
        self.tb_estoque.verticalHeader().setMinimumSectionSize(50)
        self.tb_estoque.verticalHeader().setStretchLastSection(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lb_user_logado = QtWidgets.QLabel(self.centralwidget)
        self.lb_user_logado.setGeometry(QtCore.QRect(500, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_user_logado.setFont(font)
        self.lb_user_logado.setObjectName("lb_user_logado")
        self.lb_user = QtWidgets.QLabel(self.centralwidget)
        self.lb_user.setGeometry(QtCore.QRect(610, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_user.setFont(font)
        self.lb_user.setText("")
        self.lb_user.setObjectName("lb_user")
        MainWindow.setCentralWidget(self.centralwidget)
        self.bar_menu = QtWidgets.QMenuBar(MainWindow)
        self.bar_menu.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.bar_menu.setObjectName("bar_menu")
        self.Cadastrar = QtWidgets.QMenu(self.bar_menu)
        self.Cadastrar.setObjectName("Cadastrar")
        self.menuSair = QtWidgets.QMenu(self.bar_menu)
        self.menuSair.setObjectName("menuSair")
        MainWindow.setMenuBar(self.bar_menu)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCadastrar_Produto = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/add_produto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadastrar_Produto.setIcon(icon)
        self.actionCadastrar_Produto.setObjectName("actionCadastrar_Produto")
        self.actionCadastrar_Categoria = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/add_categoria.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadastrar_Categoria.setIcon(icon1)
        self.actionCadastrar_Categoria.setObjectName("actionCadastrar_Categoria")
        self.actionCadastrar_Unidade = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Icons/add_medida.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadastrar_Unidade.setIcon(icon2)
        self.actionCadastrar_Unidade.setObjectName("actionCadastrar_Unidade")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.Cadastrar.addAction(self.actionCadastrar_Produto)
        self.Cadastrar.addAction(self.actionCadastrar_Categoria)
        self.Cadastrar.addAction(self.actionCadastrar_Unidade)
        self.menuSair.addAction(self.actionLogout)
        self.bar_menu.addAction(self.Cadastrar.menuAction())
        self.bar_menu.addAction(self.menuSair.menuAction())
        self.toolBar.addAction(self.actionCadastrar_Produto)
        self.toolBar.addAction(self.actionCadastrar_Categoria)
        self.toolBar.addAction(self.actionCadastrar_Unidade)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Estoque"))
        item = self.tb_estoque.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tb_estoque.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cod Barra"))
        item = self.tb_estoque.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Produto"))
        item = self.tb_estoque.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.tb_estoque.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Estoque"))
        self.label.setText(_translate("MainWindow", "ESTOQUE ATUAL"))
        self.lb_user_logado.setText(_translate("MainWindow", "Usuario logado: "))
        self.Cadastrar.setTitle(_translate("MainWindow", "Cadastar"))
        self.menuSair.setTitle(_translate("MainWindow", "Sair"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCadastrar_Produto.setText(_translate("MainWindow", "Produto"))
        self.actionCadastrar_Produto.setToolTip(_translate("MainWindow", "Cadastra Produtos no Estoque"))
        self.actionCadastrar_Categoria.setText(_translate("MainWindow", "Categoria"))
        self.actionCadastrar_Categoria.setToolTip(_translate("MainWindow", "Cadastra novas categorias"))
        self.actionCadastrar_Unidade.setText(_translate("MainWindow", "Unidade"))
        self.actionCadastrar_Unidade.setToolTip(_translate("MainWindow", "Cadastra novas unidades"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
import template.img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from customtkinter import CTkFrame, CTkButton, CTk, CTkLabel
from modulos.login import Login
from modulos.cad_produto import CadProduto
from tkinter.ttk import Treeview, Scrollbar
from tkinter import Menu, PhotoImage
from modulos.img import *
class TelaPrincipal(CTk):
    def __init__(self):
        CTk.__init__(self)
        self.title('Sistema')
        self.center_window()
        self.loader_widgets()
        self.cad_prod = None
        self.cad_cat = None
        self.cad_un = None
        self.login = Login(self)
        self.login.focus_set()
        
        
    def center_window(self):
        HEIGHT = 800
        WEIDTH = 1080
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
    
    def loader_widgets(self):
        self.loader_menu()
        f_button_menu = CTkFrame(self, height=100, width=1000)
        f_info = CTkFrame(self, height=100, width=1000)
        f_tabela = CTkFrame(self, height=0, width=1000)
        f_scroll = CTkFrame(self, height=10, width=1000)
        
        
        self.usuario = CTkLabel(f_info, text=' '*50, font=('Segoe UI', 12, 'bold'))
        
        self.tv_tabela = Treeview(f_tabela, columns=('id', 'cod_barra', 'descricao', 'preco_un', 'fornecedor','quant_min', 'quant_atual', 'quant_max'),
                                  height=100)
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('cod_barra', text='Cod. Barra')
        self.tv_tabela.heading('descricao', text='Descrição')
        self.tv_tabela.heading('preco_un', text='Preço Unitário')
        self.tv_tabela.heading('fornecedor', text='Fornecedor')
        self.tv_tabela.heading('quant_min', text='Quant. Min')
        self.tv_tabela.heading('quant_atual', text='Quant. Atual')
        self.tv_tabela.heading('quant_max', text='Quant. Max')
        
        self.tv_tabela.column('#0', width=2, minwidth=2, stretch=False)
        self.tv_tabela.column('id', width=50, stretch=False)
        self.tv_tabela.column('cod_barra', width=100, stretch=False)
        self.tv_tabela.column('descricao', width=300, stretch=False)
        self.tv_tabela.column('preco_un', width=100, stretch=False)
        self.tv_tabela.column('fornecedor', width=150, stretch=False)
        self.tv_tabela.column('quant_min', width=100, stretch=False)
        self.tv_tabela.column('quant_atual', width=100, stretch=False)
        self.tv_tabela.column('quant_max', width=100, stretch=False)
        
        self.scrollbar_vertical = Scrollbar(f_tabela, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(f_scroll, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        f_button_menu.pack(padx=10, pady=5, anchor='w')
        f_info.pack(padx=10, anchor='w')
        f_tabela.pack(padx=10, pady=5, anchor='w')
        f_scroll.pack(padx=10, pady=5, anchor='w')
        
        
        CTkButton(f_button_menu, text='Cadastrar Produto', image=PhotoImage(data=icon_add_produto),
                  compound='top', command=self.open_cad_prod).pack(side='left', padx=10)
        self.usuario.pack(side='right', padx=10)
        CTkLabel(f_info, text='Estoque Atual', font=('Segoe UI', 19, 'bold')).pack(side='left', padx=10)
        CTkLabel(f_info, text='Usuario Logado:', font=('Segoe UI', 12, 'bold')).pack(side='right')
        
        self.tv_tabela.pack(pady=10)
        self.scrollbar_vertical.pack(side='left', fill='y')

        self.scrollbar_horizontal.pack(fill='x')
        
    def loader_menu(self):
        self.menubar = Menu(self, font=('Segoe UI', 14))
        self.configure(menu=self.menubar)
        cad_menu = Menu(self.menubar, font=('Segoe UI', 10))
        cad_menu.add_command(label='Produto')
        cad_menu.add_command(label='Categoria')
        cad_menu.add_command(label='Unidade')
        
        sair_menu = Menu(self.menubar, font=('Segoe UI', 14))
        sair_menu.add_command(label='Logout', command=self.sair)
        
        self.menubar.add_cascade(label='Cadastrar', menu=cad_menu)
        self.menubar.add_cascade(label='Sair', menu=sair_menu)
        
    def sair(self):
        self.login.deiconify()
        self.login.user.focus_force()
        self.login.grab_set()
    
    def open_cad_prod(self):
        if self.cad_prod is None or not self.cad_prod.winfo_exists():
            self.cad_prod = CadProduto()
        else:
            self.cad_prod.lift()
    
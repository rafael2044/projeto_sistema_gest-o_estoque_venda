from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTk, CTkLabel, CTkFont
from modulos.login import Login
from modulos.cad_produto import CadProduto
from modulos.cad_categoria import CadCategoria
from tkinter.ttk import Treeview
from tkinter import Menu, PhotoImage
from modulos.img import *
class TelaPrincipal(CTk):
    def __init__(self):
        CTk.__init__(self)
        self.title('Sistema')
        self.center_window()
        self.login = Login(self)
        self.loader_widgets()
        self.cad_prod = None
        self.cad_cat = None
        self.cad_un = None
        
        
    def center_window(self):
        HEIGHT = 700
        WEIDTH = 1000
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
    
    def loader_widgets(self):
        self.loader_menu()
        f_main = CTkFrame(self)
        f_button_menu = CTkFrame(f_main)
        f_info = CTkFrame(f_main)
        f_tabela = CTkFrame(f_main)
        self.usuario = CTkLabel(f_info, text=' '*50, font=('Segoe UI', 12, 'bold'))

        
        self.tv_tabela = Treeview(f_tabela, columns=('id', 'cod_barra', 'categoria', 'produto', 'quantidade', 'unidade'))
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('cod_barra', text='Cod. Barra')
        self.tv_tabela.heading('categoria', text='Categoria')
        self.tv_tabela.heading('produto', text='Produto')
        self.tv_tabela.heading('quantidade', text='Quantidade')
        self.tv_tabela.heading('unidade', text='Un')
        
        self.tv_tabela.column('#0', width=2, minwidth=2, stretch=False)
        self.tv_tabela.column('id', width=50, stretch=False)
        self.tv_tabela.column('cod_barra', width=100, stretch=False)
        self.tv_tabela.column('categoria', width=100)
        self.tv_tabela.column('produto', width=300)
        self.tv_tabela.column('quantidade', width=75, stretch=False)
        self.tv_tabela.column('unidade', width=50, stretch=False)

        f_main.pack(padx=10,pady=10, expand=True, fill='both')
        f_button_menu.pack(padx=10, pady=5, fill='x', side='top')
        CTkButton(f_button_menu, text='Cadastrar Produto', image=PhotoImage(data=icon_add_produto),
                  compound='top', command=self.open_cad_prod).pack(side='left', padx=10)
        CTkButton(f_button_menu, text='Cadastrar Categoria', image=PhotoImage(data=icon_add_categoria),
                  compound='top', command=self.open_cad_cate).pack(side='left')
        CTkButton(f_button_menu, text='Cadastrar Unidade', image=PhotoImage(data=icon_add_medida),
                  compound='top').pack(side='left', padx=10)
        f_info.pack(padx=10, fill='x', side='top')
        CTkLabel(f_info, text='Estoque Atual', font=('Segoe UI', 19, 'bold')).pack(side='left', padx=10)
        self.usuario.pack(side='right', padx=10)
        CTkLabel(f_info, text='Usuario Logado:', font=('Segoe UI', 12, 'bold')).pack(side='right')
        
        f_tabela.pack(side='top', padx=10, pady=5, expand=True, fill='both')
        self.tv_tabela.pack(padx=5, pady=5, expand=True, fill='both')
        
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
        self.login.grab_set()
    
    def open_cad_prod(self):
        if self.cad_prod is None or not self.cad_prod.winfo_exists():
            self.cad_prod = CadProduto()
        else:
            self.cad_prod.lift()
    
    def open_cad_cate(self):
        if self.cad_cat is None or not self.cad_cat.winfo_exists():
            self.cad_cat = CadCategoria()
            
        else:
            self.cad_cat.lift()
        
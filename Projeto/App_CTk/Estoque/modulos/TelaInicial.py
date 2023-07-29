from customtkinter import CTkFrame, CTkButton, CTk, CTkLabel, CTkFont
from Estoque.modulos.TelaLogin import Login
from Estoque.modulos.TelaCadProduto import CadProduto
from Estoque.modulos.TelaFornecedor import WFornecedor
from tkinter.ttk import Treeview, Scrollbar, Style
from tkinter import Menu, PhotoImage
from Imagens.img import *
from DAO.estoqueDAO import estoqueDAO
class TelaPrincipal(CTk):
    
    def __init__(self):
        CTk.__init__(self)
        self.title('Sistema')
        self.centralizar_janela()
        self.carregar_widgets()
        self.cad_prod = None
        self.w_fornecedor = None
        self.cad_un = None
        self.tipo_usuario = None
        self.login = Login(self)
        self.login.transient(self)
        
    def centralizar_janela(self):
        HEIGHT = 800
        WEIDTH = 1065
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
    
    def carregar_widgets(self):
        self.carregar_menu()
        self.style = Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview', font=('Segoe UI', 15), rowheight=30)
        self.style.configure('Treeview.Heading', font=('Segoe UI', 13, 'bold'))
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        
        f_button_menu = CTkFrame(self)
        f_info = CTkFrame(self)
        f_tabela = CTkFrame(self)
        f_scroll = CTkFrame(self, height=10)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')

        
        self.usuario = CTkLabel(f_info, text=' '*50, font=('Segoe UI', 12, 'bold'))
        
        self.tv_tabela = Treeview(f_tabela, columns=('id', 'cod_barra', 'descricao', 'preco_un', 'fornecedor','quant_min', 'quant_atual', 'quant_max'),
                                  selectmode='browse')
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('cod_barra', text='Cod. Barra')
        self.tv_tabela.heading('descricao', text='Descrição')
        self.tv_tabela.heading('preco_un', text='Preço Unitário')
        self.tv_tabela.heading('fornecedor', text='Fornecedor')
        self.tv_tabela.heading('quant_min', text='Quant. Min')
        self.tv_tabela.heading('quant_atual', text='Quant. Atual')
        self.tv_tabela.heading('quant_max', text='Quant. Max')
        
        self.tv_tabela.column('#0', width=2, minwidth=2, stretch=True)
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50, anchor='center')
        self.tv_tabela.column('cod_barra', width=175, stretch=True, minwidth=175, anchor='center')
        self.tv_tabela.column('descricao', width=300, stretch=False, minwidth=300)
        self.tv_tabela.column('preco_un', width=150, stretch=True, minwidth=150, anchor='center')
        self.tv_tabela.column('fornecedor', width=175, stretch=False, minwidth=175)
        self.tv_tabela.column('quant_min', width=100, stretch=True, minwidth=100, anchor='center')
        self.tv_tabela.column('quant_atual', width=115, stretch=True, minwidth=115, anchor='center')
        self.tv_tabela.column('quant_max', width=110, stretch=True, minwidth=110, anchor='center')
        
        self.scrollbar_vertical = Scrollbar(f_tabela, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(f_scroll, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        f_button_menu.pack(padx=10, pady=5, anchor='w', fill='x')
        f_info.pack(padx=10, anchor='w', fill='x')
        f_tabela.pack(padx=10, pady=0, anchor='w', fill='both', expand=True)
        f_scroll.pack(padx=10, pady=0, fill='x')
        
        
        CTkButton(f_button_menu, text='Cadastrar Produto', image=PhotoImage(data=icon_add_produto),
                  compound='top', command=self.abrir_tela_cadProd, font=self.font_button).pack(side='left', padx=(0,10))
        CTkButton(f_button_menu, text='Fornecedores', image=PhotoImage(data=icon_fornecedor),
                  compound='top', command=self.abrir_tela_fornecedor, font=self.font_button).pack(side='left', padx=(10,0))
        self.usuario.pack(side='right', padx=10)
        CTkLabel(f_info, text='Estoque Atual', font=('Segoe UI', 19, 'bold')).pack(side='left')
        CTkLabel(f_info, text='Usuario Logado:', font=('Segoe UI', 12, 'bold')).pack(side='right')
        
        self.tv_tabela.pack(side='left', fill='both')
        self.scrollbar_vertical.pack(fill='y', expand=True, anchor='w')
        f_scroll.pack(padx=10, pady=0, fill='x')
        self.scrollbar_horizontal.pack(fill='x')
        
    def carregar_menu(self):
        self.menubar = Menu(self, font=('Segoe UI', 14))
        self.configure(menu=self.menubar)
        cad_menu = Menu(self.menubar, font=('Segoe UI', 10))
        cad_menu.add_command(label='Produto', command=self.abrir_tela_cadProd)
        cad_menu.add_command(label='Fornecedor', command=self.abrir_tela_fornecedor)

        
        sair_menu = Menu(self.menubar, font=('Segoe UI', 14))
        sair_menu.add_command(label='Logout', command=self.sair)
        
        self.menubar.add_cascade(label='Cadastrar', menu=cad_menu)
        self.menubar.add_cascade(label='Sair', menu=sair_menu)
        
    def carregar_estoque(self):
        estoque = estoqueDAO().select_all_estoque()
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        if estoque:
            [self.tv_tabela.insert('', 'end', values=p) for p in estoque]
    
    def sair(self):
        self.login.deiconify()
        self.login.user.focus_force()
        self.login.grab_set()
    
    def abrir_tela_cadProd(self):
        if self.cad_prod is None or not self.cad_prod.winfo_exists():
            self.cad_prod = CadProduto(self)
            self.cad_prod.transient(self)
        else:
            self.cad_prod.after(100, self.cad_prod.lift)
    
    def abrir_tela_fornecedor(self):
        if self.w_fornecedor is None or not self.w_fornecedor.winfo_exists():
            self.w_fornecedor = WFornecedor()
            self.w_fornecedor.transient(self)
        else:
            self.w_fornecedor.after(100, self.w_fornecedor.lift)
        
    def verificar_restricoes_usuario(self):
        if self.tipo_usuario == 'Administrador':
            pass
        else:
            pass
from customtkinter import CTkFrame, CTkButton, CTk, CTkLabel, CTkFont, CTkImage
from Estoque.modulos.TelaLogin import Login
from Estoque.modulos.TelaProduto import TelaProduto
from Estoque.modulos.TelaEstoque import TelaEstoque
from Estoque.modulos.TelaFornecedor import TelaFornecedor
from tkinter.ttk import Treeview, Scrollbar, Style
from tkinter import Menu
from PIL import Image
from Imagens.img import img_cad_estoque, img_cad_produto, img_fornecedor
from DAO.estoqueDAO import estoqueDAO
class TelaPrincipal(CTk):
    
    def __init__(self):
        CTk.__init__(self)
        self.title('Sistema Estoque')
        self.carregar_widgets()
        self.estoque = None
        self.produto = None
        self.w_fornecedor = None
        self.cad_un = None
        self.dados_usuario = {'usuario':'', 'nivel':'', 'setor':''}
        self.login = Login(self)
        self.login.transient()
        self.centralizar_janela()

        self.mainloop()
    def centralizar_janela(self):
        HEIGHT = int(self.winfo_screenheight()/ 1.30)
        WEIDTH = int(self.winfo_screenwidth() / 1.20)
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.minsize(WEIDTH, HEIGHT)
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+') 
        self.after(0, lambda:self.wm_state('zoomed'))
        
    def carregar_widgets(self):
        self.carregar_menu()
        self.style = Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview', font=('Segoe UI', 12), rowheight=30)
        self.style.configure('Treeview.Heading', font=('Segoe UI', 13, 'bold'))
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=30)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=500)
        self.font_button = CTkFont('Segoe UI', size=18, slant='italic', weight='bold')

        f_menu_buttons = CTkFrame(self, fg_color='transparent', border_width=2, corner_radius=20)
        f_info = CTkFrame(self, fg_color='transparent', height=10)
        
        self.usuario = CTkLabel(f_info, text=' '*10, font=('Segoe UI', 12, 'bold'))
        
        self.tv_tabela = Treeview(self, columns=('id', 'cod_barra', 'descricao', 'preco_un', 'fornecedor','quant_min', 'quant_atual', 'quant_max'),
                                  selectmode='browse', show='headings')
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('cod_barra', text='Cod. Barra')
        self.tv_tabela.heading('descricao', text='Descrição')
        self.tv_tabela.heading('preco_un', text='Preço Unitário')
        self.tv_tabela.heading('fornecedor', text='Fornecedor')
        self.tv_tabela.heading('quant_min', text='Quant. Min')
        self.tv_tabela.heading('quant_atual', text='Quant. Atual')
        self.tv_tabela.heading('quant_max', text='Quant. Max')
        
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50, anchor='center')
        self.tv_tabela.column('cod_barra', width=175, stretch=True, minwidth=175, anchor='center')
        self.tv_tabela.column('descricao', width=500, stretch=False, minwidth=450)
        self.tv_tabela.column('preco_un', width=150, stretch=True, minwidth=150, anchor='center')
        self.tv_tabela.column('fornecedor', width=200, stretch=False, minwidth=175 )
        self.tv_tabela.column('quant_min', width=100, stretch= True, minwidth=100, anchor='center')
        self.tv_tabela.column('quant_atual', width=115, stretch=True, minwidth=115, anchor='center')
        self.tv_tabela.column('quant_max', width=110, stretch=True, minwidth=110, anchor='center')
        
        
        self.scrollbar_vertical = Scrollbar(self, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        f_menu_buttons.grid(column=0, row=0, columnspan=3, sticky='we', pady=0, padx=5) 
        self.bt_estoque = CTkButton(f_menu_buttons, text='Estoque', image=CTkImage(Image.open(img_cad_estoque), size=(60,60)),
                  compound='top', command=self.abrir_tela_Estoque, font=self.font_button, fg_color='transparent', corner_radius=20)
        self.bt_produto = CTkButton(f_menu_buttons, text='Produtos', image=CTkImage(Image.open(img_cad_produto), size=(60,60)),fg_color='transparent', corner_radius=20,
                  compound='top', command=self.abrir_tela_Produto, font=self.font_button)
        self.bt_fornecedor = CTkButton(f_menu_buttons, text='Fornecedores', image=CTkImage(Image.open(img_fornecedor), size=(60,60)),fg_color='transparent', corner_radius=20,
                  compound='top', command=self.abrir_tela_fornecedor, font=self.font_button)
        
        self.bt_estoque.pack(side='left', padx=10, pady=5)
        self.bt_produto.pack(side='left', padx=(0,10),  pady=5)
        self.bt_fornecedor.pack(side='left', padx=10,  pady=5)
        CTkLabel(self, text='Estoque Atual', font=('Segoe UI', 23, 'bold')).grid(row=1, column=0, sticky='w', padx=10,  pady=5)
        f_info.grid(column=2, row=1, sticky='e', padx=5)
        CTkLabel(f_info, text='Usuario Logado:', font=('Segoe UI', 12, 'bold')).pack(side='left', padx=(0,10),  pady=0)
    
        self.usuario.pack(side='left')
        
        self.tv_tabela.grid(column=0, row=2, columnspan=4, sticky='nsew', padx=(5,10))
        self.scrollbar_vertical.grid(column=2, row=2,  sticky='nse', padx=(0,5))
        self.scrollbar_horizontal.grid(column=0, row=3, columnspan=4, sticky='ew', padx=5, pady=(0,10))
        
    def carregar_menu(self):
        self.menubar = Menu(self, font=('Segoe UI', 14))
        self.configure(menu=self.menubar)
        self.cad_menu = Menu(self.menubar, font=('Segoe UI', 10))
        self.cad_menu.add_command(label='Estoque', command=self.abrir_tela_Estoque)
        self.cad_menu.add_command(label='Produto', command=self.abrir_tela_Produto)
        self.cad_menu.add_command(label='Fornecedor', command=self.abrir_tela_fornecedor)

        
        sair_menu = Menu(self.menubar, font=('Segoe UI', 14))
        sair_menu.add_command(label='Logout', command=self.sair)
        
        self.menubar.add_cascade(label='Cadastrar', menu=self.cad_menu)
        self.menubar.add_cascade(label='Sair', menu=sair_menu)
        
    def carregar_estoque(self):
        estoque = estoqueDAO().select_all_estoque()
        self.limpar_estoque()
        if estoque:
            [self.tv_tabela.insert('', 'end', values=p) for p in estoque]
    
    def limpar_estoque(self):
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        
    def sair(self):
        self.limpar_estoque()
        self.usuario.configure(text='')
        self.login.deiconify()
        self.login.user.focus_force()
        self.login.grab_set()
        
    def abrir_tela_Estoque(self):
        if self.estoque is None or not self.estoque.winfo_exists():
            self.estoque= TelaEstoque(self)
            self.estoque.transient(self) 
            
    def abrir_tela_Produto(self):
        if self.produto is None or not self.produto.winfo_exists():
            self.produto = TelaProduto(self)
            self.produto.transient(self)
    
    def abrir_tela_fornecedor(self):
        if self.w_fornecedor is None or not self.w_fornecedor.winfo_exists():
            self.w_fornecedor = TelaFornecedor(self)
            self.w_fornecedor.transient(self)
    
    def desabilitar_botoes_menu(self):
        self.bt_estoque.configure(state='disabled')
        self.bt_estoque.configure(fg_color='gray')
        self.bt_produto.configure(state='disabled')
        self.bt_produto.configure(fg_color='gray')
        self.bt_fornecedor.configure(state='disabled')
        self.bt_fornecedor.configure(fg_color='gray')
        self.cad_menu.entryconfig('Estoque', state='disabled')
        self.cad_menu.entryconfig('Produto', state='disabled')
        self.cad_menu.entryconfig('Fornecedor', state='disabled')  
    
    def habilitar_botoes_menu(self):
        self.bt_estoque.configure(state='enabled')
        self.bt_estoque.configure(fg_color='transparent')
        self.bt_produto.configure(state='enabled')
        self.bt_produto.configure(fg_color='transparent')
        self.bt_fornecedor.configure(state='enabled')
        self.bt_fornecedor.configure(fg_color='transparent')
        self.cad_menu.entryconfig('Estoque', state='active')
        self.cad_menu.entryconfig('Produto', state='active')
        self.cad_menu.entryconfig('Fornecedor', state='active')
    
    def verificar_restricoes_usuario(self):
        if (self.dados_usuario['nivel'] == 'Padrao' and self.dados_usuario['setor'] == 'Estoque'):
            self.habilitar_botoes_menu()
        elif(self.dados_usuario['nivel'] == 'Administrador' and (self.dados_usuario['setor'] == 'Estoque' or self.dados_usuario['setor'] == 'ADM')):
            self.habilitar_botoes_menu()
        else:
            self.desabilitar_botoes_menu()
        
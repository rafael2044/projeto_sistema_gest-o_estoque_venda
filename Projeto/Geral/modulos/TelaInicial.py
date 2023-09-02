from customtkinter import CTkFrame, CTkButton, CTk, CTkLabel, CTkFont, CTkImage
from Geral.modulos.TelaLogin import Login
from Geral.modulos.TelaProduto import TelaProduto
from Geral.modulos.TelaEstoque import TelaEstoque
from Geral.modulos.TelaFornecedor import TelaFornecedor
from tkinter.ttk import Treeview, Scrollbar, Style
from tkinter import Menu
from PIL import Image
from Imagens.img import img_cad_estoque, img_cad_produto, img_fornecedor, img_venda
from DAO.estoqueDAO import estoqueDAO
class TelaPrincipal(CTk):
    
    def __init__(self):
        CTk.__init__(self)
        self.title('Sistema Estoque')
        self.carregar_widgets()
        self.venda = None
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
        
        f_menu_buttons.grid(column=0, row=0, columnspan=3, sticky='we', pady=0, padx=5) 
        self.bt_venda = CTkButton(f_menu_buttons, text='Venda', image=CTkImage(Image.open(img_venda), size=(60,60)),
                  compound='top', command=self.abrir_tela_Venda, font=self.font_button, fg_color='transparent', corner_radius=20)
        self.bt_estoque = CTkButton(f_menu_buttons, text='Estoque', image=CTkImage(Image.open(img_cad_estoque), size=(60,60)),
                  compound='top', command=self.abrir_tela_Estoque, font=self.font_button, fg_color='transparent', corner_radius=20)
        self.bt_produto = CTkButton(f_menu_buttons, text='Produtos', image=CTkImage(Image.open(img_cad_produto), size=(60,60)),fg_color='transparent', corner_radius=20,
                  compound='top', command=self.abrir_tela_Produto, font=self.font_button)
        self.bt_fornecedor = CTkButton(f_menu_buttons, text='Fornecedores', image=CTkImage(Image.open(img_fornecedor), size=(60,60)),fg_color='transparent', corner_radius=20,
                  compound='top', command=self.abrir_tela_fornecedor, font=self.font_button)
        
        self.bt_venda.pack(side='left', padx=10, pady=5)
        self.bt_estoque.pack(side='left', padx=10, pady=5)
        self.bt_produto.pack(side='left', padx=(0,10),  pady=5)
        self.bt_fornecedor.pack(side='left', padx=10,  pady=5)
        f_info.grid(column=2, row=1, sticky='e', padx=5)
        CTkLabel(f_info, text='Usuario Logado:', font=('Segoe UI', 12, 'bold')).pack(side='left', padx=(0,10),  pady=0)
    
        self.usuario.pack(side='left')
        
        
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
        
    def sair(self):
        self.limpar_estoque()
        self.usuario.configure(text='')
        self.login.deiconify()
        self.login.user.focus_force()
        self.login.grab_set()
        
    def abrir_tela_Venda(self):
        if self.venda is None or not self.venda.winfo_exists():
            #self.venda = TelaEstoque(self)
            #self.venda.transient(self)     
            pass
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
        self.bt_venda.configure(state='disabled')
        self.bt_venda.configure(fg_color='gray')
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
        self.bt_venda.configure(state='enabled')
        self.bt_venda.configure(fg_color='transparent')
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
        
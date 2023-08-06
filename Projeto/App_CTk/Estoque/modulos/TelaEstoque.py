from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton, CTkTabview, CTkFont, CTkImage
from tkinter.ttk import Treeview, Scrollbar
from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from DAO.estoqueDAO import estoqueDAO
from Estoque.modulos.TelaCadEstoque import CadEstoque
from Imagens.img import img_add_estoque
from PIL import Image
class TelaEstoque(CTkToplevel):
    
    def __init__(self, master=None):
        CTkToplevel.__init__(self, master=master, takefocus=True)
        self.master=master
        self.after(100, self.lift)
        self.title('Estoque')
        self.fornecedorDAO = fornecedorDAO()
        self.produtoDAO = produtoDAO()
        self.estoqueDAO = estoqueDAO()
        self.cadEstoque = None
        self.centralizar_janela()
        self.carreagar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = 800
        WEIDTH = 700
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//4.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carreagar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, slant='italic', weight='bold')
        
        
        tabv_main = CTkTabview(self, corner_radius=20)
        tabv_main._segmented_button.configure(font=self.font_label)
        self.tab_pesq = tabv_main.add('Pesquisar') 
        self.tab_cad = tabv_main.add('Cadastrar')
        self.tab_cad.grid_columnconfigure(0, weight=325)
        self.tab_cad.grid_columnconfigure(1, weight=325)
        self.tab_cad.grid_rowconfigure(0, weight=1)
        self.tab_cad.grid_rowconfigure(1, weight=600)
        tabv_main.pack(expand=True, fill='both', padx=10, pady=10)
        self.carregar_w_tab_cad()
        self.carregar_produtos()
    
    def carregar_w_tab_cad(self):
        
        self.pesquisa = CTkEntry(self.tab_cad, placeholder_text='Nome do Produto', width=150, font=self.font_entry)
        
        self.tv_tabela = Treeview(self.tab_cad, columns=('id', 'cod_barra', 'descricao', 'fornecedor', 'preco_un'),
                                  selectmode='browse', show='headings')
        
        
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('cod_barra', text='Cod. Barra')
        self.tv_tabela.heading('descricao', text='Descrição')
        self.tv_tabela.heading('fornecedor', text='Fornecedor')
        self.tv_tabela.heading('preco_un', text='Preço Un')
    
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50, anchor='center')
        self.tv_tabela.column('cod_barra', width=175, stretch=True, minwidth=175)
        self.tv_tabela.column('descricao', width=450, stretch=True, minwidth=300)
        self.tv_tabela.column('fornecedor', width=200, stretch=True, minwidth=200)
        self.tv_tabela.column('preco_un', width=150, stretch=True, minwidth=150)        
        
        self.scrollbar_vertical = Scrollbar(self.tab_cad, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self.tab_cad, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        self.bt_cadastrar = CTkButton(self.tab_cad, image=CTkImage(Image.open(img_add_estoque), size=(32,32)), text='Cadastrar', compound='left', font=self.font_button,height=40, width=140, state='disabled',fg_color='gray',
                                      command=self.abrir_janela_cadEstoque)
        
        self.pesquisa.grid(column=0, row=0, columnspan=2, sticky='ew', pady=10)
        CTkLabel(self.tab_cad, text='Lista de Produtos não cadastrados em estoque', font=('Segoe UI', 15, 'bold')).grid(column=0, columnspan=2, row=1, sticky='nw')
        self.tv_tabela.grid(column=0, row=1 ,columnspan=2, sticky='nsew', pady=(30,0))
        self.scrollbar_vertical.grid(row=1, column=1, rowspan=2, sticky='nse',pady=(35, 0))
        self.scrollbar_horizontal.grid(row=2, column=0, columnspan=2, sticky='ew' )
        self.bt_cadastrar.grid(column=1, row=3, pady=10, sticky='e')
        
        self.tv_tabela.bind('<<TreeviewSelect>>', self.produto_selecionado)
        self.bind('<Button-1>', self.click_fora_da_tabela)
    def carregar_w_tab_pesq(self):
        self.pesquisa = CTkEntry(self.tab_cad, placeholder_text='Nome do Produto', width=150, font=self.font_entry)

    def carregar_produtos(self):
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        produtos = self.produtoDAO.select_produto_n_cad_em_estoque()
        if produtos:
            [self.tv_tabela.insert('', 'end', values=x) for x in produtos]
    
    def verificar_restricoes_usuario(self):
        if self.master.tipo_usuario == 'Administrador':
            self.habilitar_botoes_menu()
        else:
            self.desabilitar_botoes_menu()
        
    def produto_selecionado(self, event):
        self.produto_dados = self.tv_tabela.selection()
        if self.produto_dados and self.master.tipo_usuario == 'Administrador':
            self.habilitar_botoes_inferiores()
    
    def click_fora_da_tabela(self, event):
        if event.widget not in (self.tv_tabela, self.bt_cadastrar) and self.focus_get() is self.tv_tabela and self.master.tipo_usuario == 'Administrador':
            self.desabilitar_botoes_inferiores()
            self.tv_tabela.selection_set()
    
    def desabilitar_botoes_inferiores(self):
        self.bt_cadastrar.configure(state='disabled')
        self.bt_cadastrar.configure(fg_color='gray')
        
    def habilitar_botoes_inferiores(self):
        self.bt_cadastrar.configure(state='enabled')
        self.bt_cadastrar.configure(fg_color=("#3a7ebf", "#1f538d"))
        
    def abrir_janela_cadEstoque(self):
        dados = self.tv_tabela.item(self.produto_dados[0], 'values')
        if self.cadEstoque is None or not self.cadEstoque.winfo_exists():
            self.cadEstoque = CadEstoque(self, dados)
            self.cadEstoque.transient(self)
            
        
from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton, CTkFont, CTkImage, CTkFrame
from tkinter.ttk import Treeview, Scrollbar
from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from DAO.estoqueDAO import estoqueDAO
from Estoque.modulos.TelaCadEstoque import CadEstoque
from Imagens.img import img_add_estoque, img_editar, img_excluir, img_pesquisa, img_atualizar, img_cad_novos_produtos
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
        self.cadNovosProdutos = None
        self.centralizar_janela()
        self.carreagar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = int(self.winfo_screenheight()/ 1.30)
        WEIDTH = int(self.winfo_screenwidth() / 1.20)
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//2)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carreagar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, slant='italic', weight='bold')
        
        self.carregar_widgets()
    
    
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        
        self.pesquisa = CTkEntry(self, placeholder_text='Nome do Produto', width=150, height=40, font=self.font_entry)
            
        f_bts_top = CTkFrame(self, corner_radius=25, fg_color='transparent')
        f_bts_bottom = CTkFrame(self, corner_radius=25, fg_color='transparent')    
            
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
        
        self.bt_delete = CTkButton(f_bts_bottom, state='disabled', text='Deletar', font=('Segoe UI', 18, 'bold'), 
                                   image=CTkImage(Image.open(img_excluir), size=(32,32)),height=45,width=120,fg_color='#595457', 
                                   compound='left')
        self.bt_editar = CTkButton(f_bts_bottom, state='disabled', text='Editar',font=('Segoe UI', 18, 'bold'),
                                   image=CTkImage(Image.open(img_editar), size=(32,32)), height=45,
                                   width=110,fg_color='#595457',compound='left')
        
        self.scrollbar_vertical = Scrollbar(self, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        self.pesquisa.grid(column=0, row=0, padx=10, pady=10, sticky='we')
        f_bts_top.grid(column=1, columnspan=2, row=0, sticky='e')
        
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_pesquisa), size=(32,32)), width=75,height=40).pack(side='left', padx=(5,5))
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_atualizar), size=(32,32)),height=40, width=80).pack(side='left', padx=(5,10))
        CTkButton(f_bts_top, text='Cadastrar', image=CTkImage(Image.open(img_cad_novos_produtos), size=(32,32)),font=self.font_button, compound='left',height=40,
                  command=self.abrir_tela_cadastrar_novos_produtos).pack(side='left', padx=(5,10))
        
        self.tv_tabela.grid(column=0, row=1, columnspan=2, sticky='wsen', padx=(10,0))
        self.scrollbar_vertical.grid(column=2, row=1, sticky='wns', padx=(0,10))
        self.scrollbar_horizontal.grid(column=0, row=2, sticky='we', columnspan=3, padx=(10,10))
        f_bts_bottom.grid(column=0, columnspan=3, row=3, sticky='we')
        self.bt_editar.pack(anchor='e',side='right', padx=10)
        self.bt_delete.pack(anchor='e',side='right', padx=10, pady=10)
        
        self.tv_tabela.bind('<<TreeviewSelect>>', self.linha_selecionado)
        self.bind('<Button-1>', self.desabilitar_botoes)
        
    def desabilitar_botoes(self, event):
        if event.widget not in (self.tv_tabela, self.bt_delete, self.bt_editar) and self.focus_get() is self.tv_tabela:
            self.bt_delete.configure(state='disabled')
            self.bt_delete.configure(fg_color='#595457')
            self.bt_editar.configure(state='disabled')
            self.bt_editar.configure(fg_color='#595457')
            self.tv_tabela.selection_set()        
        
    def linha_selecionado(self, event):
        self.item = self.tv_tabela.selection()
        if self.item:
            if self.master.dados_usuario['nivel'] == 'Administrador':
                self.bt_delete.configure(state='enabled')
                self.bt_delete.configure(fg_color=("#3a7ebf", "#1f538d"))
            self.bt_editar.configure(state='enabled')
            self.bt_editar.configure(fg_color=("#3a7ebf", "#1f538d"))    
        
    def abrir_tela_cadastrar_novos_produtos(self):
        if self.cadNovosProdutos is None or not self.cadNovosProdutos.winfo_exists():
            self.cadNovosProdutos = TelaProdutoEstoque(self)
            self.cadNovosProdutos.transient(self)
        
class TelaProdutoEstoque(CTkToplevel):
    def __init__(self, master=None):
        CTkToplevel.__init__(self, master=master, takefocus=True)
        self.master=master
        self.after(100, self.lift)
        self.title('Produtos não cadastrados em estoque')
        self.produtoDAO = produtoDAO()
        self.cadEstoque = None
        self.centralizar_janela()
        self.carregar_widgets()
        self.carregar_produtos()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = 700
        WEIDTH = 900
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//2)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')    
        
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=0)
        
        self.pesquisa = CTkEntry(self, placeholder_text='Nome do Produto', width=150, height=40, font=self.font_entry)
        f_bts_top = CTkFrame(self, corner_radius=25, fg_color='transparent')
        
        self.tv_tabela = Treeview(self, columns=('id', 'cod_barra', 'descricao', 'fornecedor', 'preco_un'),
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
        
        self.scrollbar_vertical = Scrollbar(self, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_pesquisa), size=(32,32)), width=75,height=40).pack(side='left', padx=(5,5))
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_atualizar), size=(32,32)),height=40, width=80).pack(side='left', padx=(5,10))
        
        self.bt_cadastrar = CTkButton(self, image=CTkImage(Image.open(img_add_estoque), size=(32,32)), text='Cadastrar', compound='left', font=self.font_button,height=40, width=140, state='disabled',fg_color='gray',
                                      command=self.abrir_janela_cadEstoque)
        
        self.pesquisa.grid(column=0, row=0, sticky='ew', pady=10, padx=10)
        f_bts_top.grid(column=1, columnspan=2, row=0, sticky='e')
        CTkLabel(self, text='Lista de Produtos não cadastrados em estoque', font=('Segoe UI', 15, 'bold')).grid(column=0, columnspan=2, row=1, sticky='nw', padx=10)
        self.tv_tabela.grid(column=0, row=1 ,columnspan=2, sticky='nsew', pady=(30,0), padx=10)
        self.scrollbar_vertical.grid(row=1, column=1, rowspan=2, sticky='nse',pady=(30, 0), padx=(0,10))
        self.scrollbar_horizontal.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)
        self.bt_cadastrar.grid(column=1, row=3, pady=10, sticky='e', padx=10)
        
        self.tv_tabela.bind('<<TreeviewSelect>>', self.produto_selecionado)
        self.bind('<Button-1>', self.click_fora_da_tabela)
        
    def carregar_produtos(self):
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        produtos = self.produtoDAO.select_produto_n_cad_em_estoque()
        if produtos:
            [self.tv_tabela.insert('', 'end', values=x) for x in produtos]

        
    def produto_selecionado(self, event):
        self.produto_dados = self.tv_tabela.selection()
        if self.produto_dados and self.master.dados_usuario['nivel'] == 'Padrao' or self.master.dados_usuario['nivel'] == 'Administrador':
            self.habilitar_botoes_inferiores()
    
    def click_fora_da_tabela(self, event):
        if event.widget not in (self.tv_tabela, self.bt_cadastrar) and self.focus_get() is self.tv_tabela:
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
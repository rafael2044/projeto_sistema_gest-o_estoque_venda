from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton,CTkFrame, CTkComboBox, CTkTabview, CTkFont, CTkImage
from tkinter.ttk import Treeview, Scrollbar
from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from Estoque.modulos.TelaEditarProduto import TelaEditarProduto
from Estoque.modulos.TelaCadProduto import CadProduto
from Popup.MensagemAlerta import MensagemAlerta
from Imagens.img import img_cadastrar, img_editar, img_excluir, img_pesquisa, img_atualizar, img_add_produto
from PIL import Image
class TelaProduto(CTkToplevel):
    
    def __init__(self, master=None):
        CTkToplevel.__init__(self, master=master, takefocus=True)
        self.master=master
        self.after(100, self.lift)
        self.title('Produtos')
        self.fornecedorDAO = fornecedorDAO()
        self.produtoDAO = produtoDAO()
        self.cad_produto = None
        self.centralizar_janela()
        self.carreagar_widgets()
        self.editar_prod = None
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = 800
        WEIDTH = 900
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//4.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carreagar_widgets(self):
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
        
        
        f_bts_top = CTkFrame(self, corner_radius=25, fg_color='transparent')
        f_bts_bottom = CTkFrame(self, corner_radius=25, fg_color='transparent')
        
        self.pesquisa = CTkEntry(self, placeholder_text='Nome do Produto', font=self.font_entry, height=40)
        
        
        self.tv_tabela = Treeview(self, columns=('id', 'cod_barra', 'descricao', 'fornecedor', 'preco_un'),
                                  selectmode='browse', show='headings')
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('cod_barra', text='Cod. Barra')
        self.tv_tabela.heading('descricao', text='Descrição')
        self.tv_tabela.heading('fornecedor', text='Fornecedor')
        self.tv_tabela.heading('preco_un', text='Preço Un')
        
        
        self.tv_tabela.column('#0', width=2, minwidth=2, stretch=True)
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50, anchor='center')
        self.tv_tabela.column('cod_barra', width=175, stretch=True, minwidth=175)
        self.tv_tabela.column('descricao', width=300, stretch=True, minwidth=300)
        self.tv_tabela.column('fornecedor', width=200, stretch=True, minwidth=200)
        self.tv_tabela.column('preco_un', width=150, stretch=True, minwidth=150)        
        
        self.bt_delete = CTkButton(f_bts_bottom, state='disabled', text='Deletar', font=('Segoe UI', 18, 'bold'), 
                                   image=CTkImage(Image.open(img_excluir), size=(32,32)),height=45,width=120,fg_color='#595457', 
                                   compound='left')
        self.bt_editar = CTkButton(f_bts_bottom, state='disabled', text='Editar',font=('Segoe UI', 18, 'bold'),
                                   image=CTkImage(Image.open(img_editar), size=(32,32)), height=45,
                                   width=110,fg_color='#595457',compound='left',command=self.editar_produtor)
        
        self.scrollbar_vertical = Scrollbar(self, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        self.pesquisa.grid(column=0, row=0, padx=10, pady=10, sticky='we')
        f_bts_top.grid(column=1, columnspan=2, row=0, sticky='e')
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_pesquisa), size=(32,32)), width=75,height=40).pack(side='left', padx=(5,5))
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_atualizar), size=(32,32)),height=40, width=80).pack(side='left', padx=(5,10))
        CTkButton(f_bts_top, text='Cadastrar', image=CTkImage(Image.open(img_add_produto), size=(32,32)),font=self.font_button, compound='left',height=40,
                  command=self.abrir_tela_cadastrar_produto).pack(side='left', padx=(5,10))
        
        self.tv_tabela.grid(column=0, row=1, columnspan=2, sticky='wsen', padx=(10,0))
        self.scrollbar_vertical.grid(column=2, row=1, sticky='wns', padx=(0,10))
        self.scrollbar_horizontal.grid(column=0, row=2, sticky='we', columnspan=3, padx=(10,10))
        f_bts_bottom.grid(column=0, columnspan=3, row=3, sticky='we')
        self.bt_editar.pack(anchor='e',side='right', padx=10)
        self.bt_delete.pack(anchor='e',side='right', padx=10, pady=10)
        
        self.tv_tabela.bind('<<TreeviewSelect>>', self.linha_selecionado)
        self.bind('<Button-1>', self.desabilitar_botoes)

        self.carregar_produtos()
        
    def abrir_tela_cadastrar_produto(self):
         if self.cad_produto is None or not self.cad_produto.winfo_exists():
            self.cad_produto = CadProduto(master=self)
            self.cad_produto.transient(self)
         
    
    def carregar_produtos(self):
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        produtos = self.produtoDAO.select_all_produto()
        if produtos:
            [self.tv_tabela.insert('', 'end', values=x) for x in produtos]

    def atualizar_tabela(self):
        self.pesquisa.delete(0,'end')
        self.carregar_produtos()
    
    def pesquisar_produto(self):
        nome = self.pesquisa.get()
        if nome:
            pass

    def editar_produtor(self):
        dados = self.tv_tabela.item(self.item[0], 'values')
        TelaEditarProduto(master=self,dados=list(dados)).transient(self)
             
    def deletar_produto(self):
        nome = self.tv_tabela.item(self.item[0], 'values')[1]
        
    def linha_selecionado(self, event):
        self.item = self.tv_tabela.selection()
        if self.item:
            if self.master.dados_usuario['nivel'] == 'Administrador':
                self.bt_delete.configure(state='enabled')
                self.bt_delete.configure(fg_color=("#3a7ebf", "#1f538d"))
            self.bt_editar.configure(state='enabled')
            self.bt_editar.configure(fg_color=("#3a7ebf", "#1f538d"))
    
    def desabilitar_botoes(self, event):
        if event.widget not in (self.tv_tabela, self.bt_delete, self.bt_editar) and self.focus_get() is self.tv_tabela:
            self.bt_delete.configure(state='disabled')
            self.bt_delete.configure(fg_color='#595457')
            self.bt_editar.configure(state='disabled')
            self.bt_editar.configure(fg_color='#595457')
            self.tv_tabela.selection_set()    
        
    def limpar_entrys(self):
        self.cod_barra.delete(0, 'end')
        self.descricao.delete(0, 'end')
        self.preco_uni.delete(0, 'end')
                        
    def validar_codBarra(self, event):
        text = self.cod_barra.get()
        if text:
            if text[-1] not in '1234567890' or len(text) > 13:
                self.cod_barra.delete(len(text)-1, 'end')
       
    def validar_preco(self, event):
        text = self.preco_uni.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.preco_uni.delete(index_end, 'end')
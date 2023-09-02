from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton,CTkFrame, CTkComboBox, CTkTabview, CTkFont, CTkImage
from tkinter.ttk import Treeview, Scrollbar
from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from Popup.MensagemAlerta import MensagemAlerta
from Imagens.img import img_cadastrar, img_editar, img_excluir, img_pesquisa, img_atualizar, img_add_produto, img_sair
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
        WEIDTH = 1050
        
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
        
        
        self.tv_tabela = Treeview(self, columns=('id', 'cod_barra', 'descricao', 'fornecedor', 'valor_venda', 'valor_custo'),
                                  selectmode='browse', show='headings')
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('cod_barra', text='Cod. Barra')
        self.tv_tabela.heading('descricao', text='Descrição')
        self.tv_tabela.heading('fornecedor', text='Fornecedor')
        self.tv_tabela.heading('valor_venda', text='Valor de venda')
        self.tv_tabela.heading('valor_custo', text='Valor de custo')
        
        
        self.tv_tabela.column('#0', width=2, minwidth=2, stretch=True)
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50, anchor='center')
        self.tv_tabela.column('cod_barra', width=175, stretch=True, minwidth=175)
        self.tv_tabela.column('descricao', width=300, stretch=True, minwidth=300)
        self.tv_tabela.column('fornecedor', width=200, stretch=True, minwidth=200)
        self.tv_tabela.column('valor_venda', width=150, stretch=True, minwidth=150)        
        self.tv_tabela.column('valor_custo', width=150, stretch=True, minwidth=150)   
        
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
 
class CadProduto(CTkToplevel):
    
    def __init__(self, master=None):
        CTkToplevel.__init__(self, master=master, takefocus=True)
        self.master=master
        self.after(100, self.lift)
        self.title('Cadastrar Produto')
        self.fornecedorDAO = fornecedorDAO()
        self.produtoDAO = produtoDAO()
        self.carreagar_widgets()
        self.centralizar_janela()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = 550
        WEIDTH = 600
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//4.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carreagar_widgets(self):
        
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        self.cod_barra = CTkEntry(self, placeholder_text='Codigo de Barra...', width=150, font=self.font_entry, height=40)

        self.descricao = CTkEntry(self, placeholder_text='Descrição do Produto...', width=550, font=self.font_entry, height=40)
    
        self.valor_venda = CTkEntry(self, width=100, font=self.font_entry, placeholder_text='R$...', height=40)
        self.valor_custo = CTkEntry(self, width=100, font=self.font_entry, placeholder_text='R$...', height=40)
        self.fornecedor = CTkComboBox(self, values=self.carregar_fornecedores(), font=self.font_label, state='readonly', height=40, width=350)
        
        self.cod_barra.bind('<KeyPress>', self.validar_codBarra)
        self.valor_venda.bind('<KeyPress>', self.validar_valor_venda)
        self.valor_custo.bind('<KeyPress>', self.validar_valor_custo)
        
        CTkLabel(self, text='Codigo de Barra', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.cod_barra.pack(padx=10, anchor='w')
        CTkLabel(self, text='Descrição', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.descricao.pack(padx=10, anchor='w')
        CTkLabel(self, text='Valor de Venda', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.valor_venda.pack(padx=10, anchor='w')
        CTkLabel(self, text='Valor de Custo', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.valor_custo.pack(padx=10, anchor='w')
        CTkLabel(self, text='Fornecedor', font=self.font_label).pack(anchor='w', padx=10, pady=10)
        self.fornecedor.pack(anchor='w', padx=10)
        
        
        CTkButton(self, text='Cadastrar', font=self.font_button, height=40, command=self.cadastrar_produto, image=CTkImage(Image.open(img_cadastrar), size=(32,32)),
                  compound='left').pack(anchor='w', padx=10, pady=20, side='left')
        CTkButton(self, text='Cancelar', font=self.font_button, height=40, command=self.destroy, image=CTkImage(Image.open(img_sair), size=(32,32)),
                  compound='left').pack(padx=10, pady=20, side='left')

    def cadastrar_produto(self):
        cod_barra = self.cod_barra.get()
        descricao = self.descricao.get()
        valor_venda = float(self.valor_venda.get().replace(',', '.'))
        valor_custo = float(self.valor_custo.get().replace(',', '.'))
        id_fornecedor = int(self.fornecedorDAO.select_id_fornecedor(self.fornecedor.get())[0])
        
        match self.produtoDAO.insert_produto(cod_barra ,descricao , valor_venda, valor_custo, id_fornecedor ):
            case 1:
                MensagemAlerta('Sucesso!', 'O produto foi cadastrado com sucesso!')
                self.master.carregar_produtos()
            case 2:
                MensagemAlerta('Erro!', 'O produto já existe no estoque!')
            case 3:
                MensagemAlerta('Erro!', 'Os campos não foram preenchidos corretamente!')
        
    def carregar_fornecedores(self):
        result = self.fornecedorDAO.select_all_name_fornecedores()
        fornecedores = []
        if result:
            for f in result:
                fornecedores.append(f[0])
            
        return fornecedores
    
    def validar_codBarra(self, event):
        text = self.cod_barra.get()
        if text:
            if text[-1] not in '1234567890' or len(text) > 13:
                self.cod_barra.delete(len(text)-1, 'end')
       
    def validar_valor_venda(self, event):
        text = self.valor_venda.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.valor_venda.delete(index_end, 'end')
             
    def validar_valor_custo(self, event):
        text = self.valor_custo.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.valor_custo.delete(index_end, 'end')
                
class TelaEditarProduto(CTkToplevel):
    
    def __init__(self, master=None, dados=None):
        CTkToplevel.__init__(self, master=master, takefocus=True)
        self.master=master
        self.dados = dados
        self.after(100, self.lift)
        self.title('Cadastrar Novo Produto')
        self.fornecedorDAO = fornecedorDAO()
        self.produtoDAO = produtoDAO()
        self.centralizar_janela()
        self.carreagar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = 540
        WEIDTH = 600
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//4.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carreagar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)
        self.grid_rowconfigure(8, weight=0)
        self.grid_rowconfigure(9, weight=0)
        self.grid_rowconfigure(10, weight=0)
        self.grid_rowconfigure(11, weight=0)
        self.grid_rowconfigure(12, weight=0)
        
        self.id_produto = CTkEntry(self, width=75, font=self.font_entry, height=40)
        self.cod_barra = CTkEntry(self, placeholder_text='Codigo de Barra...', width=150, font=self.font_entry, height=40)
        self.descricao = CTkEntry(self, placeholder_text='Descrição do Produto...', width=550, font=self.font_entry, height=40)
        self.valor_venda = CTkEntry(self, width=100, font=self.font_entry, placeholder_text='R$...', height=40)
        self.valor_custo = CTkEntry(self, width=100, font=self.font_entry, placeholder_text='R$...', height=40)
        self.fornecedor = CTkComboBox(self, values=self.carregar_fornecedores(), font=self.font_label, state='readonly', height=40, width=350)


        self.cod_barra.bind('<KeyPress>', self.validar_codBarra)
        self.valor_venda.bind('<KeyPress>', self.validar_valor_venda)
        self.valor_custo.bind('<KeyPress>', self.validar_valor_custo)
        
        CTkLabel(self, text='ID', font=self.font_label).grid(column=0, row=0, sticky='w', padx=10, pady=5)
        self.id_produto.grid(column=0, row=1, sticky='w', padx=10)
        CTkLabel(self, text='Codigo de Barra', font=self.font_label).grid(column=0, row=2, sticky='w', padx=10, pady=5)
        self.cod_barra.grid(column=0, row=3, sticky='w', padx=10)
        CTkLabel(self, text='Descrição', font=self.font_label).grid(column=0, row=4, sticky='w', padx=10, pady=5)
        self.descricao.grid(column=0, row=5, sticky='w', padx=10)
        CTkLabel(self, text='Valor de Venda', font=self.font_label).grid(column=0, row=6, sticky='w', padx=10, pady=5)
        self.valor_venda.grid(column=0, row=7, sticky='w', padx=10)
        CTkLabel(self, text='Valor de Custo', font=self.font_label).grid(column=0, row=8, sticky='w', padx=10, pady=5)
        self.valor_custo.grid(column=0, row=9, sticky='w', padx=10)
        CTkLabel(self, text='Fornecedor', font=self.font_label).grid(column=0, row=10, sticky='w', padx=10, pady=5)
        self.fornecedor.grid(column=0, row=11, sticky='w', padx=10)
        
        CTkButton(self, text='Salvar Alterações', font=self.font_button, height=40, command=self.atualizar_produto, image=CTkImage(Image.open(img_cadastrar), size=(32,32)),
                  compound='left').grid(column=0, row=12, padx=10, pady=15, sticky='w')
        CTkButton(self, text='Cancelar', font=self.font_button, height=40, command=self.destroy, image=CTkImage(Image.open(img_sair), size=(32,32)),
                  compound='left').grid(column=0, row=12, padx=(0,100), pady=5, sticky='e')
        
        self.carregar_dados()
    def carregar_fornecedores(self):
        result = self.fornecedorDAO.select_all_name_fornecedores()
        fornecedores = []
        if result:
            for f in result:
                fornecedores.append(f[0])
        return fornecedores

    def carregar_dados(self):
        self.id_produto.insert(0, self.dados[0])
        self.cod_barra.insert(0, self.dados[1])
        self.descricao.insert(0, self.dados[2])
        self.valor_venda.insert(0, self.dados[4])
        self.valor_custo.insert(0, self.dados[5])
        self.fornecedor.set(self.dados[3])
        
        self.id_produto.configure(state='disabled')
        self.cod_barra.configure(state='disabled')
    
    def atualizar_produto(self):
        self.dados[2] = self.descricao.get()
        self.dados[4] = float(self.valor_venda.get().replace(',', '.'))
        self.dados[5] = float(self.valor_custo.get().replace(',', '.'))
        self.dados[3] = int(self.fornecedorDAO.select_id_fornecedor(self.fornecedor.get())[0])
        
        if self.produtoDAO.atualizar_produto(*self.dados):
            MensagemAlerta('Sucesso!', 'As alterações do produto foram realizadas!')
            self.master.carregar_produtos()
            self.destroy()
        else:
            MensagemAlerta('Erro!', 'Houve um problema ao realizar as alterações!')
         
    def validar_codBarra(self, event):
        text = self.cod_barra.get()
        if text:
            if text[-1] not in '1234567890' or len(text) > 13:
                self.cod_barra.delete(len(text)-1, 'end')
       
    def validar_valor_venda(self, event):
        text = self.valor_venda.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.valor_venda.delete(index_end, 'end')
             
    def validar_valor_custo(self, event):
        text = self.valor_custo.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.valor_custo.delete(index_end, 'end')
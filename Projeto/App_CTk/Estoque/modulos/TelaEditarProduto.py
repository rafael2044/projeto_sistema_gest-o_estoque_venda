from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton,CTkFrame, CTkComboBox, CTkTabview, CTkFont, CTkImage
from tkinter.ttk import Treeview, Scrollbar
from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from Popup.MensagemAlerta import MensagemAlerta
from Imagens.img import img_cadastrar, img_editar, img_excluir, img_pesquisa, img_atualizar, img_sair
from PIL import Image
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
        HEIGHT = 475
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
        
        
        self.id_produto = CTkEntry(self, width=75, font=self.font_entry, height=40)
        self.cod_barra = CTkEntry(self, placeholder_text='Codigo de Barra...', width=150, font=self.font_entry, height=40)
        self.descricao = CTkEntry(self, placeholder_text='Descrição do Produto...', width=550, font=self.font_entry, height=40)
        self.preco_uni = CTkEntry(self, width=100, font=self.font_entry, placeholder_text='R$...', height=40)
        self.fornecedor = CTkComboBox(self, values=self.carregar_fornecedores(), font=self.font_label, state='readonly', height=40, width=350)


        self.cod_barra.bind('<KeyPress>', self.validar_codBarra)
        self.preco_uni.bind('<KeyPress>', self.validar_preco)
        
        CTkLabel(self, text='ID', font=self.font_label).grid(column=0, row=0, sticky='w', padx=10, pady=5)
        self.id_produto.grid(column=0, row=1, sticky='w', padx=10)
        CTkLabel(self, text='Codigo de Barra', font=self.font_label).grid(column=0, row=2, sticky='w', padx=10, pady=5)
        self.cod_barra.grid(column=0, row=3, sticky='w', padx=10)
        CTkLabel(self, text='Descrição', font=self.font_label).grid(column=0, row=4, sticky='w', padx=10, pady=5)
        self.descricao.grid(column=0, row=5, sticky='w', padx=10)
        CTkLabel(self, text='Preço Unitário', font=self.font_label).grid(column=0, row=6, sticky='w', padx=10, pady=5)
        self.preco_uni.grid(column=0, row=7, sticky='w', padx=10)
        CTkLabel(self, text='Fornecedor', font=self.font_label).grid(column=0, row=8, sticky='w', padx=10, pady=5)
        self.fornecedor.grid(column=0, row=9, sticky='w', padx=10)
        
        CTkButton(self, text='Salvar Alterações', font=self.font_button, height=40, command=self.atualizar_produto, image=CTkImage(Image.open(img_cadastrar), size=(32,32)),
                  compound='left').grid(column=0, row=10, padx=10, pady=15, sticky='w')
        CTkButton(self, text='Cancelar', font=self.font_button, height=40, command=self.destroy, image=CTkImage(Image.open(img_sair), size=(32,32)),
                  compound='left').grid(column=0, row=10, padx=(0,100), pady=5, sticky='e')
        
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
        self.preco_uni.insert(0, self.dados[4])
        self.fornecedor.set(self.dados[3])
        
        self.id_produto.configure(state='disabled')
        self.cod_barra.configure(state='disabled')
    
    def atualizar_produto(self):
        self.dados[2] = self.descricao.get()
        self.dados[4] = float(self.preco_uni.get().replace(',', '.'))
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
       
    def validar_preco(self, event):
        text = self.preco_uni.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.preco_uni.delete(index_end, 'end')
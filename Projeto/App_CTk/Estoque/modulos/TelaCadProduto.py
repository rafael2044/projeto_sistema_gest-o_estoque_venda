from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkImage, CTkFont
from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from Popup.MensagemAlerta import MensagemAlerta
from Imagens.img import img_cadastrar, img_sair
from PIL import Image
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
        HEIGHT = 500
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
    
        self.preco_uni = CTkEntry(self, width=100, font=self.font_entry, placeholder_text='R$...', height=40)
        
        self.fornecedor = CTkComboBox(self, values=self.carregar_fornecedores(), font=self.font_label, state='readonly', height=40, width=350)
        
        self.cod_barra.bind('<KeyPress>', self.validar_codBarra)
        self.preco_uni.bind('<KeyPress>', self.validar_preco)
        
        
        CTkLabel(self, text='Codigo de Barra', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.cod_barra.pack(padx=10, anchor='w')
        CTkLabel(self, text='Descrição', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.descricao.pack(padx=10, anchor='w')
        CTkLabel(self, text='Preço Unitário', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.preco_uni.pack(padx=10, anchor='w')
        CTkLabel(self, text='Fornecedor', font=self.font_label).pack(anchor='w', padx=10, pady=10)
        self.fornecedor.pack(anchor='w', padx=10)
        
        
        CTkButton(self, text='Cadastrar', font=self.font_button, height=40, command=self.cadastrar_produto, image=CTkImage(Image.open(img_cadastrar), size=(32,32)),
                  compound='left').pack(anchor='w', padx=10, pady=20, side='left')
        CTkButton(self, text='Cancelar', font=self.font_button, height=40, command=self.destroy, image=CTkImage(Image.open(img_sair), size=(32,32)),
                  compound='left').pack(padx=10, pady=20, side='left')

    def cadastrar_produto(self):
        cod_barra = self.cod_barra.get()
        descricao = self.descricao.get()
        preco_un = float(self.preco_uni.get().replace(',', '.'))
        id_fornecedor = int(self.fornecedorDAO.select_id_fornecedor(self.fornecedor.get())[0])
        
        match self.produtoDAO.insert_produto(cod_barra ,descricao , preco_un, id_fornecedor ):
            case 1:
                MensagemAlerta('Sucesso!', 'O produto foi cadastrado com sucesso!')
                self.carregar_produtos()
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
       
    def validar_preco(self, event):
        text = self.preco_uni.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.preco_uni.delete(index_end, 'end')
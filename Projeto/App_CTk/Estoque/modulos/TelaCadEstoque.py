from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkFont, CTkImage
from tkinter.ttk import Treeview
from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from DAO.estoqueDAO import estoqueDAO
from Popup.MensagemAlerta import MensagemAlerta
from Imagens.img import img_cadastrar
from PIL import Image
class CadEstoque(CTkToplevel):
    
    def __init__(self, master=None, dados=None):
        CTkToplevel.__init__(self, master=master, takefocus=True)
        self.master=master
        self.dados = dados
        self.after(100, self.lift)
        self.title('Cadastrar Produto em Estoque')
        self.fornecedorDAO = fornecedorDAO()
        self.produtoDAO = produtoDAO()
        self.estoqueDAO = estoqueDAO()
        self.carreagar_widgets()
        self.carregar_dados()
        self.centralizar_janela()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = 680
        WEIDTH = 700
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//4.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carreagar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        self.cod_barra = CTkEntry(self, placeholder_text='', width=150, font=self.font_entry, height=40)

        self.descricao = CTkEntry(self, placeholder_text='', width=550, font=self.font_entry, height=40)
    
        self.preco_uni = CTkEntry(self, width=100, font=self.font_entry, placeholder_text='', height=40)
        
        self.quantidade_min = CTkEntry(self, width=50, font=self.font_entry, height=40)
        
        self.quantidade_atual = CTkEntry(self, width=50, font=self.font_entry, height=40)
        
        self.quantidade_max = CTkEntry(self, width=50, font=self.font_entry, height=40)
        
        self.fornecedor = CTkEntry(self, placeholder_text='', width=200, font=self.font_entry, height=40)
        
        self.quantidade_min.bind('<KeyPress>', self.validar_quant_min)
        self.quantidade_max.bind('<KeyPress>', self.validar_quant_max)
        self.quantidade_atual.bind('<KeyPress>', self.validar_quant_atual)
        
        [self.grid_columnconfigure (x, weight=20) for x in range(15)]
        
        CTkLabel(self, text='Codigo de Barra', font=self.font_label, height=40).grid(column=0, row=0, padx=15, pady=5, sticky='w')
        self.cod_barra.grid(column=0, row=1, padx=15, sticky='w')
        CTkLabel(self, text='Descrição', font=self.font_label, height=40).grid(column=0, row=2, padx=15,pady=5, sticky='w')
        self.descricao.grid(column=0, row=3, padx=15, sticky='w')
        CTkLabel(self, text='Preço Unitário', font=self.font_label, height=40).grid(column=0, row=4, padx=15,pady=5, sticky='w')
        self.preco_uni.grid(column=0, row=5, padx=15, sticky='w')
        CTkLabel(self, text='Quantidade Mínima', font=self.font_label, height=40).grid(column=0, row=6, padx=15,pady=5, sticky='w')
        self.quantidade_min.grid(column=0, row=7, padx=15, sticky='w')
        CTkLabel(self, text='Quantidade Atual', font=self.font_label, height=40).grid(column=0, row=8, padx=15,pady=5, sticky='w')
        self.quantidade_atual.grid(column=0, row=9, padx=15, sticky='w')
        CTkLabel(self, text='Quantidade Máxima', font=self.font_label, height=40).grid(column=0, row=10, padx=15,pady=5, sticky='w')
        self.quantidade_max.grid(column=0, row=11, padx=15, sticky='w')
        CTkLabel(self, text='Fornecedor', font=self.font_label, height=40).grid(column=0, row=12, padx=15, sticky='w')
        self.fornecedor.grid(column=0, row=13, padx=15, sticky='w')
    
        CTkButton(self, text='Cadastrar', font=self.font_button, height=40, compound='left', image=CTkImage(Image.open(img_cadastrar), size=(32,32))).grid(column=0, row=14,
                                                                                                                                                           padx=15, pady=10,
                                                                                                                                                           sticky='w')
        

    def cadastrar_produto(self):
        cod_barra = self.cod_barra.get()
        descricao = self.descricao.get()
        preco_un = float(self.preco_uni.get().replace(',', '.'))
        quant_min = int(self.quantidade_min.get())
        quant_atual = int(self.quantidade_atual.get())
        quant_max = int(self.quantidade_max.get())
        id_fornecedor = int(self.fornecedorDAO.select_id_fornecedor(self.fornecedor.get())[0])
        
        
    def carregar_dados(self):
        self.cod_barra.insert(0, self.dados[1])
        self.descricao.insert(0, self.dados[2])
        self.preco_uni.insert(0, self.dados[3])
        self.fornecedor.insert(0, self.dados[4])
        
        self.cod_barra.configure(state='disabled')
        self.descricao.configure(state='disabled')
        self.preco_uni.configure(state='disabled')
        self.fornecedor.configure(state='disabled')
                        
    def validar_quant_min(self, event):
        text = self.quantidade_min.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890' or len(text) > 5:
                self.quantidade_min.delete(index_end, 'end')
    
    def validar_quant_atual(self, event):
        text = self.quantidade_atual.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890' or len(text) > 5:
                self.quantidade_atual.delete(index_end, 'end')
    
    def validar_quant_max(self, event):
        text = self.quantidade_max.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890' or len(text) > 5:
                self.quantidade_max.delete(index_end, 'end')
          
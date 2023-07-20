from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
from tkinter.ttk import Treeview
class CadProduto(CTkToplevel):
    def __init__(self):
        CTkToplevel.__init__(self, takefocus=True)
        self.lift()
        self.title('Cadastrar Novo Produto')
        self.center_window()
        self.loader_widgets()
        self.after(100, self.lift)
        self.protocol('WM_DELETE_WINDOW', self.destroy)
    def center_window(self):
        HEIGHT = 750
        WEIDTH = 700
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int(W_HEIGHT - HEIGHT*1.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def loader_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=15, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=15)
        self.font_button = CTkFont('Segoe UI', size=15, weight='bold')
        
        
        tabv_main = CTkTabview(self, corner_radius=20)
        tabv_main._segmented_button.configure(font=self.font_label)
        self.tab_cad = tabv_main.add('Cadastrar')
        self.tab_pesq = tabv_main.add('Pesquisar') 
        tabv_main.pack(expand=True, fill='both', padx=10, pady=10)
        self.loader_w_tab_cad()
        
    def loader_w_tab_cad(self):
        
        self.cod_barra = CTkEntry(self.tab_cad, placeholder_text='Codigo de Barra...', width=150, font=self.font_entry)

        self.descricao = CTkEntry(self.tab_cad, placeholder_text='Descrição do Produto...', width=550, font=self.font_entry)
    
        self.preco_uni = CTkEntry(self.tab_cad, width=100, font=self.font_entry, placeholder_text='R$...')
        
        
        self.quantidade_min = CTkEntry(self.tab_cad, width=50, font=self.font_entry)
        
        self.quantidade_atual = CTkEntry(self.tab_cad, width=50, font=self.font_entry)
        
        self.quantidade_max = CTkEntry(self.tab_cad, width=50, font=self.font_entry)
        
        self.fornecedor = CTkComboBox(self.tab_cad, values='', font=self.font_label, state='readonly')
        
        self.cod_barra.bind('<KeyPress>', self.validar_codBarra)
        self.quantidade_min.bind('<KeyPress>', self.validar_quant_min)
        self.quantidade_max.bind('<KeyPress>', self.validar_quant_max)
        self.quantidade_atual.bind('<KeyPress>', self.validar_quant_atual)
        self.preco_uni.bind('<KeyPress>', self.validar_preco)
        
        
        CTkLabel(self.tab_cad, text='Codigo de Barra', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.cod_barra.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Descrição', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.descricao.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Preço Unitário', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.preco_uni.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Quantidade Mínima', font=self.font_label).pack(anchor='w', padx=10, pady=10)
        self.quantidade_min.pack(anchor='w', padx=10)
        CTkLabel(self.tab_cad, text='Quantidade Atual', font=self.font_label).pack(anchor='w', padx=10, pady=10)
        self.quantidade_atual.pack(anchor='w', padx=10)
        CTkLabel(self.tab_cad, text='Quantidade Máxima', font=self.font_label).pack(anchor='w', padx=10, pady=10)
        self.quantidade_max.pack(anchor='w', padx=10)
        CTkLabel(self.tab_cad, text='Fornecedor', font=self.font_label).pack(anchor='w', padx=10, pady=10)
        self.fornecedor.pack(anchor='w', padx=10)
        
        
        CTkButton(self.tab_cad, text='Cadastrar', font=self.font_button).pack(anchor='w', padx=10, pady=20)
        
    def loader_w_tab_pesq(self):
        self.pesquisa = CTkEntry(self.tab_cad, placeholder_text='Nome do Produto', width=150, font=self.font_entry)

        
        
        
    def validar_codBarra(self, event):
        text = self.cod_barra.get()
        if len(text) > 0:
            index_end = len(text) - 1
            if text[-1] not in '1234567890' or len(text) > 13:
                self.cod_barra.delete(index_end, 'end')
    
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
                
    def validar_preco(self, event):
        text = self.preco_uni.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.preco_uni.delete(index_end, 'end')
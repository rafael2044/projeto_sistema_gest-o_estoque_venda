from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
import modulos.cursors as cursor
from tkinter.ttk import Treeview
class CadProduto(CTkToplevel):
    def __init__(self):
        CTkToplevel.__init__(self, takefocus=True)
        self.lift()
        self.title('Cadastrar Produto')
        self.center_window()
        self.loader_widgets()
        self.after(100, self.lift)
        self.protocol('WM_DELETE_WINDOW', self.destroy)
    def center_window(self):
        HEIGHT = 650
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
        f_estoque = CTkFrame(self.tab_cad, fg_color='transparent')
        f_unidade = CTkFrame(self.tab_cad, fg_color='transparent')
        
        self.cod_barra = CTkEntry(self.tab_cad, placeholder_text='Codigo de Barra...', width=150, font=self.font_entry)
        self.categoria = CTkComboBox(self.tab_cad, values=self.get_categorias(), font=self.font_label, width=150, state='readonly')
        self.nome = CTkEntry(self.tab_cad, placeholder_text='Nome do Produto...', width=550, font=self.font_entry)
        self.quantidade_estoque = CTkEntry(f_estoque, width=50, font=self.font_entry)
        self.unidade_estoque = CTkComboBox(f_estoque, values=self.get_unidades(), font=self.font_label, width=75, state='readonly', command=self.alter_un_estoque)
        self.lb_quant = CTkLabel(self.tab_cad, text=f'Quantidade por {self.get_nome_unidade(self.unidade_estoque.get())}', font=self.font_label)
        self.quantidade_un = CTkEntry(f_unidade, width=50, font=self.font_entry)
        self.unidade_un = CTkComboBox(f_unidade, values=self.get_unidades(), font=self.font_label, width=75, state='readonly',command=self.alter_un)
        self.lb_valor = CTkLabel(self.tab_cad, text=f'Valor por {self.get_nome_unidade(self.unidade_estoque.get())}', font=self.font_label)
        self.valor = CTkEntry(self.tab_cad, width=100, font=self.font_entry, placeholder_text='R$...')
        
        self.cod_barra.bind('<KeyPress>', self.validate_codBarra)
        self.quantidade_estoque.bind('<KeyPress>', self.validate_quant_estoque)
        self.quantidade_un.bind('<KeyPress>', self.validate_quant_un)
        self.valor.bind('<KeyPress>', self.validate_valor)
        
        
        CTkLabel(self.tab_cad, text='Codigo de Barra', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.cod_barra.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Categoria', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.categoria.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Nome', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.nome.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Quantidade em Estoque', font=self.font_label).pack(anchor='w', padx=10, pady=10)
        f_estoque.pack(fill='x', padx=10)
        self.quantidade_estoque.pack(side='left')
        self.unidade_estoque.pack(side='left', padx=5)
        self.lb_quant.pack(anchor='w', padx=10, pady=10)
        f_unidade.pack(fill='x', padx=10)
        self.quantidade_un.pack(side='left')
        self.unidade_un.pack(side='left', padx=10)
        self.lb_valor.pack(padx=10, pady=10, anchor='w')
        self.valor.pack(padx=10, anchor='w')
        
        CTkButton(self.tab_cad, text='Cadastrar', font=self.font_button).pack(anchor='w', padx=10, pady=20)
        
    def loader_w_tab_pesq(self):
        self.pesquisa = CTkEntry(self.tab_cad, placeholder_text='Nome do Produto', width=150, font=self.font_entry)

        
        
        
    def validate_codBarra(self, event):
        text = self.cod_barra.get()
        if len(text) > 0:
            index_end = len(text) - 1
            if text[-1] not in '1234567890' or len(text) > 13:
                self.cod_barra.delete(index_end, 'end')
    
    def validate_quant_estoque(self, event):
        text = self.quantidade_estoque.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890' or len(text) > 5:
                self.quantidade_estoque.delete(index_end, 'end')
    
    def validate_quant_un(self, event):
        text = self.quantidade_un.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890' or len(text) > 5:
                self.quantidade_un.delete(index_end, 'end')
    
    def validate_valor(self, event):
        text = self.valor.get()
        if len(text) > 0:
            index_end = len(text) - 1
            
            if text[-1] not in '1234567890,' or len(text) > 10:
                self.valor.delete(index_end, 'end')
    
    def get_categorias(self):
        return [cat['nome'] for cat in cursor.select_all_categoria()]

    def get_nome_unidade(self, un):
        if un:
            nome = cursor.select_medida_nome_por_un(un)
            if nome:
                nome = nome[0]
                return nome['nome']
        return ''
        
    def get_unidades(self):
        return [un['unidade'] for un in cursor.select_all_medida()]
        
    def alter_un_estoque(self, value):
        self.lb_quant.configure(text=f'Quantidade por {self.get_nome_unidade(value)}')
        
    def alter_un(self, value):
        self.lb_valor.configure(text=f'Valor por {self.get_nome_unidade(value)}')
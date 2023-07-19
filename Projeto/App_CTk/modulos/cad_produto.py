from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont


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
        HEIGHT = 700
        WEIDTH = 500
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def loader_widgets(self):
        font_label = CTkFont('Segoe UI', size=15, weight='bold')
        font_entry = CTkFont('Segoe UI', size=15)
        font_button = CTkFont('Segoe UI', size=15, weight='bold')
        
        
        f_main = CTkFrame(self)
        tabv_main = CTkTabview(f_main, corner_radius=20)
        tab_cad = tabv_main.add('Cadastrar')
        tab_pesq = tabv_main.add('Pesquisar') 
        
        self.cod_barra = CTkEntry(tab_cad, placeholder_text='Codigo de Barra...', width=150, font=font_entry)
        self.categoria = CTkComboBox(tab_cad, values=('Pendrive', 'Mouse'), font=font_label, width=150, state='readonly')
        self.nome = CTkEntry(tab_cad, placeholder_text='Nome do Produto...', width=550, font=font_entry)
        f_estoque = CTkFrame(tab_cad, border_color='white', border_width=1, fg_color='transparent')
        self.quantidade = CTkEntry(f_estoque, width=70, font=font_entry)
        self.unidade = CTkComboBox(f_estoque, values=('Un','Cx'), font=font_label, width=60, state='readonly')
        
        self.cod_barra.bind('<KeyPress>', self.validate_codBarra)
        f_main.pack(padx=10, pady=10, expand=True, fill='both')
        tabv_main.pack(expand=True, fill='both')
        CTkLabel(tab_cad, text='Codigo de Barra', font=font_label).pack(padx=10, anchor='w')
        self.cod_barra.pack(padx=10, anchor='w', pady=5)
        CTkLabel(tab_cad, text='Categoria', font=font_label).pack(padx=10, anchor='w', pady=5)
        self.categoria.pack(padx=10, anchor='w')
        CTkLabel(tab_cad, text='Nome', font=font_label).pack(padx=10, anchor='w', pady=5)
        self.nome.pack(padx=10, anchor='w')
        CTkLabel(tab_cad, text='Estoque', font=font_label).pack(padx=10, anchor='w', pady=5)
        f_estoque.pack(fill='x', padx=10)
        CTkLabel(f_estoque, text='Quantidade em Estoque:', font=font_label).pack(side='left', padx=2, pady=5)
        self.quantidade.pack(side='left', padx=10)
        self.unidade.pack(side='left')
    def validate_codBarra(self, event):
        text = self.cod_barra.get()
        index_end = len(text) - 1
        if text[-1] not in '1234567890' or len(text) > 13:
            self.cod_barra.delete(index_end, 'end')
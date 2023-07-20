from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
from tkinter.ttk import Treeview
class WFornecedor(CTkToplevel):
    def __init__(self):
        CTkToplevel.__init__(self, takefocus=True)
        self.lift()
        self.title('Fornecedores')
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
        self.tab_pesq = tabv_main.add('Pesquisar')
        self.tab_cad = tabv_main.add('Cadastrar') 
        tabv_main.pack(expand=True, fill='both', padx=10, pady=10)
        self.loader_w_tab_cad()
        self.loader_w_tab_pesq()
        
    def loader_w_tab_cad(self):
        
        self.nome = CTkEntry(self.tab_cad, placeholder_text='Digite o nome do Fornecedor...', font=self.font_entry)
    
        self.contato = CTkEntry(self.tab_cad, width=200, font=self.font_entry, placeholder_text='Digite o Contato...')
        
        self.endereço = CTkEntry(self.tab_cad, font=self.font_entry, placeholder_text='Digite o Endereço...')
        
        
        CTkLabel(self.tab_cad, text='Fornecedor', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.nome.pack(padx=10, anchor='w', fill='x')
        CTkLabel(self.tab_cad, text='Contato', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.contato.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Endereço', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.endereço.pack(padx=10, anchor='w', fill='x')
      
        
        CTkButton(self.tab_cad, text='Cadastrar', font=self.font_button).pack(anchor='w', padx=10, pady=20)
        
    def loader_w_tab_pesq(self):
        self.pesquisa = CTkEntry(self.tab_pesq, placeholder_text='Nome do Produto', width=150, font=self.font_entry)

        self.tv_tabela = Treeview(self.tab_pesq, columns=('id', 'nome', 'contato','endereco'))
        self.tv_tabela.column('#0', width=2, stretch=True, minwidth=2) 
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50)
        self.tv_tabela.column('nome', width=300, stretch=False, minwidth=300)
        self.tv_tabela.column('contato', width=150, stretch=True, minwidth=150)
        self.tv_tabela.column('endereco', width=250, stretch=False, minwidth=250)
        
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID', anchor='center')
        self.tv_tabela.heading('nome', text='Nome')
        self.tv_tabela.heading('contato', text='Contato')
        self.tv_tabela.heading('endereco', text='Endereço')
        
        self.pesquisa.pack(pady=5)
        self.tv_tabela.pack(fill='both', expand=True)
        
    def carregar_tab_fornecedores(self):
        pass
    
    def pesquisar_fornecedor(self):
        pass
    
    def cadastrar_fornecedor(self):
        pass
    
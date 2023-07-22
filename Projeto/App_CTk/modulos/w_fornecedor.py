from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
from tkinter.ttk import Treeview, Scrollbar, Style
from modulos.DAO.fornecedorDAO import fornecedorDAO
from modulos.pop_up import AlertMessage
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
        WEIDTH = 750
        
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
        
        self.endereco = CTkEntry(self.tab_cad, font=self.font_entry, placeholder_text='Digite o Endereço...')
        
        
        CTkLabel(self.tab_cad, text='Fornecedor', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.nome.pack(padx=10, anchor='w', fill='x')
        CTkLabel(self.tab_cad, text='Contato', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.contato.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Endereço', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.endereco.pack(padx=10, anchor='w', fill='x')
      
        
        CTkButton(self.tab_cad, text='Cadastrar', font=self.font_button, command=self.cadastrar_fornecedor).pack(anchor='w', padx=10, pady=20)
        
    def loader_w_tab_pesq(self):
        self.style = Style()
        self.style.configure('Treeview', font=('Segoe UI', 15), rowheight=30)
        self.style.configure('Treeview.Heading', font=('Segoe UI', 13))
        self.style.layout('Treeview', [('Treeview.treearea', {'sticky':'nswe'})])
        
        self.pesquisa = CTkEntry(self.tab_pesq, placeholder_text='Nome do Produto', width=150, font=self.font_entry)

        f_tabela = CTkFrame(self.tab_pesq, fg_color='transparent')
        self.tv_tabela = Treeview(f_tabela, columns=('id', 'nome', 'contato','endereco'))
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
        
        self.scrollbar_vertical = Scrollbar(f_tabela, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self.tab_pesq, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        
        self.bt_delete = CTkButton(self.tab_pesq, state='disabled', text='Excluir', command=self.deletar_fornecedor)
        
        self.pesquisa.pack(pady=5)
        f_tabela.pack(fill='both', expand=True)
        self.tv_tabela.pack(fill='both', expand=True, side='left', anchor='w')
        self.scrollbar_vertical.pack(anchor='w', fill='y', expand=True)
        self.scrollbar_horizontal.pack(fill='x', anchor='s')
        self.bt_delete.pack(anchor='e', padx=10)
        
        
        
        
        self.carregar_tabela_fornecedores()
        self.tv_tabela.bind('<<TreeviewSelect>>', self.item_selecionado)
        
    def carregar_tabela_fornecedores(self):
        result = fornecedorDAO.select_all_fornecedores()
        
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        
        for f in result:
            self.tv_tabela.insert('', 'end', values=f)
    
    def pesquisar_fornecedor(self):
        pass
    
    def cadastrar_fornecedor(self):
        nome = self.nome.get()
        contato = self.contato.get()
        endereco = self.endereco.get()
        
        if nome and contato:
            if fornecedorDAO.insert_fornecedor(nome, contato, endereco):
                AlertMessage('Cadastro', 'Cadastro Realizado com Sucesso!')
                self.carregar_tabela_fornecedores()
            else:
                AlertMessage('Cadastro', 'Erro ao realizar cadastro!')

    def deletar_fornecedor(self):
        pass

    def item_selecionado(self, event):
        item = self.tv_tabela.selection()[0]
        if item:
            self.bt_delete.configure(state='enabled')
        
        
        
    
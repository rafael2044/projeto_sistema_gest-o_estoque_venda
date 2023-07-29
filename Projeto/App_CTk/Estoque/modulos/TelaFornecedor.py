from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
from tkinter.ttk import Treeview, Scrollbar, Style
from DAO.fornecedorDAO import fornecedorDAO
from Estoque.modulos.TelaEditarFornecedor import EditarFornecedor
from Popup.MensagemAlerta import MensagemAlerta
from Popup.DialogoSimNao import DialogoSimNao
from tkinter import PhotoImage
from Imagens.img import icon_pesquisa, icon_atualizar, icon_excluir, icon_editar

class WFornecedor(CTkToplevel):
    
    def __init__(self):
        CTkToplevel.__init__(self, takefocus=True)
        self.after(100, self.lift)
        self.title('Fornecedores')
        self.fornecedorDAO = fornecedorDAO()
        self.centralizar_janela()
        self.carregar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT = 750
        WEIDTH = 850
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//4.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        tabv_main = CTkTabview(self, corner_radius=20)
        tabv_main._segmented_button.configure(font=self.font_label)
        self.tab_pesq = tabv_main.add('Pesquisar')
        self.tab_cad = tabv_main.add('Cadastrar') 
        tabv_main.pack(expand=True, fill='both', padx=10, pady=10)
        self.carregar_w_tab_cad()
        self.carregar_w_tab_pesq()
        
    def carregar_w_tab_cad(self):
        
        self.nome = CTkEntry(self.tab_cad, placeholder_text='Digite o nome do Fornecedor...', font=self.font_entry, height=40)
    
        self.contato = CTkEntry(self.tab_cad, width=200, font=self.font_entry, placeholder_text='Digite o Contato...', height=40)
        
        self.endereco = CTkEntry(self.tab_cad, font=self.font_entry, placeholder_text='Digite o Endereço...', height=40)
        
        
        CTkLabel(self.tab_cad, text='Fornecedor', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.nome.pack(padx=10, anchor='w', fill='x')
        CTkLabel(self.tab_cad, text='Contato', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.contato.pack(padx=10, anchor='w')
        CTkLabel(self.tab_cad, text='Endereço', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.endereco.pack(padx=10, anchor='w', fill='x')
      
        
        CTkButton(self.tab_cad, text='Cadastrar', font=self.font_button, command=self.cadastrar_fornecedor, height=40).pack(anchor='w', padx=10, pady=20)
        
    def carregar_w_tab_pesq(self):
        self.style = Style()
        self.style.configure('Treeview', font=('Segoe UI', 15), rowheight=30)
        self.style.configure('Treeview.Heading', font=('Segoe UI', 13))
        self.style.layout('Treeview', [('Treeview.treearea', {'sticky':'nswe'})])
        f_pesquisa = CTkFrame(self.tab_pesq, corner_radius=25, fg_color='transparent')
        
        self.pesquisa = CTkEntry(f_pesquisa, placeholder_text='Nome do Produto', width=150,height=40, font=self.font_entry)

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
        
        
        self.bt_delete = CTkButton(self.tab_pesq, state='disabled', text='', image=PhotoImage(data=icon_excluir),width=40,fg_color='gray', command=self.deletar_fornecedor)
        self.bt_editar = CTkButton(self.tab_pesq, state='disabled', text='', image=PhotoImage(data=icon_editar),command=self.editar_fornecedor, width=40,fg_color='gray')
        f_pesquisa.pack(fill='x', pady=(2,5))
        self.pesquisa.pack(fill='x',side='left', expand=True, padx=(10,5), pady=(1,1))
        CTkButton(f_pesquisa, text='', image=PhotoImage(data=icon_pesquisa), width=50,height=40, command=self.pesquisar_fornecedor).pack(side='left', padx=(5,5))
        CTkButton(f_pesquisa, text='', image=PhotoImage(data=icon_atualizar), width=50,height=40, command=self.atualizar_tabela).pack(side='left', padx=(5,10))
        f_tabela.pack(fill='both', expand=True)
        self.tv_tabela.pack(fill='both', expand=True, side='left', anchor='w', padx=(10,0))
        self.scrollbar_vertical.pack(anchor='w', fill='y', expand=True, padx=(0, 10))
        self.scrollbar_horizontal.pack(fill='x', anchor='s', padx=10, pady=(0,5))
        self.bt_editar.pack(anchor='e',side='right', padx=10)
        self.bt_delete.pack(anchor='e',side='right', padx=10, pady=10)

        self.carregar_tab_fornecedores()
        self.tv_tabela.bind('<<TreeviewSelect>>', self.linha_selecionado)
        self.bind('<Button-1>', self.desabilitar_botoes)
        
    def carregar_tab_fornecedores(self, lista=None):
        result = lista
        if not lista:
            result = self.fornecedorDAO.select_all_fornecedores()
        
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        
        for f in result:
            self.tv_tabela.insert('', 'end', values=f)
    
    def pesquisar_fornecedor(self):
        nome = self.pesquisa.get()
        if nome:
            result = self.fornecedorDAO.select_like_fornecedor(nome)
            self.carregar_tab_fornecedores(result)
            
    def cadastrar_fornecedor(self):
        nome = self.nome.get()
        contato = self.contato.get()
        endereco = self.endereco.get()
        match (self.fornecedorDAO.insert_fornecedor(nome, contato, endereco)):
            case 1:
                MensagemAlerta('Cadastro', 'Cadastro Realizado com Sucesso!')
                self.carregar_tab_fornecedores()
            case 2:
                MensagemAlerta('Erro ao Cadastrar', 'Fornecedor já existe!')
            case 3:
                MensagemAlerta('Erro ao Cadastrar', 'Nome ou Contato Inválidos!')

    def editar_fornecedor(self):
        dados = self.tv_tabela.item(self.item[0], 'values')
        EditarFornecedor(self, dados)
        

    def deletar_fornecedor(self):
        nome = self.tv_tabela.item(self.item[0], 'values')[1]
        op = DialogoSimNao('Alerta!', f'Deseja Excluir o fornecedor {nome}?')
        if op.opcao:
            fornecedorDAO.delete_fornecedor(nome)
            self.carregar_tab_fornecedores()

    def linha_selecionado(self, event):
        self.item = self.tv_tabela.selection()
        if self.item:
            self.bt_delete.configure(state='enabled')
            self.bt_delete.configure(fg_color=("#3a7ebf", "#1f538d"))
            self.bt_editar.configure(state='enabled')
            self.bt_editar.configure(fg_color=("#3a7ebf", "#1f538d"))
    
    def desabilitar_botoes(self, event):
        if event.widget not in (self.tv_tabela, self.bt_delete, self.bt_editar) and self.focus_get() is self.tv_tabela:
            self.bt_delete.configure(state='disabled')
            self.bt_delete.configure(fg_color='gray')
            self.bt_editar.configure(state='disabled')
            self.bt_editar.configure(fg_color='gray')
            self.tv_tabela.selection_set()
        
    def atualizar_tabela(self):
        self.pesquisa.delete(0,'end')
        self.carregar_tab_fornecedores() 
        
    
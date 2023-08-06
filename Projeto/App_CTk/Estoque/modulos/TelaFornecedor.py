from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkTabview, CTkFont, CTkImage
from tkinter.ttk import Treeview, Scrollbar
from DAO.fornecedorDAO import fornecedorDAO
from Estoque.modulos.TelaEditarFornecedor import EditarFornecedor
from Popup.MensagemAlerta import MensagemAlerta
from Popup.DialogoSimNao import DialogoSimNao
from PIL import Image
from Imagens.img import img_pesquisa, img_atualizar, img_excluir, img_editar, img_cadastrar

class TelaFornecedor(CTkToplevel):
    
    def __init__(self, master=None):
        CTkToplevel.__init__(self, master=master, takefocus=True)
        self.master = master
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
        
        self.tab_cad.grid_columnconfigure(0, weight=1)
        self.tab_cad.grid_rowconfigure(0, weight=0)
        self.tab_cad.grid_rowconfigure(1, weight=0)
        self.tab_cad.grid_rowconfigure(2, weight=0)
        self.tab_cad.grid_rowconfigure(3, weight=0)
        self.tab_cad.grid_rowconfigure(4, weight=0)
        self.tab_cad.grid_rowconfigure(5, weight=0)
        self.tab_cad.grid_rowconfigure(6, weight=0)
        
        self.nome = CTkEntry(self.tab_cad, placeholder_text='Digite o nome do Fornecedor...', font=self.font_entry, height=40)
    
        self.contato = CTkEntry(self.tab_cad, width=200, font=self.font_entry, placeholder_text='Digite o Contato...', height=40)
        
        self.endereco = CTkEntry(self.tab_cad, font=self.font_entry, placeholder_text='Digite o Endereço...', height=40)
        
        CTkLabel(self.tab_cad, text='Fornecedor', font=self.font_label).grid(padx=10, sticky='w', pady=10, column=0, row=0)
        self.nome.grid(padx=10, sticky='we', column=0, row=1)
        CTkLabel(self.tab_cad, text='Contato', font=self.font_label).grid(padx=10, sticky='w', pady=10, column=0, row=2)
        self.contato.grid(padx=10, sticky='w', column=0, row=3)
        CTkLabel(self.tab_cad, text='Endereço', font=self.font_label).grid(padx=10, sticky='w', pady=10, column=0, row=4)
        self.endereco.grid(padx=10, sticky='we', column=0, row=5)
      
        
        CTkButton(self.tab_cad, text='Cadastrar', image = CTkImage(Image.open(img_cadastrar)),compound='left',
                  font=self.font_button, command=self.cadastrar_fornecedor, height=40).grid(padx=10, sticky='w', pady=10, column=0, row=6)
        
    def carregar_w_tab_pesq(self):
        
        self.tab_pesq.grid_columnconfigure(0, weight=3)
        self.tab_pesq.grid_columnconfigure(1, weight=1)
        self.tab_pesq.grid_columnconfigure(2, weight=0)
        self.tab_pesq.grid_rowconfigure(0, weight=0)
        self.tab_pesq.grid_rowconfigure(1, weight=1)
        self.tab_pesq.grid_rowconfigure(2, weight=0)
        self.tab_pesq.grid_rowconfigure(3, weight=0)
        
        
        f_bts_top = CTkFrame(self.tab_pesq, corner_radius=25, fg_color='transparent')
        f_bts_bottom = CTkFrame(self.tab_pesq, corner_radius=25, fg_color='transparent')
        
        self.pesquisa = CTkEntry(self.tab_pesq, placeholder_text='Nome do fornecedor', width=150,height=40, font=self.font_entry)

        self.tv_tabela = Treeview(self.tab_pesq, columns=('id', 'nome', 'contato','endereco'), show='headings')
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
        
        self.scrollbar_vertical = Scrollbar(self.tab_pesq, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self.tab_pesq, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        
        self.bt_delete = CTkButton(f_bts_bottom, state='disabled', text='Deletar', font=('Segoe UI', 18, 'bold'), 
                                   image=CTkImage(Image.open(img_excluir), size=(32,32)),height=45,width=120,fg_color='#595457', 
                                   command=self.deletar_fornecedor,compound='left')
        self.bt_editar = CTkButton(f_bts_bottom, state='disabled', text='Editar',font=('Segoe UI', 18, 'bold'),
                                   image=CTkImage(Image.open(img_editar), size=(32,32)),command=self.editar_fornecedor, height=45,
                                   width=110,fg_color='#595457',compound='left')
        
        
        self.pesquisa.grid(column=0, row=0, padx=10, pady=10, sticky='we')
        f_bts_top.grid(column=1, columnspan=2, row=0, sticky='e')
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_pesquisa), size=(32,32)), width=75,height=40, 
                  command=self.pesquisar_fornecedor).pack(side='left', padx=(5,5))
        CTkButton(f_bts_top, text='', image=CTkImage(Image.open(img_atualizar), size=(32,32)), width=75,height=40, 
                  command=self.atualizar_tabela).pack(side='left', padx=(5,10))
        
        self.tv_tabela.grid(column=0, row=1, columnspan=2, sticky='wsen', padx=(10,0))
        self.scrollbar_vertical.grid(column=2, row=1, sticky='wns', padx=(0,10))
        self.scrollbar_horizontal.grid(column=0, row=2, sticky='we', columnspan=3, padx=(10,10))
        f_bts_bottom.grid(column=0, columnspan=3, row=3, sticky='we')
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
                MensagemAlerta('Erro ao Cadastrar', 'Nome e/ou Contato Inválidos!')

    def editar_fornecedor(self):
        dados = self.tv_tabela.item(self.item[0], 'values')
        EditarFornecedor(self, dados)
        

    def deletar_fornecedor(self):
        nome = self.tv_tabela.item(self.item[0], 'values')[1]
        op = DialogoSimNao('Alerta!', f'Deseja Excluir o fornecedor {nome}?')
        if op.opcao:
            self.fornecedorDAO.delete_fornecedor(nome)
            self.carregar_tab_fornecedores()

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
        
    def atualizar_tabela(self):
        self.pesquisa.delete(0,'end')
        self.carregar_tab_fornecedores() 
        
    
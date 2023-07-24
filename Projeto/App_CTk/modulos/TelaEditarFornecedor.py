from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
from modulos.DAO.fornecedorDAO import fornecedorDAO
from modulos.MensagemAlerta import MensagemAlerta
class EditarFornecedor(CTkToplevel):
    def __init__(self, master, dados:list):
        CTkToplevel.__init__(self)
        self.master =master
        self.dados = list(dados)
        self.lift()
        self.title('Editar Fornecedor')
        self.centralizar_janela()
        self.carregar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT =500
        WEIDTH = 450
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int(W_HEIGHT - HEIGHT*1.3)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        frame = CTkFrame(self)
        frame.pack(padx=10, pady=10, fill='both')
        self.nome = CTkEntry(frame, placeholder_text='Digite o nome do Fornecedor...', font=self.font_entry, height=40)
    
        self.contato = CTkEntry(frame, width=200, font=self.font_entry, placeholder_text='Digite o Contato...', height=40)
        
        self.endereco = CTkEntry(frame, font=self.font_entry, placeholder_text='Digite o Endereço...', height=40)    
        
        CTkLabel(frame, text='Fornecedor', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.nome.pack(padx=10, anchor='w', fill='x')
        CTkLabel(frame, text='Contato', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.contato.pack(padx=10, anchor='w')
        CTkLabel(frame, text='Endereço', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.endereco.pack(padx=10, anchor='w', fill='x')
      
        
        CTkButton(frame, text='Salvar Alteracoes', font=self.font_button, height=40, command=self.salvar_alterecoes).pack(anchor='w', padx=10, pady=20)
        self.carregar_dados()
        print(self.dados)
        
    def carregar_dados(self):
        self.nome.insert(0, self.dados[1])
        self.contato.insert(0, self.dados[2])
        if self.dados[-1] != '':
            self.endereco.insert(0, self.dados[3])
            
    def salvar_alterecoes(self):
        self.dados[1] = self.nome.get()
        self.dados[2] = self.contato.get()
        self.dados[3] = self.endereco.get()
        
        if fornecedorDAO().atualizar_fornecedor(*self.dados):
            MensagemAlerta('Sucesso!', 'Alteracoes realizadas com sucesso!')
        else:
            MensagemAlerta('Erro!', 'Aconteceu um erro ao realizar as alteracoes!')
        self.master.carregar_tab_fornecedores()
        self.destroy()
    
            
        
        
        
        
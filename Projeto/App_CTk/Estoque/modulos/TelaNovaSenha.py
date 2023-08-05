from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTk, CTkLabel, CTkFont
from Popup.MensagemAlerta import MensagemAlerta
from DAO.usuarioDAO import usuarioDAO
class NovaSenha(CTkToplevel):
    def __init__(self, usuario):
        CTkToplevel.__init__(self)
        self.usuario = usuario
        self.title('Nova Senha')
        self.usuarioDAO = usuarioDAO()
        self.centralizar_janela()
        self.resizable(False, False)
        self.carregar_widgets()
        self.grab_set()
        self.protocol('WM_DELETE_WINDOW', self.sair)
        self.bind('<Return>', self.inserir)
        
    def centralizar_janela(self):
        HEIGHT = 260
        WEIDTH = 300
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')    
    
    def carregar_widgets(self):
        font_label = CTkFont('Segoe UI', size=18, weight='bold')
        font_entry = CTkFont('Segoe UI', size=16)
        font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        f_main = CTkFrame(self)
        f_button = CTkFrame(f_main, fg_color='transparent')
        self.password = CTkEntry(f_main, placeholder_text='Digite a Senha...', height=40, font=font_entry, takefocus=True, show='*')
        self.password_validacao = CTkEntry(f_main, show='*', placeholder_text='Digite a Senha novamente...', height=40, font=font_entry)
        
        self.bt_inserir = CTkButton(f_button, text='Inserir', font=font_button, command=self.inserir, height=40)
        self.bt_sair = CTkButton(f_button, text='Sair', font=font_button, command=self.sair,height=40)
        
        f_main.pack(padx=10,pady=10, expand=True, fill = 'both')
        CTkLabel(f_main, text='Senha', font=font_label).pack(padx=10, pady=5, anchor='w')
        self.password.pack(padx=10, anchor='w', fill='x')
        CTkLabel(f_main, text='Validar Senha',font=font_label).pack(padx=10, pady=5, anchor='w')
        self.password_validacao.pack(padx=10, anchor='w', fill='x')
        f_button.pack(padx=10, pady=(10,5))
        self.bt_inserir.pack(padx=(0,20), side='left')
        self.bt_sair.pack(padx=(20,0), side='left')
        
    def inserir(self, event=None):
        senha = self.password.get()
        validar_senha = self.password_validacao.get()
        
        if senha == validar_senha:
            self.usuarioDAO.nova_senha(self.usuario, senha)
            MensagemAlerta('Sucesso', 'Senha inserida com sucesso!')
            self.destroy()
        else:
            MensagemAlerta('Erro', 'As senhas precisam ser iguais!')
        
    def sair(self):
        self.destroy()


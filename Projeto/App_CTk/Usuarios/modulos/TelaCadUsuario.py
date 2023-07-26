from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTk, CTkLabel, CTkFont, CTkComboBox
from modulos.MensagemAlerta import MensagemAlerta
from modulos.DAO.usuarioDAO import usuarioDAO
class CadUsuario(CTkToplevel):
    def __init__(self, master):
        CTkToplevel.__init__(self)
        self.master = master
        self.title('Cadastrar Usuario')
        self.centralizar_janela()
        self.resizable(False, False)
        self.carregar_widgets()
        self.transient(master)
        self.protocol('WM_DELETE_WINDOW', self.sair)
        
    def centralizar_janela(self):
        HEIGHT = 350
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
        
        self.tipos = {'Padrão':1, 'Administrador':2}
        
        f_main = CTkFrame(self)
        f_button = CTkFrame(f_main, fg_color='transparent')
        self.user = CTkEntry(f_main, placeholder_text='Digite o Usuario...', width=250, height=40, font=font_entry)
        self.password = CTkEntry(f_main, show='*', placeholder_text='Digite a Senha...', width=250, height=40, font=font_entry)
        self.cb_tipo = CTkComboBox(f_main, values=[x for x in self.tipos], font=font_label, state='readonly')
        self.bt_cadastrar = CTkButton(f_button, text='Cadastrar', font=font_button, command=self.cadastrar, height=40)
        self.bt_sair = CTkButton(f_button, text='Sair', font=font_button, command=self.sair,height=40)
        
        f_main.pack(padx=10,pady=10, expand=True, fill = 'both')
        CTkLabel(f_main, text='Usuario', font=font_label).pack(padx=10, pady=5, anchor='w')
        self.user.pack(padx=10, anchor='w')
        CTkLabel(f_main, text='Senha',font=font_label).pack(padx=10, pady=5, anchor='w')
        self.password.pack(padx=10, anchor='w')
        CTkLabel(f_main, text='Tipo', font=font_label).pack(padx=10, pady=5, anchor='w')
        self.cb_tipo.pack(padx=10, anchor='w')
        f_button.pack(padx=10, pady=20)
        self.bt_cadastrar.pack(padx=10, side='left')
        self.bt_sair.pack(padx=20, side='left')
        
    def cadastrar(self, event=None):
        user = self.user.get()
        password = self.password.get()
        tipo = self.tipos[self.cb_tipo.get()]
        
        match usuarioDAO.insert_usuario(user, password, tipo):
            
            case 1:
                MensagemAlerta('Sucesso', 'Usuario cadastrado com sucesso!')
                self.master.carregar_usuarios()
                self.sair()
            case 2:
                MensagemAlerta('Erro', 'Usuario já existe!')
            case 3:
                MensagemAlerta('Erro', 'Os campos não estão completamente preenchidos')
        
    def sair(self):
        self.destroy()


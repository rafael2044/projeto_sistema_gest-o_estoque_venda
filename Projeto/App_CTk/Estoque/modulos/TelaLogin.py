from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTk, CTkLabel, CTkFont
from Popup.MensagemAlerta import MensagemAlerta
from DAO.usuarioDAO import usuarioDAO
from Estoque.modulos.TelaNovaSenha import NovaSenha

class Login(CTkToplevel):
    def __init__(self, master):
        CTkToplevel.__init__(self)
        self.master = master
        self.title('Login Sistema')
        self.usuarioDAO = usuarioDAO()
        self.centralizar_janela()
        self.resizable(False, False)
        self.carregar_widgets()
        self.grab_set()
        self.user.focus_set()
        self.protocol('WM_DELETE_WINDOW', self.sair)
        self.bind('<Return>', self.logar)
        
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
        self.user = CTkEntry(f_main, placeholder_text='Digite o Usuario...', height=40, font=font_entry, takefocus=True)
        self.password = CTkEntry(f_main, show='*', placeholder_text='Digite a Senha...', height=40, font=font_entry)
        
        self.bt_entrar = CTkButton(f_button, text='Entrar', font=font_button, command=self.logar, height=40)
        self.bt_sair = CTkButton(f_button, text='Sair', font=font_button, command=self.sair,height=40)
        
        f_main.pack(padx=10,pady=10, expand=True, fill = 'both')
        CTkLabel(f_main, text='Usuario', font=font_label).pack(padx=10, pady=5, anchor='w')
        self.user.pack(padx=10, anchor='w', fill='x')
        CTkLabel(f_main, text='Senha',font=font_label).pack(padx=10, pady=5, anchor='w')
        self.password.pack(padx=10, anchor='w', fill='x')
        f_button.pack(padx=10, pady=(10,5))
        self.bt_entrar.pack(padx=(0,20), side='left')
        self.bt_sair.pack(padx=(20,0), side='left')
        
    def logar(self, event=None):
        user = self.user.get()
        password = self.password.get()
        
        match self.usuarioDAO.validar_usuario(user, password):
            case 1:
                self.limpar_entrys()
                self.master.tipo_usuario = self.usuarioDAO.select_tipo_usuario(user)[0]
                self.master.usuario.configure(text=user)
                self.master.verificar_restricoes_usuario()
                self.master.carregar_estoque()
                self.grab_release()
                self.withdraw()
            case 2:
                MensagemAlerta('Login Invalido', 'Usuario ou Senha invalidos!')
            case 3:
                NovaSenha(user)
        
    def limpar_entrys(self):
        self.user.delete(0, 'end')
        self.password.delete(0, 'end')
        
    def sair(self):
        self.quit()


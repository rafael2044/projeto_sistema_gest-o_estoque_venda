from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTk, CTkLabel, CTkFont
from Popup.MensagemAlerta import MensagemAlerta
from DAO.usuarioDAO import usuarioDAO
class ResetarSenha(CTkToplevel):
    def __init__(self, master):
        CTkToplevel.__init__(self)
        self.master = master
        self.title('Resetar Senha')
        self.centralizar_janela()
        self.carregar_widgets()
        self.transient(master)
        self.protocol('WM_DELETE_WINDOW', self.sair)
        self.bind('<Return>', self.resetar)
        
    def centralizar_janela(self):
        HEIGHT = 260
        WEIDTH = 300
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        self.resizable(False, False)   
    
    def carregar_widgets(self):
        font_label = CTkFont('Segoe UI', size=18, weight='bold')
        font_entry = CTkFont('Segoe UI', size=16)
        font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        f_main = CTkFrame(self)
        f_button = CTkFrame(f_main, fg_color='transparent')
        self.user = CTkEntry(f_main, placeholder_text='Digite o Usuario...', width=250, height=40, font=font_entry, takefocus=True)
        self.bt_resetar = CTkButton(f_button, text='Resetar', font=font_button, command=self.resetar, height=40)
        self.bt_sair = CTkButton(f_button, text='Sair', font=font_button, command=self.sair,height=40)
        
        f_main.pack(padx=10,pady=10, expand=True, fill = 'both')
        CTkLabel(f_main, text='Usuario', font=font_label).pack(padx=10, pady=5, anchor='w')
        self.user.pack(padx=10, anchor='w')
        CTkLabel(f_main, text='Senha',font=font_label).pack(padx=10, pady=5, anchor='w')
        f_button.pack(padx=10, pady=20)
        self.bt_resetar.pack(padx=10, side='left')
        self.bt_sair.pack(padx=20, side='left')
        
    def resetar(self, event=None):
        user = self.user.get()
        match usuarioDAO().resetar_senha(user):
            case 1:
                MensagemAlerta('Sucesso', 'A senha foi resetada!\nFaca login para inserir uma nova.')
            case 2:
                MensagemAlerta('Erro', 'Usuario nao existe!')
        
    def sair(self):
        self.destroy()


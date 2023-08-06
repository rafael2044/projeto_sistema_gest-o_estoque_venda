from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkLabel, CTkFont, CTkImage
from Popup.MensagemAlerta import MensagemAlerta
from DAO.usuarioDAO import usuarioDAO
from Imagens.img import img_resetar, img_sair
from PIL import Image
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
        HEIGHT = 175
        WEIDTH = 350
        
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
        self.grid_columnconfigure(0, weight=10)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        
        self.user = CTkEntry(self, placeholder_text='Digite o Usuario...', height=40, font=font_entry, takefocus=True)
        self.bt_resetar = CTkButton(self, text='Resetar', font=font_button, command=self.resetar, height=40,
                                    image=CTkImage(Image.open(img_resetar), size=(32,32)), compound='left')
        self.bt_sair = CTkButton(self, text='Sair', font=font_button, command=self.sair,height=40,
                                 image=CTkImage(Image.open(img_sair), size=(32,32)), compound='left')
        
        CTkLabel(self, text='Usuario', font=font_label).grid(column=0, row=0, pady=5, padx=10, sticky='w')
        self.user.grid(column=0, row=1, pady=5, padx=10, sticky='we')
        self.bt_resetar.grid(column=0, row=2, pady=15, padx=10, sticky='w')
        self.bt_sair.grid(column=0, row=2, pady=15, padx=10, sticky='e')
        
    def resetar(self, event=None):
        user = self.user.get()
        match usuarioDAO().resetar_senha(user):
            case 1:
                MensagemAlerta('Sucesso', 'A senha foi resetada!\nEfetue login no sistema para inserir uma nova.')
            case 2:
                MensagemAlerta('Erro', 'Usuario não existe!')
        
    def sair(self):
        self.destroy()


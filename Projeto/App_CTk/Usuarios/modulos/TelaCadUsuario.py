from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkFont, CTkComboBox, CTkImage
from Popup.MensagemAlerta import MensagemAlerta
from Popup.DialogoSimNao import DialogoSimNao
from DAO.usuarioDAO import usuarioDAO
from DAO.tipoDAO import TipoDAO
from Imagens.img import img_cadastrar, img_sair
from PIL import Image
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
        HEIGHT = 230
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
        
        self.tipos = TipoDAO().select_all_tipo()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
       
        self.user = CTkEntry(self, placeholder_text='Digite o Usuario...', height=40, font=font_entry)
        self.cb_tipo = CTkComboBox(self, values=[x[1] for x in self.tipos], font=font_label, state='readonly', height=40)
        self.bt_cadastrar = CTkButton(self, text='Cadastrar', font=font_button, command=self.cadastrar, height=40,
                                      image=CTkImage(Image.open(img_cadastrar), size=(32,32)), compound='left')
        self.bt_sair = CTkButton(self, text='Sair', font=font_button, command=self.sair,height=40, width=80,
                                 image=CTkImage(Image.open(img_sair), size=(32,32)), compound='left')
        
        CTkLabel(self, text='Usuario', font=font_label).grid(padx=10, pady=5, sticky='w', column=0, row=0)
        self.user.grid(padx=10, sticky='we', column=0, row=1)
        CTkLabel(self, text='Tipo de Usuario', font=font_label).grid(padx=10, pady=5, sticky='w', column=0, row=2)
        self.cb_tipo.grid(padx=10, pady=(0,5), sticky='we', column=0, row=3)
        self.bt_cadastrar.grid(padx=10, pady=10, sticky='w', column=0, row=4)
        self.bt_sair.grid(padx=10, pady=10, sticky='e', column=0, row=4)
        
    def cadastrar(self, event=None):
        user = self.user.get()
        tipo = TipoDAO().select_id_tipo(self.cb_tipo.get())[0]
        
        op = DialogoSimNao('Cadastrar', 'Deseja realizar o cadastro?')
        if op.opcao:
            match usuarioDAO().insert_usuario(user, tipo):
                
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


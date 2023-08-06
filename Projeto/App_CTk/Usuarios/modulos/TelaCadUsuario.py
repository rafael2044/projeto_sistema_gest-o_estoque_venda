from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkFont, CTkComboBox, CTkImage
from Popup.MensagemAlerta import MensagemAlerta
from Popup.DialogoSimNao import DialogoSimNao
from DAO.usuarioDAO import usuarioDAO
from DAO.nivelDAO import NivelDAO
from DAO.setorDAO import SetorDAO
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
        HEIGHT = 300
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
        
        self.niveis = NivelDAO().select_all_nivel()
        self.setores = SetorDAO().select_all_setor()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
       
        self.user = CTkEntry(self, placeholder_text='Digite o Usuario...', height=40, font=font_entry)
        self.cb_nivel = CTkComboBox(self, values=[x[1] for x in self.niveis], font=font_label, state='readonly', height=40)
        self.cb_setor = CTkComboBox(self, values=[x[1] for x in self.setores], font=font_label, state='readonly', height=40)
        self.bt_cadastrar = CTkButton(self, text='Cadastrar', font=font_button, command=self.cadastrar, height=40,
                                      image=CTkImage(Image.open(img_cadastrar), size=(32,32)), compound='left')
        self.bt_sair = CTkButton(self, text='Sair', font=font_button, command=self.sair,height=40, width=80,
                                 image=CTkImage(Image.open(img_sair), size=(32,32)), compound='left')
        
        CTkLabel(self, text='Usuario', font=font_label).grid(padx=10, pady=5, sticky='w', column=0, row=0)
        self.user.grid(padx=10, sticky='we', column=0, row=1)
        CTkLabel(self, text='Nivel de Usuario', font=font_label).grid(padx=10, pady=5, sticky='w', column=0, row=2)
        self.cb_nivel.grid(padx=10, pady=(0,5), sticky='we', column=0, row=3)
        CTkLabel(self, text='Setor', font=font_label).grid(padx=10, pady=5, sticky='w', column=0, row=4)
        self.cb_setor.grid(padx=10, pady=(0,5), sticky='we', column=0, row=5)
        self.bt_cadastrar.grid(padx=10, pady=10, sticky='w', column=0, row=6)
        self.bt_sair.grid(padx=10, pady=10, sticky='e', column=0, row=6)
        
    def cadastrar(self, event=None):
        user = self.user.get()
        nivel = NivelDAO().select_id_nivel(self.cb_nivel.get())[0]
        setor = SetorDAO().select_id_setor(self.cb_setor.get())[0]
        op = DialogoSimNao('Cadastrar', 'Deseja realizar o cadastro?')
        if op.opcao:
            match usuarioDAO().insert_usuario(user, nivel, setor):
                
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


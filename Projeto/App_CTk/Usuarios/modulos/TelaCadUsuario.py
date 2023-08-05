from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTk, CTkLabel, CTkFont, CTkComboBox
from Popup.MensagemAlerta import MensagemAlerta
from Popup.DialogoSimNao import DialogoSimNao
from DAO.usuarioDAO import usuarioDAO
from DAO.tipoDAO import TipoDAO
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
        HEIGHT = 250
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
        
        f_main = CTkFrame(self)
        f_button = CTkFrame(f_main, fg_color='transparent')
        self.user = CTkEntry(f_main, placeholder_text='Digite o Usuario...', height=40, font=font_entry)
        self.cb_tipo = CTkComboBox(f_main, values=[x[1] for x in self.tipos], font=font_label, state='readonly')
        self.bt_cadastrar = CTkButton(f_button, text='Cadastrar', font=font_button, command=self.cadastrar, height=40)
        self.bt_sair = CTkButton(f_button, text='Sair', font=font_button, command=self.sair,height=40)
        
        f_main.pack(padx=10,pady=10, expand=True, fill = 'both')
        CTkLabel(f_main, text='Usuario', font=font_label).pack(padx=10, pady=5, anchor='w')
        self.user.pack(padx=10, anchor='w', fill='x')
        CTkLabel(f_main, text='Tipo de Usuario', font=font_label).pack(padx=10, pady=5, anchor='w')
        self.cb_tipo.pack(padx=10, anchor='w', fill='x')
        f_button.pack(padx=10, pady=(20,10))
        self.bt_cadastrar.pack(padx=(0,20), side='left')
        self.bt_sair.pack(padx=(20,0), side='left')
        
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


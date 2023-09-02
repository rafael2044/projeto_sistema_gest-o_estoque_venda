from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkLabel, CTkFont, CTkImage
from Popup.MensagemAlerta import MensagemAlerta
from DAO.usuarioDAO import usuarioDAO
from Imagens.img import img_logo, img_sair, img_entrar, img_salvar_senha
from PIL import Image
class Login(CTkToplevel):
    def __init__(self, master):
        CTkToplevel.__init__(self, master=master)
        self.master = master
        self.title('Entrada no Sistema')
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
        font_label = CTkFont('Segoe UI', size=14, weight='bold')
        font_entry = CTkFont('Segoe UI', size=15)
        font_button = CTkFont('Segoe UI', size=15, weight='bold')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=4)
        self.grid_rowconfigure(3, weight=4)
        
        self.user = CTkEntry(self, placeholder_text='Digite o Usuario...', height=40, font=font_entry, takefocus=True)
        self.password = CTkEntry(self, show='*', placeholder_text='Digite a Senha...', height=40, font=font_entry)
        
        self.bt_entrar = CTkButton(self, text='Confirmar', font=font_button, command=self.logar, width=100, height=40, image=CTkImage(Image.open(img_entrar), size=(32,32)),
                                   compound='left')
        self.bt_sair = CTkButton(self, text='Cancelar', font=font_button, command=self.sair,width=100, height=40, image=CTkImage(Image.open(img_sair), size=(32,32)),
                                 compound='left')
        
        CTkLabel(self, text='', image=CTkImage(Image.open(img_logo), size=(200,80))).grid(column=0, row=0, columnspan=2, sticky='nesw')
        CTkLabel(self, text='Usuario:', font=font_label).grid(column=0, row=1, padx=(2,2), sticky='e')
        self.user.grid(column=1, row=1, padx=(3,10),sticky='we')
        CTkLabel(self, text='Senha:',font=font_label).grid(column=0, row=2, sticky='e', padx=(2,2))
        self.password.grid(column=1, row=2, sticky='we', padx=(3,10))
        self.bt_entrar.grid(column=0, row=3, columnspan=2, padx=20, sticky='w')
        self.bt_sair.grid(column=0, row=3, columnspan=2, padx=20, sticky='e')
        

    def logar(self, event=None):
        user = self.user.get()
        password = self.password.get()
        
        match self.usuarioDAO.validar_usuario(user, password):
            case 1:
                self.limpar_entrys()
                self.master.dados_usuario['usuario'] = user
                self.master.dados_usuario['nivel'] = self.usuarioDAO.select_nivel_usuario(user)[0]
                self.master.dados_usuario['setor'] = self.usuarioDAO.select_setor_usuario(user)[0]
                self.master.usuario.configure(text=user)
                self.master.verificar_restricoes_usuario()
                self.grab_release()
                self.withdraw()
            case 2:
                MensagemAlerta('Login Invalido', 'Usuario e/ou Senha invalidos!')
            case 3:
                NovaSenha(user)
        
    def limpar_entrys(self):
        self.user.delete(0, 'end')
        self.password.delete(0, 'end')
        
    def sair(self):
        self.quit()
        
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
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        
        self.password = CTkEntry(self, placeholder_text='Digite a Senha...', height=40, font=font_entry, takefocus=True, show='*')
        self.password_validacao = CTkEntry(self, show='*', placeholder_text='Digite a Senha novamente...', height=40, font=font_entry)
        
        self.bt_salvar = CTkButton(self, text='Salvar', font=font_button, image=CTkImage(Image.open(img_salvar_senha), size=(32,32)),compound='left', command=self.inserir, height=40)
        self.bt_sair = CTkButton(self, text='Sair', font=font_button,image=CTkImage(Image.open(img_sair), size=(32,32)),compound='left', command=self.sair,height=40, width=80)
        
        CTkLabel(self, text='Senha', font=font_label).grid(column=0, row=0, pady=10, padx=10, sticky='w')
        self.password.grid(column=0, row=1, padx=10, sticky='we')
        CTkLabel(self, text='Validar Senha',font=font_label).grid(column=0, row=2, pady=10, padx=10, sticky='w')
        self.password_validacao.grid(column=0, row=3, padx=10, sticky='we')
        self.bt_salvar.grid(column=0, row=4, pady=10, padx=10, sticky='w')
        self.bt_sair.grid(column=0, row=4, pady=10, padx=10, sticky='e')
        
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


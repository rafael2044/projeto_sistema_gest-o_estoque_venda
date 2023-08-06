from customtkinter import CTkFrame, CTkButton, CTk, CTkLabel, CTkFont, CTkImage
from Usuarios.modulos.TelaLogin import Login
from Usuarios.modulos.TelaCadUsuario import CadUsuario
from Usuarios.modulos.TelaResetarSenha import ResetarSenha
from Usuarios.modulos.TelaEditarUsuario import EditarUsuario
from Popup.MensagemAlerta import MensagemAlerta
from Popup.DialogoSimNao import DialogoSimNao
from DAO.usuarioDAO import usuarioDAO
from Imagens.img import img_editar, img_excluir, img_add_usuario, img_resetar_senha
from tkinter.ttk import Treeview, Scrollbar, Style
from tkinter import Menu
from PIL import Image
class TelaPrincipal(CTk):
    
    def __init__(self):
        CTk.__init__(self)
        self.title('Sistema Usuario')
        self.usuarioDAO = usuarioDAO()
        self.centralizar_janela()
        self.carregar_widgets()
        self.dados_usuario = {'usuario':'', 'nivel':'', 'setor':''}
        self.login = Login(self)
        self.cad_usuario = None
        self.resetar_senha = None
        self.editar_usuario = None
        
    def centralizar_janela(self):
        HEIGHT = 650
        WEIDTH = 750
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
    
    def carregar_widgets(self):
        self.carregar_menu()
        self.style = Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview', font=('Segoe UI', 15), rowheight=30)
        self.style.configure('Treeview.Heading', font=('Segoe UI', 13, 'bold'))
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        
        
        self.grid_columnconfigure(0, weight=30)
        self.grid_columnconfigure(1, weight=30)
        self.grid_columnconfigure(2, weight=0)
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=30)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=5)
        
        f_menu = CTkFrame(self, height=40, border_width=2, border_color='white', fg_color='transparent')
        f_info = CTkFrame(self, height=30, fg_color='transparent')
        f_buttons = CTkFrame(self, height=30, fg_color='transparent')
        
        self.font_button = CTkFont('Segoe UI', size=18, slant='italic', weight='bold')
        
        self.usuario = CTkLabel(f_info, text=' '*50, font=('Segoe UI', 12, 'bold'))
        
        self.tv_tabela = Treeview(self, columns=('id', 'usuario', 'nivel', 'setor'),
                                  selectmode='browse', show='headings')
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('usuario', text='Usuario')
        self.tv_tabela.heading('nivel', text='Nivel')
        self.tv_tabela.heading('setor', text='Setor')
        
        self.tv_tabela.column('#0', width=2, minwidth=2, stretch=True)
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50, anchor='center')
        self.tv_tabela.column('usuario', width=300, stretch=True, minwidth=175)
        self.tv_tabela.column('nivel', width=200, stretch=True, minwidth=175)
        self.tv_tabela.column('setor', width=200, stretch=True, minwidth=175)
        
        self.scrollbar_vertical = Scrollbar(self, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(self, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        self.bt_cad = CTkButton(f_menu, text='Cadastrar Usuario', command=self.abrir_janela_cadastro, font=self.font_button,
                                image=CTkImage(Image.open(img_add_usuario), size=(64,64)), compound='top', fg_color='transparent')
        self.bt_reset = CTkButton(f_menu, text='Resetar Senha', font=self.font_button, command=self.abrir_janela_resetar_senha,
                                  image=CTkImage(Image.open(img_resetar_senha), size=(64,64)), compound='top', fg_color='transparent')
        self.bt_delete = CTkButton(f_buttons, command=self.deletar_usuario_selecionado, text='Deletar',
                                   compound='left', image=CTkImage(Image.open(img_excluir), size=(32,32)),height=45,width=110, fg_color='gray',
                                   font=('Segoe UI', 15, 'bold'))
        self.bt_editar = CTkButton(f_buttons, command=self.abrir_janela_editar_usuario, text='Editar', 
                                   compound='left', image=CTkImage(Image.open(img_editar), size=(32,32)), height=45, width=110, fg_color='gray',
                                   font=('Segoe UI', 15, 'bold'))
        
        f_menu.grid(column=0, row=0, columnspan=3, sticky='we', padx=5, pady=5)
        f_info.grid(column=1, row=1, columnspan=2, padx=(0,5))
        f_buttons.grid(column=1, row=4, columnspan=2, sticky='we', padx=5)
        
        self.bt_cad.pack(padx=(5,10), side='left', pady=5)
        self.bt_reset.pack(side='left')
        
        CTkLabel(self, text='Usuarios Cadastrados', font=('Segoe UI', 19, 'bold')).grid(column=0, row=1, sticky='w', padx=10)
        self.usuario.pack(side='right', padx=(5,0))
        CTkLabel(f_info, text='Usuario Logado:', font=('Segoe UI', 12, 'bold')).pack(side='right')
        
        self.tv_tabela.grid(row=2, column=0, columnspan=2, sticky='nswe', padx=(5,0))
        self.scrollbar_vertical.grid(column=2, row=2, sticky='ns', padx=(0,5))
        self.scrollbar_horizontal.grid(column=0, row=3, columnspan=3, sticky='we', padx=5)
        
        self.bt_delete.pack(side='right', padx=(10,0))
        self.bt_editar.pack(side='right')
        
        self.tv_tabela.bind('<<TreeviewSelect>>', self.usuario_selecionado)
        self.bind('<Button-1>', self.click_fora_da_tabela)
        
    def carregar_menu(self):
        font_menubar = CTkFont(family='Segoe UI', size=14)
        font_menu = CTkFont(family='Segoe UI', size=12)
        self.menubar = Menu(self, font=font_menubar)
        self.configure(menu=self.menubar)
        self.cad_menu = Menu(self.menubar, font=font_menu)
        self.cad_menu.add_command(label='Usuario', command=self.abrir_janela_cadastro)

        self.editar_menu = Menu(self.menubar, font=font_menu)
        self.editar_menu.add_command(label='Resetar Senha de Usuario', command=self.abrir_janela_resetar_senha)
        
        sair_menu = Menu(self.menubar, font=font_menu)
        sair_menu.add_command(label='Logout', command=self.sair)
        
        self.menubar.add_cascade(label='Cadastrar', menu=self.cad_menu)
        self.menubar.add_cascade(label='Editar', menu=self.editar_menu)
        self.menubar.add_cascade(label='Sair', menu=sair_menu)
   
    def carregar_usuarios(self):
        usuarios = self.usuarioDAO.select_all_usuario()
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        if usuarios:
            [self.tv_tabela.insert('', 'end', values=p) for p in usuarios]
        
    def sair(self):
        self.login.deiconify()
        self.login.user.focus_force()
        self.login.grab_set()
    
    def verificar_restricoes_usuario(self):
        if self.dados_usuario['nivel'] == 'Administrador' and self.dados_usuario['setor'] == 'ADM':
            self.habilitar_botoes_menu()
        else:
            self.desabilitar_botoes_menu()
        
    def abrir_janela_cadastro(self):
        if self.cad_usuario is None or not self.cad_usuario.winfo_exists():
            self.cad_usuario = CadUsuario(self)
        else:
            self.cad_usuario.lift()
            
    def abrir_janela_resetar_senha(self):
        if self.resetar_senha is None or not self.resetar_senha.winfo_exists():
            self.resetar_senha = ResetarSenha(self)
        else:
            self.resetar_senha.lift()
            
    def abrir_janela_editar_usuario(self):
        dados = self.tv_tabela.item(self.usuario_dados_selecionado[0], 'values')
        if self.editar_usuario is None or not self.editar_usuario.winfo_exists():
            self.editar_usuario = EditarUsuario(self, dados)
        else:
            self.editar_usuario.lift()
    
    def deletar_usuario_selecionado(self):
        op = DialogoSimNao('Alerta de Exclusao', 'Deseja excluir o usuario selecionado?')
        if op.opcao:
            self.id = self.tv_tabela.item(self.usuario_dados_selecionado[0], 'values')[0]
            if self.usuarioDAO.deletar_usuario(self.id):
                MensagemAlerta('Sucesso!', 'Usuario Excluido com sucesso!')
                self.carregar_usuarios()
            else:
                MensagemAlerta('Erro', 'Falha ao tentar excluir usuario!')
        
    def usuario_selecionado(self, event):
        self.usuario_dados_selecionado = self.tv_tabela.selection()
        if self.usuario_dados_selecionado and self.dados_usuario['nivel'] == 'Administrador' and self.dados_usuario['setor'] == 'ADM':
            self.habilitar_botoes_inferiores()
    
    def click_fora_da_tabela(self, event):
        if event.widget not in (self.tv_tabela, self.bt_delete, self.bt_editar) and self.focus_get() is self.tv_tabela and self.dados_usuario['nivel'] == 'Administrador' and self.dados_usuario['setor'] == 'ADM' :
            self.desabilitar_botoes_inferiores()
            self.tv_tabela.selection_set()
    
    def desabilitar_botoes_inferiores(self):
        self.bt_delete.configure(state='disabled')
        self.bt_delete.configure(fg_color='gray')
        self.bt_editar.configure(state='disabled')
        self.bt_editar.configure(fg_color='gray')
        
    def habilitar_botoes_inferiores(self):
        self.bt_delete.configure(state='enabled')
        self.bt_delete.configure(fg_color=("#3a7ebf", "#1f538d"))
        self.bt_editar.configure(state='enabled')
        self.bt_editar.configure(fg_color=("#3a7ebf", "#1f538d"))
        
    def habilitar_botoes_menu(self):
        self.bt_cad.configure(state='enabled')
        self.bt_cad.configure(fg_color='transparent')
        self.bt_reset.configure(state='enabled')
        self.bt_reset.configure(fg_color='transparent')
        self.cad_menu.entryconfig('Usuario', state='active')
        self.editar_menu.entryconfig('Resetar Senha de Usuario', state='active')
    
    def desabilitar_botoes_menu(self):
        self.bt_cad.configure(state='disabled')
        self.bt_cad.configure(fg_color='gray')
        self.bt_reset.configure(state='disabled')
        self.bt_reset.configure(fg_color='gray')
        self.cad_menu.entryconfig('Usuario', state='disabled')
        self.editar_menu.entryconfig('Resetar Senha de Usuario', state='disabled')
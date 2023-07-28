from customtkinter import CTkFrame, CTkButton, CTk, CTkLabel, CTkFont
from Usuarios.modulos.TelaLogin import Login
from Usuarios.modulos.TelaCadUsuario import CadUsuario
from Usuarios.modulos.TelaResetarSenha import ResetarSenha
from Usuarios.modulos.TelaEditarUsuario import EditarUsuario
from Usuarios.modulos.MensagemAlerta import MensagemAlerta
from DAO.usuarioDAO import usuarioDAO
from Imagens.img import icon_editar, icon_excluir
from tkinter.ttk import Treeview, Scrollbar, Style
from tkinter import Menu, PhotoImage
class TelaPrincipal(CTk):
    
    def __init__(self):
        CTk.__init__(self)
        self.title('Sistema')
        self.centralizar_janela()
        self.carregar_widgets()
        self.login = Login(self)
        self.nivel_usuario = None
        self.cad_usuario = None
        self.resetar_senha = None
        self.editar_usuario = None
        
    def centralizar_janela(self):
        HEIGHT = 500
        WEIDTH = 585
        
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
        
        f_button_top_menu = CTkFrame(self)
        f_info = CTkFrame(self)
        f_tabela = CTkFrame(self)
        f_scroll = CTkFrame(self, height=10)
        f_button_bottom = CTkFrame(self)
        
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')

        
        self.usuario = CTkLabel(f_info, text=' '*50, font=('Segoe UI', 12, 'bold'))
        
        self.tv_tabela = Treeview(f_tabela, columns=('id', 'usuario', 'tipo'),
                                  selectmode='browse')
        self.tv_tabela.heading('#0', text='')
        self.tv_tabela.heading('id', text='ID')
        self.tv_tabela.heading('usuario', text='Usuario')
        self.tv_tabela.heading('tipo', text='Tipo')
        
        
        self.tv_tabela.column('#0', width=2, minwidth=2, stretch=True)
        self.tv_tabela.column('id', width=50, stretch=True, minwidth=50, anchor='center')
        self.tv_tabela.column('usuario', width=300, stretch=True, minwidth=175)
        self.tv_tabela.column('tipo', width=200, stretch=True, minwidth=175)
        
        self.scrollbar_vertical = Scrollbar(f_tabela, orient='vertical', command=self.tv_tabela.yview)
        self.scrollbar_horizontal = Scrollbar(f_scroll, orient='horizontal', command=self.tv_tabela.xview)
        self.tv_tabela.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.tv_tabela.configure(yscrollcommand=self.scrollbar_vertical.set)
        
        f_button_top_menu.pack(padx=10, pady=5, anchor='w', fill='x')
        f_info.pack(padx=10, anchor='w', fill='x')
        f_tabela.pack(padx=10, pady=0, anchor='w', fill='both', expand=True)
        f_scroll.pack(padx=10, pady=0, fill='x')
        
        
        self.bt_cad = CTkButton(f_button_top_menu, text='Cadastrar Usuario', command=self.abrir_janela_cadastro, font=self.font_button, state='disabled')
        self.bt_cad.pack(side='left', padx=10)
        self.bt_reset = CTkButton(f_button_top_menu, text='Resetar Senha', font=self.font_button, state='disabled', command=self.abrir_janela_resetar_senha)
        self.bt_reset.pack(side='left', padx=10)
        
        self.bt_delete = CTkButton(f_button_bottom, state='disabled', command=self.deletar_usuario, text='', image=PhotoImage(data=icon_excluir),width=40,fg_color='gray')
        self.bt_editar = CTkButton(f_button_bottom, state='disabled', command=self.abrir_janela_editar_usuario, text='', image=PhotoImage(data=icon_editar), width=40,fg_color='gray')
        
        self.usuario.pack(side='right', padx=10)
        CTkLabel(f_info, text='Usuarios Ativoss', font=('Segoe UI', 19, 'bold')).pack(side='left', padx=10)
        CTkLabel(f_info, text='Usuario Logado:', font=('Segoe UI', 12, 'bold')).pack(side='right')
        
        self.tv_tabela.pack(side='left', fill='both')
        self.scrollbar_vertical.pack(fill='y', expand=True, anchor='w')
        f_scroll.pack(padx=10, pady=0, fill='x')
        self.scrollbar_horizontal.pack(fill='x')
        
        f_button_bottom.pack(padx=10, pady=5, anchor='w', fill='x')
        self.bt_delete.pack(side='right')
        self.bt_editar.pack(side='right', padx=10)
        self.tv_tabela.bind('<<TreeviewSelect>>', self.usuario_selecionado)
        self.bind('<Button-1>', self.desabilitar_botoes)
        
    def carregar_menu(self):
        self.menubar = Menu(self, font=('Segoe UI', 14))
        self.configure(menu=self.menubar)
        cad_menu = Menu(self.menubar, font=('Segoe UI', 10))
        cad_menu.add_command(label='Usuario')

        
        sair_menu = Menu(self.menubar, font=('Segoe UI', 14))
        sair_menu.add_command(label='Logout', command=self.sair)
        
        self.menubar.add_cascade(label='Cadastrar', menu=cad_menu)
        self.menubar.add_cascade(label='Sair', menu=sair_menu)
   
    def carregar_usuarios(self):
        usuarios = usuarioDAO.select_all_usuario()
        [self.tv_tabela.delete(x) for x in self.tv_tabela.get_children()]
        if usuarios:
            [self.tv_tabela.insert('', 'end', values=p) for p in usuarios]
        
    def sair(self):
        self.login.deiconify()
        self.login.user.focus_force()
        self.login.grab_set()
    
    def verificar_nivel(self):
        if self.nivel_usuario == 'Administrador':
            self.bt_cad.configure(state='enabled')
            self.bt_reset.configure(state='enabled')
        else:
            self.bt_cad.configure(state='disabled')
            self.bt_reset.configure(state='disabled')
        
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
        dados = self.tv_tabela.item(self.usuario_dados[0], 'values')
        if self.editar_usuario is None or not self.editar_usuario.winfo_exists():
            self.editar_usuario = EditarUsuario(self, dados)
        else:
            self.editar_usuario.lift()
    
    def deletar_usuario(self):
        self.id = self.tv_tabela.item(self.usuario_dados[0], 'values')[0]
        print(self.id)
        if usuarioDAO.deletar_usuario(self.id):
            MensagemAlerta('Sucesso!', 'Usuario Excluido com sucesso!')
            self.carregar_usuarios()
        else:
            MensagemAlerta('Erro', 'Falha ao tentar excluir usuario!')
    
    def usuario_selecionado(self, event):
        self.usuario_dados = self.tv_tabela.selection()
        if self.usuario_dados and self.nivel_usuario == 'Administrador':
            self.bt_delete.configure(state='enabled')
            self.bt_delete.configure(fg_color=("#3a7ebf", "#1f538d"))
            self.bt_editar.configure(state='enabled')
            self.bt_editar.configure(fg_color=("#3a7ebf", "#1f538d"))
    
    def desabilitar_botoes(self, event):
        if event.widget not in (self.tv_tabela, self.bt_delete, self.bt_editar) and self.focus_get() is self.tv_tabela and self.nivel_usuario == 'Administrador':
            self.bt_delete.configure(state='disabled')
            self.bt_delete.configure(fg_color='gray')
            self.bt_editar.configure(state='disabled')
            self.bt_editar.configure(fg_color='gray')
            self.tv_tabela.selection_set()
            
            
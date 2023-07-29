from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
from DAO.usuarioDAO import usuarioDAO
from DAO.tipoDAO import TipoDAO
from Popup.MensagemAlerta import MensagemAlerta

class EditarUsuario(CTkToplevel):
    def __init__(self, master, dados:list):
        CTkToplevel.__init__(self)
        self.master =master
        self.dados = list(dados)
        self.tipoDAO = TipoDAO()
        self.after(100, self.lift)
        self.title('Editar Usuario')
        self.centralizar_janela()
        self.carregar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT =350
        WEIDTH = 450
        
        X = int(self.master.winfo_x() + WEIDTH//2)
        Y = self.master.winfo_y()
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        self.tipos = self.tipoDAO.select_all_tipo()
        
        frame = CTkFrame(self)
        frame.pack(padx=10, pady=10, fill='both')
        self.usuario = CTkEntry(frame, placeholder_text='Digite o novo usuario...', font=self.font_entry, height=40)
        
        self.tipo = CTkComboBox(frame, font=self.font_entry, values=[x[1] for x in self.tipos], height=40)    
        
      
        CTkLabel(frame, text='Usuario', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.usuario.pack(padx=10, anchor='w')
        CTkLabel(frame, text='Tipo de Usuario', font=self.font_label).pack(padx=10, anchor='w', pady=10)
        self.tipo.pack(padx=10, anchor='w', fill='x')
      
        
        CTkButton(frame, text='Salvar Alteracoes', font=self.font_button, height=40, command=self.salvar_alterecoes).pack(anchor='w', padx=10, pady=20, side='left')
        CTkButton(frame, text='Cancelar', font=self.font_button, height=40, command=self.destroy).pack(anchor='w', padx=10, pady=20, side='left')

        self.carregar_dados()
        
    def carregar_dados(self):
        self.usuario.insert(0, self.dados[1])
        self.tipo.set(self.dados[2])
            
    def salvar_alterecoes(self):
        self.dados[1] = self.usuario.get()
        self.dados[2] = self.tipoDAO.select_id_tipo(self.tipo.get())[0]

        print(self.dados)
        match usuarioDAO().atualizar_usuario(*self.dados):
            case 1:
                MensagemAlerta('Sucesso!', 'Alteracoes realizadas com sucesso!')
                self.master.carregar_usuarios()
                self.destroy()
            case 2:
                MensagemAlerta('Erro!', 'O usuario ja existe!')

        
    
            
        
        
        
        
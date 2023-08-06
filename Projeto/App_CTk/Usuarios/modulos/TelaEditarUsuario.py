from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkFont, CTkImage
from DAO.usuarioDAO import usuarioDAO
from DAO.nivelDAO import NivelDAO
from DAO.setorDAO import SetorDAO
from Popup.MensagemAlerta import MensagemAlerta
from Imagens.img import img_salvar, img_sair
from PIL import Image


class EditarUsuario(CTkToplevel):
    def __init__(self, master, dados:list):
        CTkToplevel.__init__(self)
        self.master =master
        self.dados = list(dados)
        self.nivelDAO = NivelDAO()
        self.setorDAO = SetorDAO()
        self.after(100, self.lift)
        self.title('Editar Usuario')
        self.centralizar_janela()
        self.carregar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def centralizar_janela(self):
        HEIGHT =425
        WEIDTH = 450
        
        X = int(self.master.winfo_x() + WEIDTH//2)
        Y = self.master.winfo_y()
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, weight='bold')
        
        self.grid_columnconfigure(0, weight=30)
        
        self.niveis = self.nivelDAO.select_all_nivel()
        self.setores = self.setorDAO.select_all_setor()
        
        self.id = CTkEntry(self, font=self.font_entry, height=40, width=40)
        
        self.usuario = CTkEntry(self, placeholder_text='Digite o novo nome de usuario...', font=self.font_entry, height=40)
        
        self.nivel = CTkComboBox(self, font=self.font_entry, values=[x[1] for x in self.niveis], height=40, state='readonly')    
        self.setor = CTkComboBox(self, font=self.font_entry, values=[x[1] for x in self.setores], height=40, state='readonly')  
        
        CTkLabel(self, text='ID', font=self.font_label).grid(padx=10, pady=10, column=0, row=0, sticky='w')
        self.id.grid(padx=10, sticky='w', column=0, row=1)
        CTkLabel(self, text='Usuario', font=self.font_label).grid(padx=10, pady=10, column=0, row=2, sticky='w')
        self.usuario.grid(padx=10, sticky='we', column=0, row=3)
        CTkLabel(self, text='Nivel de Usuario', font=self.font_label).grid(padx=10, sticky='w', pady=10, column=0, row=4)
        self.nivel.grid(padx=10, sticky='we', column=0, row=5)
        CTkLabel(self, text='Setor', font=self.font_label).grid(padx=10, sticky='w', pady=10, column=0, row=6)
        self.setor.grid(padx=10, sticky='we', column=0, row=7)
      
        
        CTkButton(self, text='Salvar Alterações', font=self.font_button, height=40, command=self.salvar_alterecoes,
                  image=CTkImage(Image.open(img_salvar), size=(32,32)), compound='left').grid(sticky='w', padx=10, pady=20, column=0, row=8)
        CTkButton(self, text='Cancelar', font=self.font_button, height=40, command=self.destroy, 
                  image=CTkImage(Image.open(img_sair), size=(32,32)), compound='left').grid(sticky='e', padx=10, pady=20, column=0, row=8)

        self.carregar_dados()
        
    def carregar_dados(self):
        self.id.insert(0, self.dados[0])
        self.usuario.insert(0, self.dados[1])
        self.nivel.set(self.dados[2])
        self.setor.set(self.dados[3])
        self.id.configure(state='disabled')
            
    def salvar_alterecoes(self):
        self.dados[1] = self.usuario.get()
        self.dados[2] = self.nivelDAO.select_id_nivel(self.nivel.get())[0]
        self.dados[3] = self.setorDAO.select_id_setor(self.setor.get())[0]
        
        match usuarioDAO().atualizar_usuario(*self.dados):
            case 1:
                MensagemAlerta('Sucesso!', 'Alterações realizadas com sucesso!')
                self.master.carregar_usuarios()
                self.destroy()
            case 2:
                MensagemAlerta('Erro!', 'O usuario já existe!')

        
    
            
        
        
        
        
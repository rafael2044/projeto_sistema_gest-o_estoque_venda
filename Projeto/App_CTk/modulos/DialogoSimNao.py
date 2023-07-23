from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkFont

class DialogoSimNao(CTkToplevel):
    def __init__(self, titulo, mensagem):
        CTkToplevel.__init__(self)
        self.title(titulo)
        self.center_window()
        self.resizable(False,False)
        self.mensagem = mensagem
        self.opcao = 0
        
        self.carregar_widgets()
        self.wait_visibility()
        self.grab_set()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        self.wait_window()
        
    def center_window(self):
        HEIGHT = 100
        WEIDTH = 300
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+') 
        
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=15, weight='bold')
        CTkLabel(self, text=self.mensagem, font=self.font_label).pack(padx=10, pady=5, anchor='center')
        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=0, pady=10)
        CTkButton(frame, text='Sim', command=self.opcao_sim, width=100, font=self.font_label).pack(padx=10, anchor='center', side='left')
        CTkButton(frame, text='Não', command=self.opcao_nao, width=100, font=self.font_label).pack(padx=10, anchor='center')
        
    def opcao_sim(self):
        self.opcao = 1
        self.close()
    def opcao_nao(self):
        self.opcao = 0
        self.close()

    def close(self, event=None):
        self.destroy()

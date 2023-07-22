from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTk

class PopUp_Yes_No(CTkToplevel):
    def __init__(self, title, message):
        CTkToplevel.__init__(self)
        self.title(title)
        self.center_window()
        self.resizable(False,False)
        self.opcao = None
        CTkLabel(self, text=message).pack(padx=10, pady=5, anchor='center')
        CTkButton(self, text='Sim', command=self.opcao_sim, width=100).pack(padx=10, anchor='center')
        CTkButton(self, text='Não', command=self.opcao_nao, width=100).pack(padx=10, anchor='center')
        self.focus_force()
        self.grab_set()
        self.bind('<Return>', self.close)
        
    def center_window(self):
        HEIGHT = 75
        WEIDTH = 300
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+') 
    
    
    def opcao_sim(self):
        self.opcao = 1
        self.destroy()
    def opcao_nao(self):
        self.opcao = 0
        self.destroy()
    def close(self, event):
        self.destroy()


if __name__ == '__main__':
    root = CTk()
    resp = PopUp_Yes_No('Alerta', 'Deseja Deletar o fornecedor?')
    if resp.opcao:
        print('Sim')
    root.mainloop()
    
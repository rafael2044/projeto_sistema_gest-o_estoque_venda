from customtkinter import CTkToplevel, CTkLabel, CTkButton

class AlertMessage(CTkToplevel):
    def __init__(self, title, message):
        CTkToplevel.__init__(self)
        self.title(title)
        self.center_window()
        self.resizable(False,False)
        CTkLabel(self, text=message).pack(padx=10, pady=5, anchor='center')
        CTkButton(self, text='OK', command=self.destroy, width=100).pack(padx=10, anchor='center')
        self.focus_force()
        self.grab_set()
        self.bind('<Return>', self.close)
        
    def center_window(self):
        HEIGHT = 75
        WEIDTH = 200
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = (W_WEIDTH - WEIDTH)//2
        Y = (W_HEIGHT - HEIGHT)//2
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+') 
        
    def close(self, event):
        self.destroy()

    
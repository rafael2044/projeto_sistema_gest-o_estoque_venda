from customtkinter import CTkToplevel, CTkFont, CTkFrame, CTkButton, CTkEntry, CTk, CTkOptionMenu, CTkImage, CTkLabel
from tkinter.ttk import Treeview
from PIL import Image

class TelaVenda(CTkToplevel):
    def __init__(self, master=None):
        CTkToplevel.__init__(self, master=master)
        self.master=master
        self.after(100, self.lift)
        self.title('Venda de Produtos')
        self.vendaDAO = None
        self.carrinho = [['Teclado', 10, '43,50'], ['Mouse', 5, '25,00'], ['Monitor', 2, '540,00']]
        self.centralizar_janela()
        self.carregar_widgets()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
        
    def centralizar_janela(self):
        HEIGHT = 540
        WEIDTH = 600
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int((W_HEIGHT - HEIGHT)//4.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
        
    def carregar_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=18, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=16)
        self.font_button = CTkFont('Segoe UI', size=18, slant='italic', weight='bold')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        
        f_info_carrinho = CTkFrame(self)
        f_info_carrinho.grid_columnconfigure(0, weight=1)
        f_info_carrinho.grid_columnconfigure(1, weight=1)
        f_info_carrinho.grid_rowconfigure(0, weight=0)
        f_info_carrinho.grid_rowconfigure(1, weight=0)
        
        self.bt_abrir = CTkButton(f_info_carrinho, text='↓', width=10, height=10, font=self.font_button, command=self.abrir_carrinho)

        self.f_carrinho = CTkFrame(self)
        self.f_itens_carrinho = CTkFrame(self.f_carrinho)
        
        self.bt_fechar = CTkButton(self.f_carrinho, text='^', font=self.font_button, command=self.fechar_carrinho)
    
        self.filtro = CTkOptionMenu(self, values=['Todos os Produtos'])
        self.entry_pesquisa = CTkEntry(self, placeholder_text='Pesquisar produto', width=150, height=40, font=self.font_entry)
        self.bt_pesquisar = CTkButton(self, text='Pesquisar')
            
        f_info_carrinho.grid(row=0, column=0, columnspan=3, sticky='we')
        
        self.bt_abrir.grid(row=1, column=0, columnspan=3, sticky='n')
        self.filtro.grid(row=1, column=0, columnspan=3, padx=10, sticky='w')
        self.entry_pesquisa.grid(row=2, column=0, columnspan=2, padx=10, sticky='we')
        self.bt_pesquisar.grid(row=2, column=2, padx=10,sticky='w')
    
        
    def abrir_carrinho(self):
        self.f_carrinho.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='wesn')
        self.f_itens_carrinho.pack(expand=True, fill='both')
        self.carregar_itens_carrinho()
        self.bt_fechar.pack()
        self.bt_abrir.grid_forget()
        self.filtro.grid_forget()
        self.entry_pesquisa.grid_forget()
        self.bt_pesquisar.grid_forget()
    
    def carregar_itens_carrinho(self):
        for row in range(len(self.carrinho)):
            for nome, quantidade, valor in self.carrinho:
                CTkLabel(self.f_itens_carrinho, text=f'{nome}\t{quantidade}\t{valor}').grid(column=0, row=row)
                CTkButton(self.f_itens_carrinho, text='X', command=lambda:self.remover_item(nome), width=10, height=10).grid(column=1, row=row)
            
    def remover_item(self, nome):
        for item in self.carrinho:
            if nome in item:
                self.carrinho.remove(item)
        [widget.destroy() for widget in self.f_itens_carrinho.winfo_children()]
        self.carregar_itens_carrinho()
        
    def fechar_carrinho(self):
        self.f_carrinho.grid_forget()
        self.bt_abrir.grid(row=1, column=0, columnspan=2, sticky='n')
        self.filtro.grid(row=1, column=0, columnspan=2, padx=10, sticky='w')
        self.entry_pesquisa.grid(row=2, column=0, columnspan=2, padx=10, sticky='we')
        self.bt_pesquisar.grid(row=2, column=2, padx=10,sticky='w')
        

root = CTk()
TelaVenda(root)
root.mainloop()
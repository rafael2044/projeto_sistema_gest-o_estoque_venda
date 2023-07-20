from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkComboBox, CTkTabview, CTkFont
import modulos.cursors as cursor
from tkinter.ttk import Treeview

class CadCategoria(CTkToplevel):
    def __init__(self):
        CTkToplevel.__init__(self)
        self.lift()
        self.title('Cadastrar Categoria')
        self.center_window()
        self.loader_widgets()
        self.after(100, self.lift)
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        
    def center_window(self):
        HEIGHT = 650
        WEIDTH = 700
        
        W_HEIGHT = self.winfo_screenheight()
        W_WEIDTH = self.winfo_screenwidth()
        
        X = int((W_WEIDTH - WEIDTH)//2)
        Y = int(W_HEIGHT - HEIGHT*1.5)
        
        self.geometry(f'{WEIDTH}x{HEIGHT}+{X}+{Y}+')
    def loader_widgets(self):
        self.font_label = CTkFont('Segoe UI', size=15, weight='bold')
        self.font_entry = CTkFont('Segoe UI', size=15)
        self.font_button = CTkFont('Segoe UI', size=15, weight='bold')
        
        
        tabv_main = CTkTabview(self, corner_radius=20)
        tabv_main._segmented_button.configure(font=self.font_label)
        self.tab_cad = tabv_main.add('Cadastrar')
        self.tab_pesq = tabv_main.add('Pesquisar') 
        tabv_main.pack(expand=True, fill='both', padx=10, pady=10)
        self.loader_w_tab_cad()
        self.loader_w_tab_pesq()
        self.get_categorias()
    def loader_w_tab_cad(self):
        self.nome = CTkEntry(self.tab_cad, placeholder_text='Digite o nome da Categoria...', font=self.font_entry, width=500)
        self.nome.pack(side='left', padx=10, pady=10, anchor='n')
        CTkButton(self.tab_cad, text='Cadastrar', font=self.font_button, width=100).pack(side='left', anchor='ne', pady=10)
        
    def loader_w_tab_pesq(self):
        f_pesquisa = CTkFrame(self.tab_pesq, fg_color='transparent')
        self.nome = CTkEntry(f_pesquisa, placeholder_text='Digite o nome da Categoria...', font=self.font_entry, width=500)
        self.tb_categoria = Treeview(self.tab_pesq, columns=('id', 'categoria'))
        self.tb_categoria.column('id', width=100, stretch=False, anchor='center')
        self.tb_categoria.column('#0', width=2, stretch=False)
        self.tb_categoria.heading('id', text='ID')
        self.tb_categoria.heading('categoria', text='Categoria')
        
        
        f_pesquisa.pack(fill='x', padx=10, pady=10)
        self.nome.pack(side='left', anchor='n')
        CTkButton(f_pesquisa, text='Pesquisar', font=self.font_button, width=100).pack(anchor='e')
        self.tb_categoria.pack(padx=10, pady=10, expand=True, fill='both')
        
        
    def get_categorias(self):
        categorias = cursor.select_all_categoria()
        [self.tb_categoria.delete(n) for n in self.tb_categoria.get_children()]

        
        for categoria in categorias:
            self.tb_categoria.insert('', 'end', values=(categoria['id'], categoria['nome']))
        
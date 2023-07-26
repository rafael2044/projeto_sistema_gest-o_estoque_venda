import tkinter as tk


class Application:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()    
        self.okButton = tk.Button(self.frame, text="OK",
                                  command=self.window_maker).pack()
        self.quitButton = tk.Button(self.frame, text="Close",
                                    command=self.frame.quit).pack()
        self.window_maker()
    def window_maker(self):
        MakeWindow("A message to Toplevel")


class MakeWindow(tk.Toplevel):
    def __init__(self, message):
        tk.Toplevel.__init__(self) #instead of super
        self.message = message
        self.display = tk.Label(self, text=message)
        self.display.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
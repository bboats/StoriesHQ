import tkinter as tk


class InterfaceStoriesHQ():
    def __init__(self):
        self.janela_principal = tk.Tk()
        self.janela_principal.title("StoriesHQ")
        self.janela_principal.resizable(height = 0, width = 0)
        self.janela_principal.geometry('1000x600')
        
        #inicializacao das frames no grid principal
        self.frame_esquerda = tk.Frame(self.janela_principal,height = 600, width = 650, bg="blue")
        self.frame_esquerda.grid(column=0, row=0)
        self.frame_direita = tk.Frame(self.janela_principal,height = 600, width = 350, bg="green")
        self.frame_direita.grid(column=1, row=0)
        
        #inicializacao das frames incluidas em frame_esquerda
        self.frame_esquerda_superior = tk.Frame(self.frame_esquerda,height = 300, width = 650, bg="gray")
        self.frame_esquerda_superior.grid(column=0, row=0)
        
        self.frame_esquerda_inferior = tk.Frame(self.frame_esquerda,height = 300, width = 650, bg="red")
        self.frame_esquerda_inferior.grid(column=0, row=1)
        
        
        ###


    def iniciar(self):
        self.janela_principal.mainloop()

    @staticmethod
    def abrir_interface_storieshq():
        interface = InterfaceStoriesHQ()
        interface.iniciar()




if __name__ == "__main__":
    InterfaceStoriesHQ.abrir_interface_storieshq()
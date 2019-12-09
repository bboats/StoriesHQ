import tkinter as tk
from PIL import Image, ImageTk
import os

FONTE_BOTOES = "Helvetica"
TAMANHO_FONTE_BOTOES = 25
PADDING_EXTERNO_BOTOES = (30,0) #(esquerda,direita)
CLASSES_DROPDOWN = [
    'Classe1',
    'Classe2',
    'Classe3'
]
CAMINHO_DO_EXECUTAVEL = os.getcwd()
janela_principal = tk.Tk()
janela_principal.title("StoriesHQ")
janela_principal.resizable(height = 0, width = 0)
janela_principal.geometry('1000x600')

#define a imagem de fundo da janela
background_quadrinhos = tk.PhotoImage(file= CAMINHO_DO_EXECUTAVEL + r"\src\img\quadrinhos.png")
background_label = tk.Label(janela_principal, image=background_quadrinhos)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#inicializa os tamanhos das linhas e colunas do grid principal 2x2
janela_principal.grid_columnconfigure(0, minsize=200)
janela_principal.grid_columnconfigure(1, minsize=450)
janela_principal.grid_columnconfigure(2, minsize=350)
janela_principal.grid_rowconfigure(0, minsize=90)
janela_principal.grid_rowconfigure(1, minsize=90)
janela_principal.grid_rowconfigure(2, minsize=90)
janela_principal.grid_rowconfigure(3, minsize=330)

# #inicializacao dos botoes na frame_esquerda_superior
botao_opcao_1 = tk.Button(janela_principal,borderwidth=5,command='#')
botao_opcao_1.grid(column=0, row=0, padx=PADDING_EXTERNO_BOTOES, ipadx=70, pady=(10,0))
descricao_botao_1 = tk.Label(
    janela_principal, 
    text='Descricao da opcao 1', 
    font=(FONTE_BOTOES,TAMANHO_FONTE_BOTOES),
    bg='white')
descricao_botao_1.grid(column=1, row=0, pady=(10,0))

botao_opcao_2 = tk.Button(janela_principal,borderwidth=5,command='#')
botao_opcao_2.grid(column=0, row=1, padx=PADDING_EXTERNO_BOTOES, ipadx=70)
descricao_botao_2 = tk.Label(
    janela_principal, 
    text='Descricao da opcao 2', 
    font=(FONTE_BOTOES,TAMANHO_FONTE_BOTOES),
    bg='white')
descricao_botao_2.grid(column=1, row=1)

botao_opcao_3 = tk.Button(janela_principal,borderwidth=5,command='#')
botao_opcao_3.grid(column=0, row=2, padx=PADDING_EXTERNO_BOTOES, ipadx=70)
descricao_botao_3 = tk.Label(
    janela_principal, 
    text='Descricao da opcao 3', 
    font=(FONTE_BOTOES,TAMANHO_FONTE_BOTOES),
    bg='white')
descricao_botao_3.grid(column=1, row=2)



#drop down menu direita
var_dropdown = tk.StringVar(janela_principal)
var_dropdown.set(CLASSES_DROPDOWN[0])
menu_dropdown = tk.OptionMenu(janela_principal, var_dropdown, *CLASSES_DROPDOWN)
menu_dropdown.config(width = 30)
menu_dropdown.grid(row=0, column=2, pady=(0,0))
explicacao_classe = tk.Text(janela_principal, height=24, width=25)
explicacao_classe.grid(row=1, column=2, rowspan=3, padx=(10,0))
explicacao_classe.configure(bd=0)
explicacao_classe.insert(tk.END, " ~~Descricao da classe~~")
explicacao_classe.config(state=tk.DISABLED)


#menu que muda com a opcao escolhida




if __name__ == "__main__":
    janela_principal.mainloop()
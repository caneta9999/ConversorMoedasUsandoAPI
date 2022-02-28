#Variáveis necessárias
corFundo = 'lightblue'
fonteLabelTitulo = ("Arial",20)
fonteLabelsSuporte = ("Arial", 15)
#Imports necessários
from random import randrange
from tkinter import *

#Funções necessárias
def Sortear(limiteInferior,limiteSuperior):
    numeroSorteado = randrange(limiteInferior, limiteSuperior+1)
    return numeroSorteado
def MudarTextoSorteioRealizado(texto):
    labelSorteio['text'] = texto
def ClicarParaSortear():
    limiteInferior = 1
    limiteSuperior = 10
    try:
        limiteInferior = int(limiteInferiorEntry.get())
        limiteSuperior = int(limiteSuperiorEntry.get())
    except:
        limiteInferior = 1
        limiteSuperior = 10
    if limiteInferior >= limiteSuperior or limiteInferior < 0 or limiteSuperior < 1:
        limiteInferior = 1
        limiteSuperior = 10
    labelSorteio['text'] = 'Sorteando...'
    textoSorteio = f'Limites:{limiteInferior} e {limiteSuperior}\nResultado:{Sortear(limiteInferior,limiteSuperior)}'
    labelSorteio.after(1500,MudarTextoSorteioRealizado,textoSorteio)

#Interface gráfica
#Criando componentes e ajustes iniciais
window = Tk()
window.title("Sorteador")
window.geometry('500x500')

labelTitulo = Label(window, text="Sorteador de números", font=fonteLabelTitulo, bg = corFundo)
labelTitulo.grid(column=0, row=0)

labelLimiteInferior = Label(window, text="Limite inferior: ", font=fonteLabelsSuporte, bg = corFundo)
labelLimiteInferior.grid(column=0, row=1)
limiteInferiorEntry = Entry(window)
limiteInferiorEntry.grid(column=1,row=1)

labelLimiteSuperior = Label(window, text="Limite superior: ", font=fonteLabelsSuporte, bg = corFundo)
labelLimiteSuperior.grid(column=0, row=2)
limiteSuperiorEntry = Entry(window)
limiteSuperiorEntry.grid(column=1,row=2)

buttonSortear = Button(window, text="Realizar o sorteio",command=ClicarParaSortear, bg = corFundo)
buttonSortear.grid(column=0, row=3)

labelSorteio = Label(window, text="", font=fonteLabelsSuporte, bg = corFundo)
labelSorteio.grid(column=0, row=4)
#Configurando a cor do fundo da window
window['bg'] = corFundo
#Realizando o sorteio
window.mainloop()

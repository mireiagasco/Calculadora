from tkinter import *

#creem la finestra
finestra = Tk()
finestra.title("Calculadora")

#creem un índex per poder introduir els valors a la caixa de text en l'ordre correcte
i = 0

#creem l'entrada de text
text = Entry(finestra, font = "Calibri 20")
text.grid(row = 0, column = 0, columnspan = 4, pady = 5, padx = 5)

#funcions
def boto_seleccionat(valor):
    global i #accedim a l'índex
    if i == 0:
        esborrar_text()
    text.insert(i, valor)
    i +=1 #augmentem l'índex

def esborrar_text():
    text.delete(0, END)

def calcular():
    global i
    operacio = text.get()
    esborrar_text()
    try:
        resultat = eval(operacio)
    except Exception:
        resultat = "Error"
    text.insert(0, resultat)
    i = 0


#creem els botons
boto1 = Button(finestra, text = "1", width = 5, height = 2, command = lambda: boto_seleccionat(1))
boto2 = Button(finestra, text = "2", width = 5, height = 2, command = lambda: boto_seleccionat(2))
boto3 = Button(finestra, text = "3", width = 5, height = 2, command = lambda: boto_seleccionat(3))
boto4 = Button(finestra, text = "4", width = 5, height = 2, command = lambda: boto_seleccionat(4))
boto5 = Button(finestra, text = "5", width = 5, height = 2, command = lambda: boto_seleccionat(5))
boto6 = Button(finestra, text = "6", width = 5, height = 2, command = lambda: boto_seleccionat(6))
boto7 = Button(finestra, text = "7", width = 5, height = 2, command = lambda: boto_seleccionat(7))
boto8 = Button(finestra, text = "8", width = 5, height = 2, command = lambda: boto_seleccionat(8))
boto9 = Button(finestra, text = "9", width = 5, height = 2, command = lambda: boto_seleccionat(9))
boto0 = Button(finestra, text = "0", width = 16, height = 2, command = lambda: boto_seleccionat(0))

boto_suma = Button(finestra, text = "+", width = 5, height = 2, command = lambda: boto_seleccionat("+"))
boto_resta = Button(finestra, text = "-", width = 5, height = 2, command = lambda: boto_seleccionat("-"))
boto_multi = Button(finestra, text = "*", width = 5, height = 2, command = lambda: boto_seleccionat("*"))
boto_div = Button(finestra, text = "/", width = 5, height = 2, command = lambda: boto_seleccionat("/"))

boto_igual = Button(finestra, text = "=", width = 5, height = 2, command = calcular)
boto_esborrar = Button(finestra, text = "AC", width = 5, height = 2, command = esborrar_text)
boto_obrir_parentesi = Button(finestra, text = "(", width = 5, height = 2, command = lambda: boto_seleccionat("("))
boto_tancar_parentesi = Button(finestra, text = ")", width = 5, height = 2, command = lambda: boto_seleccionat(")"))
boto_punt = Button(finestra, text = ".", width = 5, height = 2, command = lambda: boto_seleccionat("."))

#posicionem els botons a la finestra
boto_esborrar.grid(row = 1, column = 0)
boto_obrir_parentesi.grid(row = 1, column = 1)
boto_tancar_parentesi.grid(row = 1, column = 2)
boto_div.grid(row = 1, column = 3)

boto7.grid(row = 2, column = 0)
boto8.grid(row = 2, column = 1)
boto9.grid(row = 2, column = 2)
boto_multi.grid(row = 2, column = 3)

boto4.grid(row = 3, column = 0)
boto5.grid(row = 3, column = 1)
boto6.grid(row = 3, column = 2)
boto_suma.grid(row = 3, column = 3)

boto1.grid(row = 4, column = 0)
boto2.grid(row = 4, column = 1)
boto3.grid(row = 4, column = 2)
boto_resta.grid(row = 4, column = 3)

boto0.grid(row = 5, column = 0, columnspan = 2)
boto_punt.grid(row = 5, column = 2)
boto_igual.grid(row = 5, column = 3)



finestra.mainloop()
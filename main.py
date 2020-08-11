from tkinter import *

#creem la finestra
finestra = Tk()
finestra.title("Calculadora")

#creem un índex per poder introduir els valors a la caixa de text en l'ordre correcte
i = 0

#creem l'entrada de text
text = Entry(finestra, font = "Arial 20")
text.grid(row = 0, column = 0, columnspan = 5, pady = 5, padx = 5)

#creem la finestreta on es mostrarà el resultat
finestra_resultat = Entry(finestra, font = "Arial 20", width = 7)
finestra_resultat.grid(row = 1, column = 3, columnspan = 2)

#---------funcions
#funció que escriu a la caixa de text el valor equivalent a la tecla pitjada
def boto_seleccionat(valor):
    global i #accedim a l'índex
    if i == 0:
        esborrar_text(text)
        esborrar_text(finestra_resultat)
    text.insert(i, valor)
    res_parcial()
    i +=1 #augmentem l'índex

#lambda que esborra tot el text de la caixa de text indicada
esborrar_text = lambda lloc: lloc.delete(0, END)

#lambda que mostra el resultat en una caixa de text indicada en els arguments
mostrar_text = lambda lloc, valor: lloc.insert(0, valor)

#funció que calcula el resultat de l'operació escrita en la caixa de text i, si no es pot,
#dona un missatge d'error
def calcular():
    global i
    operacio = text.get() #obtenim el string amb l'operació
    try:
        resultat = eval(operacio)
    except Exception:
        if operacio[-1] == "=":
            resultat = "Error"
        else:
            resultat = " "
    return resultat
    

#funció que va mostrant el resultat parcial a la finestreta petita
def res_parcial():
    global i
    if i != 0:
        resultat = calcular()
        mostrar_text(finestra_resultat, resultat)

#funció que mostra el resultat final d'una operació
def res_final(nom_finestra):
    global i
    i = 0
    resultat = calcular() #calculem el resultat
    esborrar_text(text) #netegem la caixa de text
    mostrar_text(text, resultat) #mostrem el resultat


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
boto0 = Button(finestra, text = "0", width = 14, height = 2, command = lambda: boto_seleccionat(0))

boto_suma = Button(finestra, text = "+", width = 5, height = 2, command = lambda: boto_seleccionat("+"))
boto_resta = Button(finestra, text = "-", width = 5, height = 2, command = lambda: boto_seleccionat("-"))
boto_multi = Button(finestra, text = "*", width = 5, height = 2, command = lambda: boto_seleccionat("*"))
boto_div = Button(finestra, text = "/", width = 5, height = 2, command = lambda: boto_seleccionat("/"))

boto_igual = Button(finestra, text = "=", width = 7, height = 10, command = lambda: res_final(text))
boto_esborrar = Button(finestra, text = "AC", width = 5, height = 2, command = esborrar_text)
boto_obrir_parentesi = Button(finestra, text = "(", width = 5, height = 2, command = lambda: boto_seleccionat("("))
boto_tancar_parentesi = Button(finestra, text = ")", width = 5, height = 2, command = lambda: boto_seleccionat(")"))
boto_punt = Button(finestra, text = ".", width = 5, height = 2, command = lambda: boto_seleccionat("."))

#posicionem els botons a la finestra
boto_esborrar.grid(row = 1, column = 0)
boto_obrir_parentesi.grid(row = 1, column = 1)
boto_tancar_parentesi.grid(row = 1, column = 2)
boto_div.grid(row = 5, column = 3)

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
boto_igual.grid(row = 2, column = 4, rowspan = 4)

#generem el loop de la finestra
finestra.mainloop()

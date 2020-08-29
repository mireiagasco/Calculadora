from tkinter import *
import tkinter.messagebox

#classe que genera una finestra tkinter amb aparença de calculadora
class Calculadora:
      
    def  __init__(self):        

        self.reiniciar = False

        #creem la finestra
        self.finestra = Tk()
        self.finestra.title("Calculadora")
        self.finestra.iconbitmap(r"icona_calculadora.ico")

        #creem l'entrada de text
        self.entr_op = Entry(self.finestra, font = "Arial 20")
        self.entr_op.grid(row = 0, column = 0, columnspan = 5, pady = 5, padx = 5)

        #creem la finestreta on es mostrarà el resultat
        self.f_res_par = Entry(self.finestra, font = "Arial 20", width = 7)
        self.f_res_par.grid(row = 1, column = 3, columnspan = 2)
             
        #creem els botons
        Button(self.finestra, text = "1", width = 5, height = 2, command = lambda: self.boto_seleccionat('1')).grid(row = 4, column = 0)
        Button(self.finestra, text = "2", width = 5, height = 2, command = lambda: self.boto_seleccionat('2')).grid(row = 4, column = 1)
        Button(self.finestra, text = "3", width = 5, height = 2, command = lambda: self.boto_seleccionat('3')).grid(row = 4, column = 2)
        Button(self.finestra, text = "4", width = 5, height = 2, command = lambda: self.boto_seleccionat('4')).grid(row = 3, column = 0)
        Button(self.finestra, text = "5", width = 5, height = 2, command = lambda: self.boto_seleccionat('5')).grid(row = 3, column = 1)
        Button(self.finestra, text = "6", width = 5, height = 2, command = lambda: self.boto_seleccionat('6')).grid(row = 3, column = 2)
        Button(self.finestra, text = "7", width = 5, height = 2, command = lambda: self.boto_seleccionat('7')).grid(row = 2, column = 0)
        Button(self.finestra, text = "8", width = 5, height = 2, command = lambda: self.boto_seleccionat('8')).grid(row = 2, column = 1)
        Button(self.finestra, text = "9", width = 5, height = 2, command = lambda: self.boto_seleccionat('9')).grid(row = 2, column = 2)
        Button(self.finestra, text = "0", width = 14, height = 2, command = lambda: self.boto_seleccionat('0')).grid(row = 5, column = 0, columnspan = 2)

        Button(self.finestra, text = "+", width = 5, height = 2, command = lambda: self.boto_seleccionat("+")).grid(row = 3, column = 3)
        Button(self.finestra, text = "-", width = 5, height = 2, command = lambda: self.boto_seleccionat("-")).grid(row = 4, column = 3)
        Button(self.finestra, text = "*", width = 5, height = 2, command = lambda: self.boto_seleccionat("*")).grid(row = 2, column = 3)
        Button(self.finestra, text = "/", width = 5, height = 2, command = lambda: self.boto_seleccionat("/")).grid(row = 5, column = 3)

        Button(self.finestra, text = "=", width = 7, height = 10, command = lambda: self.res_final()).grid(row = 2, column = 4, rowspan = 4)
        Button(self.finestra, text = "AC", width = 5, height = 2, command = lambda: self.esborrar_tot()).grid(row = 1, column = 0)
        Button(self.finestra, text = "(", width = 5, height = 2, command = lambda: self.boto_seleccionat("(")).grid(row = 1, column = 1)
        Button(self.finestra, text = ")", width = 5, height = 2, command = lambda: self.boto_seleccionat(")")).grid(row = 1, column = 2)
        Button(self.finestra, text = ".", width = 5, height = 2, command = lambda: self.boto_seleccionat(".")).grid(row = 5, column = 2)

    #generem el main loop de la finestra
    def iniciar(self):
        self.finestra.mainloop()

    #lambda que esborra tot el text de la caixa de text indicada
    esborrar_text = lambda self, lloc: lloc.delete(0, END)

    #lambda que mostra el resultat en una caixa de text indicada en els arguments
    mostrar_text = lambda self, valor, lloc: lloc.insert(0, valor)

    #funció que escriu a la caixa de text els valors que es van pitjant
    def boto_seleccionat(self, valor):        

        if self.reiniciar:
            self.esborrar_text(self.f_res_par)
            self.esborrar_text(self.entr_op)
            self.reiniciar = False

        #mostrem el nou valor
        actual = self.entr_op.get()
        self.esborrar_text(self.entr_op)
        self.entr_op.insert(0, actual + valor)       
        resultat = self.calcular(actual + valor)
        
        #esborrem el text de la finestra del resultat parcial i mostrem el nou
        self.esborrar_text(self.f_res_par)
        if resultat != "Error":            
            self.mostrar_text(resultat, self.f_res_par)            

    #funció que calcula el resultat de l'operació escrita en la caixa de text i, si no es pot, dona un missatge d'error
    def calcular(self, operacio):
        try:
            resultat = eval(operacio)
        except SyntaxError:
            resultat = "Error"
        except ZeroDivisionError:
            resultat = "Error"
            tkinter.messagebox.showerror("Error", "No es pot dividir entre zero")
        return resultat
    
    #funció que mostra el resultat final d'una operació
    def res_final(self):
        self.reiniciar = True
        resultat = self.f_res_par.get()
        self.esborrar_text(self.entr_op)
        if resultat:    #si el resultat parcial és vàlid
            self.mostrar_text(resultat, self.entr_op) #mostrem el resultat
        else:
            self.mostrar_text("Error", self.entr_op) #mostrem un error

    #funció que esborra el text de les dues caixes
    def esborrar_tot(self):
        self.esborrar_text(self.entr_op)
        self.esborrar_text(self.f_res_par)

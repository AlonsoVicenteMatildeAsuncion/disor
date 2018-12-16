from tkinter import *
from Cifrar import Cifrar
from AlfabetoMin import AlfabetoMin
from AlfabetoMay import AlfabetoMay
from Separar import Separar


window = Tk()
window.title("Cifrado Cesar")
window.geometry('550x200')

textLabel = Label(window, text="Texto")
textLabel.grid(column=0, row=0)
text = Entry(window, bd = 8)
text.grid(column=1, row=0)

textLabel1 = Label(window, text="Desplazamiento")
textLabel1.grid(column=0, row=1)
displacement = Spinbox(window, from_ = 1, to = 3000)
displacement.grid(column=1, row=1)

cesarLabel = Label(window, text="Cifrado Cesar")
cesarLabel.grid(column=0, row=2)
cifradoLabel = Label(window, text="...")
cifradoLabel.grid(column=0, row=3)

invertLabel = Label(window, text="Texto Invertido")
invertLabel.grid(column=1, row=2)
invertTextLabel = Label(window, text="...")
invertTextLabel.grid(column=1, row=3)

cifradoGrupoLabel = Label(window, text="Cifrado grupos")
cifradoGrupoLabel.grid(column=2, row=2)
groups = Spinbox(window, from_ = 1, to = 3000)
groups.grid(column=2, row=3)
textGroupsLabel = Label(window, text="...")
textGroupsLabel.grid(column=2, row=4)


def cifradoText(event):
    cifradoLabel["text"] = Cifrar.cifrado(text.get(), displacement.get(), AlfabetoMay, AlfabetoMin)
    cifrado = Cifrar.cifrado(text.get(), displacement.get(), AlfabetoMay, AlfabetoMin)
    invertTextLabel["text"] = text.get()[::-1]
    textGroupsLabel["text"] = Separar.dividir(cifrado, groups.get())
text.bind('<KeyRelease>', cifradoText)

displacement.bind('<ButtonPress>', cifradoText)
groups.bind('<ButtonPress>', cifradoText)


window.mainloop()

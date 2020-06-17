from tkinter import *
import os
import subprocess
import webbrowser
from winsound import *
from random import randint


def ouvrir():
    text.insert(1.,open("code.HTML",'r').read())


def sauvegarder():
    open("code.HTML", "w").write(text.get(0., END))

def lancer():
    webbrowser.open('K:\profil\Bureau\HMLedit\code.HTML')

def site():
    open("site.txt", "w").write(tex.get(1., END))
    f = open("site.txt", "r")
    hello = f.read()
    webbrowser.open(hello)


def blanc():
    fen['bg']="white"
    text['bg']="white"
    text['fg']="black"
    tex['bg']="white"
    tex['fg']="black"


def noir():
    fen['bg']="black"
    text['bg']="black"
    text['fg']="white"
    tex['bg']="black"
    tex['fg']="white"

def couleur():
    a = randint(1, 6)

    if a == 1:
        text['fg'] = "red"
    elif a == 2:
        text['fg'] = "blue"
    elif a == 3:
        text['fg'] = "green"
    elif a == 4:
        text['fg'] = "gray"
    elif a == 5:
        text['fg'] = "olive"
    else:
        text['fg'] = "yellow"

def couleur2():
    a = randint(1, 6)

    if a == 1:
        text['bg'] = "red"
    elif a == 2:
        text['bg'] = "blue"
    elif a == 3:
        text['bg'] = "green"
    elif a == 4:
        text['bg'] = "gray"
    elif a == 5:
        text['bg'] = "olive"
    else:
        text['bg'] = "yellow"



fen = Tk()
fen.title('HTMLeditor')
fen.iconbitmap('icone.ico')

fen.configure(bg="black")
text = Text(fen, bg="black", fg="white")
#photo = PhotoImage(file = "run.gif")
#musique_menu = PlaySound("musique.mp3", SND_FILENAME)
text.grid(row=1, column=0, columnspan=10, sticky=N, padx=2, pady=2)
Button(fen, text='Ouvrir', width=10, command=ouvrir, bg="blue").grid(row=2, column=0)
Button(fen, text='Sauvegarder', width=10, command=sauvegarder, bg="red").grid(row=2, column=1)
Button(fen, text='Quitter', width=10, command=fen.quit, bg="yellow").grid(row=2, column=2)
Button(fen, width="10", command=lancer, text="lancer", bg="green").grid(row=2, column=3)
Button(fen, text="site", bg="pink", command=site).grid(row=2, column=5)
Button(fen, text="blanc", bg="white", command=blanc).grid(row=2, column=6)
Button(fen, text="noir", bg="black", fg="white", command=noir).grid(row=2, column=7)
Button(fen, text="couleur", bg="olive", fg="white", command=couleur).grid(row=2, column=8)
Button(fen, text="fond", bg="olive", fg="white", command=couleur2).grid(row=2, column=9)



tex = Text(fen, bg="black", fg="white", width = 5, height = 2)
tex.grid(row=2, column=4)





fen.mainloop()

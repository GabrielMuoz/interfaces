from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.geometry()
raiz.configure(bg='black')

'''frames'''
blueFrame=ttk.Frame(raiz,bg="cyan4",)
blueFrame.grid(column=0, row=0,columnspan=15)
blueFrame.config(borderwidth=20)

darkFrame=ttk.Frame(raiz,bg="black")
darkFrame.grid(column=0, row=1,padx=30)
darkFrame.config()

'''blue frame'''
imagenMenu = PhotoImage(file="menu1.png")
bimagen = ttk.Button(blueFrame,background="cyan4")
bimagen.grid(column=0 ,row=0)
bimagen.config(borderwidth=0)
bimagen['image'] = imagenMenu

spaiLabel=ttk.Label(blueFrame, text=" SPAI 4.0                                                                                                                                                       ", font= ("arial", 15, "bold"), foreground="white", background="cyan4")
spaiLabel.grid(column=1,row=0)

'''black frame'''
tablasFrame=ttk.Frame(darkFrame, bg="black")
tablasFrame.grid(column=0,row=1)

imagenIndicadores = PhotoImage(file="primeraImagen.png")
Pimagen_reducida=imagenIndicadores.subsample(2, 2)
Pimagen = ttk.Label(tablasFrame,background="black")
Pimagen.grid(column=0 ,row=0)
Pimagen.config(borderwidth=2)
Pimagen['image'] = Pimagen_reducida

imagenTemperatura = PhotoImage(file="temperaturas.png")
timagen_reducida=imagenTemperatura.subsample(2, 2)
timagen = ttk.Label(tablasFrame,background="black")
timagen.grid(column=1 ,row=0)
timagen.config(borderwidth=2)
timagen['image'] = timagen_reducida

indicadoresFrame=ttk.Frame(darkFrame, bg="black")
indicadoresFrame.grid(column=0,row=2)

imagenVelocidad = PhotoImage(file="velocidad.png")
vimagen_reducida=imagenVelocidad.subsample(2, 2)
vimagen = ttk.Label(indicadoresFrame,background="black")
vimagen.grid(column=0 ,row=0)
vimagen.config(borderwidth=2)
vimagen['image'] = vimagen_reducida

imagenTanque = PhotoImage(file="tanque.png")
taimagen_reducida=imagenTanque.subsample(2, 2)
taimagen = ttk.Label(indicadoresFrame,background="black")
taimagen.grid(column=1 ,row=0)
taimagen.config(borderwidth=2)
taimagen['image'] = taimagen_reducida

indicadoresFrame=ttk.Frame(darkFrame, bg="black")
indicadoresFrame.grid(column=1,row=1,rowspan=2)

imagenGrafica = PhotoImage(file="grafica.png")
gimagen_reducida=imagenGrafica.subsample(2, 2)
gimagen = ttk.Label(indicadoresFrame,background="black")
gimagen.grid(column=0 ,row=0, sticky=N)
gimagen.config(borderwidth=2)
gimagen['image'] = gimagen_reducida


raiz.mainloop()
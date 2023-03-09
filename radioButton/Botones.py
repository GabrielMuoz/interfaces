from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text="boton solo texto")
boton.grid()

imagen= PhotoImage(file="giants1.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image']= imagen

btnCombinada= ttk.Button(raiz, text="boton combinado", compound="bottom")
btnCombinada.grid()
btnCombinada['image']= imagen

chkBoton = ttk.Checkbutton(raiz, text="opcion 1")
chkBoton.grid()

raiz.mainloop()
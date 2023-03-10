from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.config(bd=25)

nombre = StringVar()
paterno=StringVar()
materno = StringVar()
correo=StringVar()
movil=StringVar()

raiz.title("muestra widgets")

aficiones= ttk.Frame(raiz, padding="10 15 10 15", relief="raised")
aficiones.grid(column=0, row=7, columnspan=1,pady=10)

registro=ttk.Frame(raiz,padding="10 15 10 15", relief="raised")
registro.grid(column=0, row=0, rowspan=6, columnspan=1,pady=10)

oficios=ttk.Frame(raiz, padding="10 15 10 15")
oficios.grid(column=2, row=0, rowspan=6,pady=10)


'''datos'''
nombreEntry=ttk.Entry(registro, width=20, textvariable=nombre)
nombreEntry.grid(column=1,row=0,pady=10)

paternoEntry=ttk.Entry(registro, width=20, textvariable=paterno)
paternoEntry.grid(column=1,row=1,pady=10)

maternoEntry=ttk.Entry(registro, width=20, textvariable=materno)
maternoEntry.grid(column=1,row=2,pady=10)

correoEntry=ttk.Entry(registro, width=20, textvariable=correo)
correoEntry.grid(column=1,row=3,pady=10)

movilEntry=ttk.Entry(registro, width=20, textvariable=movil)
movilEntry.grid(column=1,row=4,pady=10)


ttk.Label(registro, text="usuario:").grid(column=0, row=0, pady=10)
ttk.Label(registro, text="A.paterno:").grid(column=0, row=1, pady=10)
ttk.Label(registro, text="A.materno:").grid(column=0, row=2, pady=10)
ttk.Label(registro, text="correo:").grid(column=0, row=3, pady=10)
ttk.Label(registro, text="movil:").grid(column=0, row=4, pady=10)


'''oficio'''
estudiante=ttk.Radiobutton(oficios, text='estuiante')
estudiante.grid(column=2,row=2,)

empleado=ttk.Radiobutton(oficios, text='empleado')
empleado.grid(column=2,row=3,pady=4, sticky=(N))

desempleo=ttk.Radiobutton(oficios, text='desempleado')
desempleo.grid(column=2,row=4,pady=4, sticky=(N))


'''aficiones'''

ttk.Label(aficiones, text="aficiones").grid(column=0,row=0)

leer=ttk.Checkbutton(aficiones,text="leer")
leer.grid(column=0, row=1)

estudiar=ttk.Checkbutton(aficiones,text="estuiar")
estudiar.grid(column=1, row= 1)

videojuegos=ttk.Checkbutton(aficiones,text="videojuegos")
videojuegos.grid(column=2, row= 1)

'''estado'''
estados=ttk.Combobox(raiz, text= "estados")
estados.grid(column=2,row=7)
estados['values']=("jalisco", "nayarit", "colima","michoacan" )

'''guardar y cancelar'''

ttk.Button(raiz, text="guardar").grid(column=0,row=8)
ttk.Button(raiz, text="cancelar").grid(column=1,row=8)


raiz.mainloop()

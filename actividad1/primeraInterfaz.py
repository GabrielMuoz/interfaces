from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.geometry("600x450")


'''notebook'''
notebook=ttk.Notebook(raiz)
notebook.pack(expand=True, fill=BOTH)

tab1=ttk.Frame(notebook)
tab2=ttk.Frame(notebook)
tab3=ttk.Frame(notebook)
tab4=ttk.Frame(notebook)
tab5=ttk.Frame(notebook)


'''frames'''
blank=ttk.Frame(tab1,padding="10 15 10 15",width=600, height=10, relief="groove")
blank.grid(column=0, row=1, sticky=(W,N,E,S))

datos=ttk.Frame(tab1, padding="10 20 10 20",width=600, height=110, relief="groove")
datos.grid(column=0, row=2, sticky=(W,N,E,S))

tarjeta=ttk.Frame(tab1,padding="10 20 10 20", width=600, height=110, relief="groove")
tarjeta.grid(column=0, row=3, sticky=(W,N,E,S))

room=ttk.Frame(tab1, padding="10 20 10 20",width=600,height=110, relief="groove" )
room.grid(column=0, row=4, sticky=(W,N,E,S))

terminar=ttk.Frame(tab1, padding="10 20 10 20",width=600, height=110)
terminar.grid(column=0, row=5, sticky=())



'''style'''
style=ttk.Style()
style.configure("menuStyle", backgroun='blue')

'''tabs'''
notebook.add(tab1,text='                add           ')
notebook.add(tab2,text='                   delete           ')
notebook.add(tab3,text='                search             ')
notebook.add(tab4,text='                 services             ')
notebook.add(tab5,text='                 help             ')

'''blank'''
ttk.Label(blank,text="")

'''datos'''

nombreEntry=ttk.Entry(datos)
nombreEntry.grid(column=1,row=0,columnspan=3, padx=10, pady=20)

apellidoEntry=ttk.Entry(datos)
apellidoEntry.grid(column=5,row=0,columnspan=6, padx=10)

diaEntry=ttk.Entry(datos, width=3)
diaEntry.grid(column=1,row=1, padx=4)

mesEntry=ttk.Entry(datos, width=3)
mesEntry.grid(column=2,row=1, padx=4)

añoEntry=ttk.Entry(datos, width=5)
añoEntry.grid(column=3,row=1,padx=4)

ciudadEntry=ttk.Entry(datos)
ciudadEntry.grid(column=5,row=1,padx=10)

ttk.Label(datos, text="nombre").grid(column=0, row=0, pady=7)
ttk.Label(datos, text="apellio").grid(column=4, row=0)
ttk.Label(datos, text="fecha de nacimiento").grid(column=0, row=1, pady=7)
ttk.Label(datos, text="ciudad").grid(column=4, row=1)

'''tarjeta'''
tarjetaEntry=ttk.Entry(tarjeta)
tarjetaEntry.grid(column=1,row=0, pady=15, sticky=(N))


ttk.Label(tarjeta, text="Tarjeta de creito(si hay): ").grid(column=0,row=0)
ttk.Label(tarjeta, text="Tipo de tarjeta de creito(si hay): ").grid(column=0,row=1)


visa=ttk.Radiobutton(tarjeta, text='visa')
visa.grid(column=1,row=1)

masterCard=ttk.Radiobutton(tarjeta, text='Mastercard')
masterCard.grid(column=2,row=1)

'''cuarto'''
ttk.Label(room, text="tipo de cuarto: ").grid(column=0,row=0)
ttk.Label(room, text="Tiempo de estancia(dias): ").grid(column=2,row=0,padx=20)

normal=ttk.Radiobutton(room, text='normal')
normal.grid(column=1,row=0,padx=15)
familiar=ttk.Radiobutton(room, text='familiar')
familiar.grid(column=1,row=1)
especial=ttk.Radiobutton(room, text='especial')
especial.grid(column=1,row=2)

diasEntry=ttk.Entry(room, width=6)
diasEntry.grid(column=3,row=0)

'''final'''
ttk.Button(terminar, text="Submit").grid()


raiz.mainloop()
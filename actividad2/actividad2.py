from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
import tkinter as ttk

raiz = Tk()


'''frames'''
darkFrame=ttk.Frame(raiz,bg="black")
darkFrame.grid(column=0, row=1, sticky=(W,N,E,S), rowspan=2)

greyFrame=ttk.Frame(darkFrame, background="gray40")
greyFrame.grid(column=0, row=0, sticky=(W,N,E,S))


maronFrame=ttk.Frame(darkFrame, bg="#482525")
maronFrame.grid(column=0,row=1,padx=30)
maronFrame.config(borderwidth=20)

tableFrame=ttk.Frame(maronFrame,bg="#482525")
tableFrame.grid(column=0,row=7,columnspan=5)

'''titulo'''
imagen = PhotoImage(file="carrito.png")
bimagen = ttk.Label(greyFrame,background="gray40")
bimagen.grid(column=0 ,row=0,sticky=(W,N))
bimagen['image'] = imagen

ttk.Label(greyFrame, text="Prouct management  ", background="gray40", font= ("arial", 30, "bold"), foreground="white").grid(column=1,row=0)

'''frame marron'''
id=ttk.Label(maronFrame, text="id_protect",bg="#482525",foreground="white")
id.grid(column=0,row=1)

name=ttk.Label(maronFrame, text="name",bg="#482525",foreground="white")
name.grid(column=0,row=2)

descripcion=ttk.Label(maronFrame, text="descripcion",bg="#482525",foreground="white")
descripcion.grid(column=0,row=3)

quantity=ttk.Label(maronFrame, text="quantity",bg="#482525",foreground="white")
quantity.grid(column=0,row=4)

price=ttk.Label(maronFrame, text="price",bg="#482525",foreground="white")
price.grid(column=0,row=5)

nameEntry=ttk.Entry(maronFrame)
nameEntry.grid(column=1,row=1,pady=5)

nameEntry=ttk.Entry(maronFrame)
nameEntry.grid(column=1,row=2,pady=5)

nameEntry=ttk.Entry(maronFrame)
nameEntry.grid(column=1,row=3,pady=5)

nameEntry=ttk.Entry(maronFrame)
nameEntry.grid(column=1,row=4,pady=5)

nameEntry=ttk.Entry(maronFrame)
nameEntry.grid(column=1,row=5,pady=5)

lupimag = PhotoImage(file="Limpiar.png")
Lumagen = ttk.Button(maronFrame,background="#482525" )
Lumagen.config(borderwidth=0)
Lumagen.grid(column=3 ,row=0,sticky=(W,N), pady=10)
Lumagen['image'] = lupimag

Limimag = PhotoImage(file="lup.png")
Limagen = ttk.Button(maronFrame,background="#482525" )
Limagen.config(borderwidth=0)
Limagen.grid(column=4 ,row=0,sticky=(W,N), pady=10)
Limagen['image'] = Limimag

backButton=ttk.Button(maronFrame,background="#482525",text="Back", compound="bottom",foreground="purple1")
backButton.config(borderwidth=0)
backButton.grid(column=5,row=0, pady=10)

saveButton=ttk.Button(maronFrame,background="SpringGreen4", compound="bottom", foreground="ghost white",text="Save",width=13)
saveButton.config(borderwidth=0)
saveButton.grid(column=3,row=1,columnspan=5, pady=5,padx=15)

deleteButton=ttk.Button(maronFrame,background="red3", compound="bottom", foreground="ghost white",text="Delete",width=13)
deleteButton.config(borderwidth=0)
deleteButton.grid(column=3,row=2,columnspan=5,pady=5,padx=15)

updateButton=ttk.Button(maronFrame,background="DarkOrange1", compound="bottom", foreground="ghost white",text="Update", width=13)
updateButton.config(borderwidth=0)
updateButton.grid(column=3,row=3,columnspan=5,pady=5, padx=15)


'''tabla'''
ttk.Label(tableFrame, text="idproduit", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(tableFrame, text="namep", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(tableFrame, text="description", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(tableFrame, text="quantity", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(tableFrame, text="unite_price", width=10, bg="gray", fg="white").grid(row=0, column=4)

data = [
    ("1", "Condia", "lait", "24", "100.0"),
    ("2", "la vache quirit", "fromage", "200", "300.0"),
    ("3", "hamound boualam", "boisson gaseuse", "98", "90.0"),
    ("4", "Mina", "Chocolat", "80", "50.0"),
    ("5", "Aroma", "cafe", "60", "80.0"),
    ("6", "Facto", "Facto", "7000", "600.0"),
    ("", "", "", "", ""),
    ("", "", "", "", ""),
    ("", "", "", "", "")
]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(tableFrame, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j, sticky=(W))





raiz.mainloop()
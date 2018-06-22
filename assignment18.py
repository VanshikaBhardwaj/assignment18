
import tkinter as tk
from tkinter import *

# q1
dict = {'ABC': '456737847', 'ANUBHI': '9394839783', 'ANUJ': '7366384683', 'SUSHANT': '98938985'}
c = tk.Tk()
f = Frame(master=c)
f.pack()
scroll = Scrollbar(master=f)
scroll.pack(fill=Y, side=RIGHT)
l = Listbox(f, yscrollcommand=scroll.set)
l.pack()
for key in dict:
    l.insert(END, '{}'.format(key))


# q2
def add():
    dict.update({a.get(): b.get()})
    for key in dict.keys():
        print(key)
    i = key
    l.insert(END, i)


bu = Button(master=f, text="Add", command=add)
bu.pack()
la = Label(f,text="Enter name and phone number:")
la.pack()
a = Entry(f, text="Name:")
b = Entry(f, text="Phone no:")
a.pack()
b.pack()
c.mainloop()
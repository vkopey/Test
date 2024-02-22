# -*- coding: utf-8 -*-
from tkinter import * # імпортувати все з модуля Tkinter
def Button1Click(): # функція, яка викликається під час натиску на Button1
    x=float(s.get()) # присвоїти `x` значення `s`
    s.set(x**2) # установити `s` значення x**2
root = Tk() # головне вікно програми
root.title('Simple GUI app') # надпис на вікні
root.resizable(width=TRUE, height=FALSE) # дозволити зміну розміру вікна по ширині
root.geometry("200x150+0+0") # розмір вікна
Button1=Button(root, text="SQR", command=Button1Click) # створити кнопку, пов'язати з функцією command1
Button1.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.1) # розташувати на вікні
#Button1.pack(side=RIGHT) # або розташувати на вікні справа
s=StringVar() # створити рядкову змінну
Entry1 = Entry(root,textvariable=s,width=10) # створити поле вводу, пов'язати зі змінною s
Entry1.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1) # розташувати на вікні
s.set(0) # установити рядковій змінній значення 0
root.mainloop() # головний цикл програми (для обробки подій)
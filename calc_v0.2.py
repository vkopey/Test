from tkinter import * # імпортувати все з модуля Tkinter
from math import *
S="+ - * / sqrt sin cos tan asin acos atan log log10".split(" ")
B=[eval('lambda: calculate("'+s+'")') for s in S]

def calculate(s):
    try:
        x=float(s1.get())
        y=float(s2.get())
    except:
        s3.set('error!')
        return
    #if s in '+-*' and type(x) in [int, float] and type(y) in [int, float]:
    if s in "+-*/":
        z=eval('x'+s+'y')
    else:
        z=eval(s+'(x)')
    s3.set(z)

root = Tk() # головне вікно програми
root.title('Simple GUI app') # надпис на вікні
root.resizable(width=TRUE, height=FALSE) # дозволити зміну розміру вікна по ширині
root.geometry("350x150+100+100") # розмір вікна

x,y=0.5,0.3
for s,f in zip(S,B):
    Button(root, text=s, command=f).place(relx=x, rely=y, relwidth=0.1, relheight=0.1)
    x+=0.11
    if x>0.8: x=0.5; y+=0.11

s1=StringVar() # створити рядкову змінну
Entry1 = Entry(root, textvariable=s1, width=10) # створити поле вводу, пов'язати зі змінною s
Entry1.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.1) # розташувати на вікні

s2=StringVar() # створити рядкову змінну
Entry2 = Entry(root, textvariable=s2, width=10) # створити поле вводу, пов'язати зі змінною s
Entry2.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1) # розташувати на вікні

s3=StringVar() # створити рядкову змінну
Entry3 = Entry(root, textvariable=s3, width=10) # створити поле вводу, пов'язати зі змінною s
Entry3.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1) # розташувати на вікні
s3.set(0) # установити рядковій змінній значення 0

root.mainloop() # головний цикл програми (для обробки подій)
from tkinter import * # імпортувати все з модуля Tkinter
from tkinter import messagebox
from math import *
import sys
ver="Calculator v.0.4"

S="a+b a-b a*b a/b a**b sqrt(a) sin(a) cos(a) tan(a) asin(a) acos(a) atan(a) exp(a) log(a) log10(a) log(a,b) eval(a) evalw(a) e pi".split(" ")
B=[eval('lambda: calculate("'+s+'")') for s in S]

def calculate(s):
    try:
        a=float(s1.get())
    except:
        a=s1.get()
    b=float(s2.get())
    #if s in '+-*' and type(x) in [int, float] and type(y) in [int, float]:
    c=eval(s)
    s3.set(c)
    List1.insert(END, a, b, c)

def evalw(s):
    from urllib.request import urlopen
    html = urlopen('http://localhost:8080/hello/%s'%s).read()
    return html

def list1_dbl_click(e):
    i=List1.curselection()
    text=List1.get(i)
    s1.set(text)

def menu_save():
    D=List1.get(0, List1.size())
    f=open("calc_data.txt", "w")
    f.writelines(str(D))
    f.close()

def menu_open():
    f=open("calc_data.txt", "r")
    s=f.read()
    D=s[1:-1].split(', ')
    List1.insert(END, *D)
    f.close()

def menu_to(m):
    i=List1.curselection()
    text=List1.get(i)
    if m==1: s1.set(text)
    if m==2: s2.set(text)

root = Tk() # головне вікно програми
root.title(ver) # надпис на вікні
root.resizable(width=TRUE, height=FALSE) # дозволити зміну розміру вікна по ширині
root.geometry("500x200+100+100") # розмір вікна

x,y=0.45,0.1
for s,f in zip(S,B):
    Button(root, text=s, command=f).place(relx=x, rely=y, relwidth=0.1, relheight=0.1)
    x+=0.11
    if x>0.7: x=0.45; y+=0.11

s1=StringVar() # створити рядкову змінну
Entry1 = Entry(root, textvariable=s1, width=10) # створити поле вводу, пов'язати зі змінною s
Entry1.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.1) # розташувати на вікні
Label(root, text="a=").place(relx=0.0, rely=0.3, relwidth=0.1, relheight=0.1)

s2=StringVar() # створити рядкову змінну
Entry2 = Entry(root, textvariable=s2, width=10) # створити поле вводу, пов'язати зі змінною s
Entry2.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1) # розташувати на вікні
Label(root, text="b=").place(relx=0.0, rely=0.5, relwidth=0.1, relheight=0.1)

s3=StringVar() # створити рядкову змінну
Entry3 = Entry(root, textvariable=s3, width=10) # створити поле вводу, пов'язати зі змінною s
Entry3.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1) # розташувати на вікні
s3.set(0) # установити рядковій змінній значення 0
Label(root, text="res=").place(relx=0.0, rely=0.7, relwidth=0.1, relheight=0.1)

List1=Listbox(root)
List1.place(relx=0.8, rely=0.0, relwidth=0.2, relheight=1.0)
List1.bind("<Double-Button-1>", list1_dbl_click)

menu1 = Menu(root) # створити меню
root.config(menu=menu1) # установити меню для вікна
menu11 = Menu(menu1) # створити підменю
menu1.add_cascade(label='File', menu=menu11) # додати підменю
menu11.add_command(label='Save',command=menu_save) # додати елемент меню
menu11.add_command(label='Open',command=menu_open) # додати елемент меню
menu11.add_command(label='Exit',command=sys.exit) # додати елемент меню
menu12 = Menu(menu1) # створити підменю
menu1.add_cascade(label='Edit', menu=menu12) # додати підменю
menu12.add_command(label='To a',command=lambda: menu_to(1)) # додати елемент меню
menu12.add_command(label='To b',command=lambda: menu_to(2)) # додати елемент меню
menu13 = Menu(menu1) # створити підменю
menu1.add_cascade(label='Help', menu=menu13) # додати підменю
menu13.add_command(label='About',command=lambda: messagebox.showinfo('About', ver+'\nhttps://github.com/vkopey/Test')) # додати елемент меню
menu_open()

root.mainloop() # головний цикл програми (для обробки подій)
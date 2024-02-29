from tkinter import * # імпортувати все з модуля Tkinter
import math

def Button1Click(): # функція, яка викликається під час натиску на Button1
    calculate("+")

def Button2Click(): # функція, яка викликається під час натиску на Button2
    calculate("-")

def Button3Click(): # функція, яка викликається під час натиску на Button3
    calculate("*")

def Button4Click(): # функція, яка викликається під час натиску на Button3
    calculate("sqrt")

def Button5Click(): # функція, яка викликається під час натиску на Button3
    calculate("sin")

def calculate(s):
    try:
        x=float(s1.get())
        y=float(s2.get())
    except:
        s3.set('error!')
        return
    #if s in '+-*' and type(x) in [int, float] and type(y) in [int, float]:
    #z=eval('x'+s+'y')
    if s=='+': z=x+y
    if s=='-': z=x-y
    if s=='*': z=x*y
    if s=='sqrt': z=x**0.5
    if s=='sin': z=math.sin(x)
    s3.set(z)

root = Tk() # головне вікно програми
root.title('Simple GUI app') # надпис на вікні
root.resizable(width=TRUE, height=FALSE) # дозволити зміну розміру вікна по ширині
root.geometry("200x150+100+100") # розмір вікна

B=(('+',Button1Click),
   ('-',Button2Click),
   ('*', Button3Click),
   ('sqrt', Button4Click),
   ('sin', Button5Click))

x,y=0.5,0.3
for s,f in B:
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
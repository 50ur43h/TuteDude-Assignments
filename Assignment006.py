#Module 10 & 11: CALCULATOR USING TKINTER

from tkinter import *
import math

win = Tk()
win.geometry('500x500')


eb = Entry(win, width=58, borderwidth=5)
eb.place(x=0, y=0)


def click(num):
    result = eb.get()
    eb.delete(0, END)
    eb.insert(0, str(result) + str(num))


def prcnt():
    num1 = eb.get()
    prcntg = 10
    eb.delete(0, END)
    eb.insert(0, (prcntg/100)*float(num1))
b = Button(win, text='%', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=prcnt)
b.place(x=5, y=30)

def clrentry():
    eb.delete(0, END)
b = Button(win, text='CE', bg='orange', fg='white', width=7, font=('Arial', 12, 'bold'), command=clrentry)
b.place(x=95, y=30)

def clear():
    global a, cal
    eb.delete(0, END)
    a = cal = NONE
b = Button(win, text='C', bg='orange', fg='white', width=7, font=('Arial', 12, 'bold'), command=clear)
b.place(x=185, y=30)

def bkspc():
    num1 = eb.get()
    eb.delete(len(num1) - 1, END)
b = Button(win, text='<-', bg='red', fg='white', width=7, font=('Arial', 12, 'bold'), command=bkspc)
b.place(x=275, y=30)

def expo():
    num1 = eb.get()
    eb.delete(0, END)
    eb.insert(0, 1 / float(num1))
b = Button(win, text='1/x', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=expo)
b.place(x=5, y=65)

def sqr():
    num1 = eb.get()
    eb.delete(0, END)
    eb.insert(0, int(num1) ** 2)
b = Button(win, text='x^2', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=sqr)
b.place(x=95, y=65)

def sqrt():
    num1 = eb.get()
    eb.delete(0, END)
    eb.insert(0, math.sqrt(int(num1)))
b = Button(win, text='x^(1/2)', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=sqrt)
b.place(x=185, y=65)

def mul():
    num1 = eb.get()
    global cal, a
    cal = "multiplication"
    a = float(num1)
    eb.delete(0, END)
b = Button(win, text='*', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=mul)
b.place(x=275, y=65)

b = Button(win, text='7', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(7))
b.place(x=5, y=100)

b = Button(win, text='8', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(8))
b.place(x=95, y=100)

b = Button(win, text='9', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(9))
b.place(x=185, y=100)

def div():
    num1 = eb.get()
    global cal, a
    cal = "division"
    a = float(num1)
    eb.delete(0, END)
b = Button(win, text='/', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=div)
b.place(x=275, y=100)

b = Button(win, text='4', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(4))
b.place(x=5, y=135)

b = Button(win, text='5', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(5))
b.place(x=95, y=135)

b = Button(win, text='6', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(6))
b.place(x=185, y=135)

def add():
    num1 = eb.get()
    global cal, a
    cal = "addition"
    a = float(num1)
    eb.delete(0, END)
b = Button(win, text='+', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=add)
b.place(x=275, y=135)

b = Button(win, text='1', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(1))
b.place(x=5, y=170)

b = Button(win, text='2', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(2))
b.place(x=95, y=170)

b = Button(win, text='3', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(3))
b.place(x=185, y=170)

def sub():
    num1 = eb.get()
    global cal, a
    cal = "subtraction"
    a = float(num1)
    eb.delete(0, END)
b = Button(win, text='-', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=sub)
b.place(x=275, y=170)

def sign():
    num1 = eb.get()
    if num1:
        if num1.startswith('-'):
            eb.delete(0, 'end')
            eb.insert(0, num1[1:])
        else:
            eb.delete(0, 'end')
            eb.insert(0, '-' + num1)
b = Button(win, text='+/-', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=sign)
b.place(x=5, y=205)

b = Button(win, text='0', bg='black', fg='white', width=7, font=('Arial', 12, 'bold'), command=lambda: click(0))
b.place(x=95, y=205)

def dcml():
    num1 = eb.get()
    if '.' not in num1:
        eb.insert('end', '.')
b = Button(win, text='.', bg='blue', fg='white', width=7, font=('Arial', 12, 'bold'), command=dcml)
b.place(x=185, y=205)

def equal():
    num2 = eb.get()
    eb.delete(0, END)
    if cal == "addition":
        res = a + float(num2)
    elif cal == "subtraction":
        res = a - float(num2)
    elif cal == "multiplication":
        res = a * float(num2)
    elif cal == "division":
        res = a / float(num2)
    eb.insert(0, int(res) if res == int(res) else res)
b = Button(win, text='=', bg='green', fg='white', width=7, font=('Arial', 12, 'bold'), command=equal)
b.place(x=275, y=205)


mainloop()
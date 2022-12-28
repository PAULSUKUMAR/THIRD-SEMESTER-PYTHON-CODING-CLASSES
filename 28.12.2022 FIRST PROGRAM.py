from tkinter import *
def addNumbers():
    a=int(e1.get())
    b=int(e2.get())
    res=a+b
    s.set(res)
def subtractnumbers():
    a=int(e1.get())
    b=int(e2.get())
    res=a-b
    s.set(res)
def multiplenumbers():
    a=int(e1.get())
    b=int(e2.get())
    res=a*b
    s.set(res)
def dividenumbers():
    a=int(e1.get())
    b=int(e2.get())
    res=a/b
    s.set(res)    
cal = Tk()
s=StringVar()
Label(cal, text="First").grid(row=0,column=0)
Label(cal, text="Second").grid(row=1,column=0)
Label(cal, text="Result:").grid(row=2,column=0)
result=Label(cal, text="", textvariable=s).grid(row=2,column=1)
e1 = Entry(cal)
e2 = Entry(cal)
e3 = Entry(cal)
e4 = Entry(cal)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
b1 = Button(cal, text="Addition", command=addNumbers)
b2 = Button(cal, text="Subtraction", command=subtractnumbers)
b3=Button(cal,text="Multiplication",command=multiplenumbers)
b4=Button(cal,text="Division",command=dividenumbers)
b1.grid(row=3)
b2.grid(row=4)
b3.grid(row=5)
b4.grid(row=6)
mainloop()

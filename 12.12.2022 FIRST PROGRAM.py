from tkinter import *
s=Tk()
s.title("STUDENT APPLICATION FORM")
Label(s,text="STUDENT ID:").grid(row=0,column=0)
Label(s,text="STUDENT NAME:").grid(row=1,column=0)
Label(s,text="FATHER NAME:").grid(row=2,column=0)
Label(s,text="GROUP:").grid(row=3,column=0)
Label(s,text="PHONE NUMBER:").grid(row=4,column=0)
Label(s,text="EMAIL ID:").grid(row=5,column=0)
Label(s,text="ADDRESS:").grid(row=6,column=0)
e1=Entry(s)
e2=Entry(s)
e3=Entry(s)
e4=Entry(s)
e5=Entry(s)
e6=Entry(s)
e7=Entry(s)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)
Button(s,text="SUBMIT").grid(row=7,column=0)
Button(s,text="CANCEL").grid(row=7,column=1)
mainloop()








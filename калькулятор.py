from tkinter import *
a=0
b=0
c=0
def plus():
    a=float(e1.get())
    b=float(e2.get())
    c=a+b
    lbl['text'] = c
def minus():
    a=float(e1.get())
    b=float(e2.get())
    c=a-b
    lbl['text'] = c
def umn():
    a=float(e1.get())
    b=float(e2.get())
    c=a*b
    lbl['text'] = c
def deel():
    a=float(e1.get())
    b=float(e2.get())
    c=a/b
    lbl['text'] = c
def stepen():
    a=float(e1.get())
    b=float(e2.get())
    c=a**b
    lbl['text'] = c
root=Tk()
lbl=Label(background="gray24", foreground="OliveDrab1", border="5")
lbl.pack(fill=X, side=BOTTOM)
e1=Entry(background="gray24", foreground="OliveDrab1", border="5")
e1.pack(fill=X, side=BOTTOM)
e2=Entry(background="gray24", foreground="OliveDrab1", border="5")
e2.pack(fill=X, side=BOTTOM)


btn1=Button(text='+',width=20, command=plus)
btn1.pack(fill=X)
btn2=Button(text='-',width=20,command=minus)
btn2.pack(fill=X)
btn3=Button(text='*',width=20,command=umn)
btn3.pack(fill=X)
btn4=Button(text='/',width=20,command=deel)
btn4.pack(fill=X)
btn5=Button(text='^', width=20, command=stepen)
btn5.pack(fill=X)
root.mainloop()

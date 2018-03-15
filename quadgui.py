#!/usr/bin/python
from math import sqrt as sroot
from fractions import Fraction
from random import randint
import tkinter
class calc(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.a = tkinter.Entry(self)
        self.b = tkinter.Entry(self)
        self.c = tkinter.Entry(self)
        self.a.grid(columnspan=1, column=0, row=0)
        self.b.grid(columnspan=1, column=1, row=0)
        self.c.grid(columnspan=1, column=2, row=0)
        self.a.bind("<Return>", self.dothis)
        self.b.bind("<Return>", self.dothis)
        self.c.bind("<Return>", self.dothis)
        self.x1 = tkinter.StringVar()
        self.x2 = tkinter.StringVar()
        self.maxmin = tkinter.StringVar()
        self.maxmin_lab = tkinter.StringVar()
        x1_label = tkinter.Label(self, textvariable=self.x1, anchor="w")
        x2_label = tkinter.Label(self, textvariable=self.x2, anchor='w')
        maxmin_label = tkinter.Label(self, textvariable=self.maxmin_lab, anchor='w')
        maxmincoord = tkinter.Label(self, textvariable=self.maxmin, anchor="w")
        maxmin_label.grid(column=0, row = 3)
        maxmincoord.grid(column = 2, row=3)
        
        x1_label.grid(row=2, column=0)
        x2_label.grid(row=2, column=1)
    
    def f(self, x, a, b, c):
        return a*x**2+b*x+c

    def get_max_min(self, a, b, c):
        h = float((-1*b)/(2*a))
        k = self.f(h, a, b, c)
        if a < 0:
            self.maxmin_lab.set("Minimun")
        else:
            self.maxmin_lab.set("Maximum")
        self.maxmin.set("("+str(h)+","+str(k)+")")


    def get_x_int(self, i, a, b, c):
        try:
            rooty = sroot(((b**2)-4*a*c))
        except:
            rooty = sroot(-1*((b**2)-4*a*c))
        root1 = (-b + rooty)/(2*a)
        root2 = (-b - rooty)/(2*a)
        if i == 1:
            return root1
        elif i == 0:
            return root2
        else:
                exit
    def dothis(self, event):
        a = float(self.a.get())
        b = float(self.b.get())
        c= float(self.c.get())
        xint = [str(Fraction((self.get_x_int(1, a, b, c)))), str(Fraction((self.get_x_int(0, a, b, c))))]
        self.x1.set(xint[0])
        self.x2.set(xint[1])
        self.get_max_min(a, b, c)
if __name__ == "__main__":
    app = calc(None)
    app.title("calc")
    app.mainloop()

#!/usr/bin/python
from tkinter import Tk, Label, Button 

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("First shot!!")
        
        self.label = Label(master, text="I FUCKING LOVE HAILEY LYNN NEVILLE")
        self.label.pack()

        self.greet_button = Button(master, text="greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="close", command=master.quit)
        self.close_button.pack()


    def greet(self):
        print("greetings")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

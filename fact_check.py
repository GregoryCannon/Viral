import sys
from tkinter import *
from __main__ import *

   
class FactCheckGui:
    def __init__(self, master, truths, cat_names, inp):
        self.master = master
        self.i = 0
        self.truths = truths
        master.title("Fact Checker GUI")

        self.label = Label(master, text="Click the info to see if it's right! Then click 'Clear Info'")
        self.label.pack(pady=25)

        
        self.cat0 = Label(master, text=cat_names[0])
        self.cat0.pack(pady=(10,0))
        self.opt00 = Button(master, text=inp[0][0], command=lambda : self.check(inp[0][0]))
        self.opt00.pack()
        self.opt01 = Button(master, text=inp[0][1], command=lambda : self.check(inp[0][1]))
        self.opt01.pack()
        self.opt02 = Button(master, text=inp[0][2], command=lambda : self.check(inp[0][2]))
        self.opt02.pack()

        self.cat1 = Label(master, text=cat_names[1])
        self.cat1.pack(pady=(10,0))
        self.opt10 = Button(master, text=inp[1][0], command=lambda : self.check(inp[1][0]))
        self.opt10.pack()
        self.opt11 = Button(master, text=inp[1][1], command=lambda : self.check(inp[1][1]))
        self.opt11.pack()
        self.opt12 = Button(master, text=inp[1][2], command=lambda : self.check(inp[1][2]))
        self.opt12.pack()

        self.cat2 = Label(master, text=cat_names[2])
        self.cat2.pack(pady=(10,0))
        self.opt20 = Button(master, text=inp[2][0], command=lambda : self.check(inp[2][0]))
        self.opt20.pack()
        self.opt21 = Button(master, text=inp[2][1], command=lambda : self.check(inp[2][1]))
        self.opt21.pack()
        self.opt22 = Button(master, text=inp[2][2], command=lambda : self.check(inp[2][2]))
        self.opt22.pack()

        self.cat3 = Label(master, text=cat_names[3])
        self.cat3.pack(pady=(10,0))
        self.opt30 = Button(master, text=inp[3][0], command=lambda : self.check(inp[3][0]))
        self.opt30.pack()
        self.opt31 = Button(master, text=inp[3][1], command=lambda : self.check(inp[3][1]))
        self.opt31.pack()
        self.opt32 = Button(master, text=inp[3][2], command=lambda : self.check(inp[3][2]))
        self.opt32.pack()

        #self.clear_button = Button(master, text="Clear Info", command=self.clear_label)
        #self.clear_button.pack()

        #self.truth_button = Button(master, text="Reveal Truth", command=self.show_truth)
        #self.truth_button.pack(pady=50)

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack(pady=0)
        self.bot_label = Label(master, text="Made by Brian, Greg, Suki, Forrest and Gabby")
        self.bot_label.pack(pady=(35,15))

    def change_label(self):
        self.label.config(text=cards[self.i])
        self.i += 1

    def clear_label(self):
        self.label.config(text = "                                                                             ")

    def check(self,guess):
        print(guess)
        truefalse = "True" if guess in self.truths else "False"
        self.label.config(text=truefalse)
        self.master.after(1000, self.clear_label)
        

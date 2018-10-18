import sys
from Tkinter import *
from __main__ import *

   
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.i = 0
        master.title("Fact Checker GUI")

        self.label = Label(master, text="Click the info to see if it's right! Then click 'Clear Info'")
        self.label.pack(pady=25)

        '''
        self.cat0 = Label(master, text=cat_names[0])
        self.cat0.pack(pady=25)
        self.opt0 = Button(master, text=inp[0][0], command=self.check(inp[0][0]))
        self.opt0.pack()
        self.opt1 = Button(master, text=inp[0][1], command=self.check(inp[0][1]))
        self.opt1.pack()
        self.opt2 = Button(master, text=inp[0][2], command=self.check(inp[0][2]))
        self.opt2.pack()'''

        self.clear_button = Button(master, text="Clear Info", command=self.clear_label)
        self.clear_button.pack()

        self.truth_button = Button(master, text="Reveal Truth", command=self.show_truth)
        self.truth_button.pack(pady=50)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(pady=0)

        self.bot_label = Label(master, text="Made by XX")
        self.bot_label.pack(pady=100)

    def greet(self):
        print("Greetings!")

    def change_label(self):
        self.label.config(text=cards[self.i])
        self.i += 1

    def clear_label(self):
        self.label.config(text = '')

    def check(self,guess):
        print(guess)
        

root = Tk()

root.title('The game')
#You can set the geometry attribute to change the root windows size
root.geometry("500x500") #You want the size of the app to be 500x500
root.resizable(0, 0)
back = Frame(master=root,bg='grey')
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=BOTH, expand=1)

my_gui = MyFirstGUI(root)
root.mainloop()

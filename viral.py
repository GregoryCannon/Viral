from brian import *
from Tkinter import *
import random
import sys,os
#test

cat_names = []
inp = []
truths = []
lies = []


'a'
 

numcats = 4
numopts = 3

for i in range(numcats):
    newname = input("Input a category name: ")
    cat_names.append(newname)

for i in range(numcats):
    catname = cat_names[i]
    cur_lies = []
    cur_inp = []
    for i in range(numopts):
        opt = input("Enter an option for category \"" + catname + "\": ")
        cur_lies.append(opt)
        cur_inp.append(opt)
    cur_truth = random.choice(cur_lies)
    truths.append(cur_truth)
    cur_lies.remove(cur_truth)
    lies.append(cur_lies)
    inp.append(cur_inp)

print("catnames", cat_names)
print("truths", truths)
print("lies", lies)
print("input", inp)

cards = []
for i in range(100):
    cards.append(getcard(cat_names, inp, truths, lies))

intro_string = "Click 'View Card' to see info, click 'Clear Info' when done"

   
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.i = 0
        master.title("Viral!")

        self.label = Label(master, text=intro_string)
        self.label.pack(pady=25)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.change_button = Button(master, text="View Card", command=self.change_label)
        self.change_button.pack()

        self.clear_button = Button(master, text="Clear Info", command=self.clear_label)
        self.clear_button.pack()

        self.launch_button = Button(master, text="Fact Check", command=self.launch_gui)
        self.launch_button.pack(pady=50)

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
        self.label.config(text = intro_string)

    def show_truth(self):
        self.label.config(text = truths)

    def launch_gui(self):
        import fact_check
        

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

'''





import tkinter as tk

def startgame():
    pass

mw = tk.Tk()

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
mw.option_add("*Button.Background", "black")
mw.option_add("*Button.Foreground", "red")

mw.title('The game')
#You can set the geometry attribute to change the root windows size
mw.geometry("500x500") #You want the size of the app to be 500x500
mw.resizable(0, 0) #Don't allow resizing in the x or y direction

back = tk.Frame(master=mw,bg='black')
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

#Changed variables so you don't have these set to None from .pack()
go = tk.Button(master=back, text='Start Game', command=startgame)
go.pack()
close = tk.Button(master=back, text='Quit', command=mw.destroy)
close.pack()
info = tk.Label(master=back, text='Made by me!', bg='red', fg='black')
info.pack()

mw.mainloop()


'''

'''
import tkinter as tk
counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
'''

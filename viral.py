from brian import *
from fact_check import *
from tkinter import *
import random
import datetime
import sys,os

#-----------------
# Get Categories
#-----------------
cat_names = ['Person', 'Place', 'Accomplice', 'What Happened?']
truths = ['1', '6', '9', '10']
lies = [['2', '3'], ['4', '5'], ['7', '8'], ['11', '12']]
inp = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']]

numcats = 4
numopts = 3

skip_inputs = input("Skip inputting? input 1 or 0: ")
if (skip_inputs == "0"):
    cat_names = []
    truths = []
    lies = []
    inp = []

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

print("cat_names", cat_names)
print("truths", truths)
print("lies", lies)
print("inp", inp)

#-----------------
# Generate Cards
#-----------------
cards = []
for i in range(100):
    cards.append(getcard(cat_names, inp, truths, lies))

intro_string = "Click 'Generate Story' to see your story.\nThen click 'Clear Display' when done"


def launch_fact_check():
    ### Fact Check
    fc_root = Tk()

    fc_root.title('The game')
    #You can set the geometry attribute to change the root windows size
    fc_root.geometry("500x600") #You want the size of the app to be 500x500
    fc_root.resizable(0, 0)
    fc_back = Frame(master=fc_root,bg='grey')
    fc_back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
    fc_back.pack(fill=BOTH, expand=1)

    fc_gui = FactCheckGui(fc_root, truths, cat_names, inp)
    fc_root.mainloop()
   
class ViralGui:
    def __init__(self, master):
        self.master = master
        self.i = 0
        self.secs = 300
        master.title("Viral!")

        #self.titlelabel = Label(master, text="Viral!", font=(None, 50), bg="#486ebf")
        #self.titlelabel.pack(pady=50)

        self.label = Label(master, height=6, text=intro_string)
        self.label.pack(pady=5)

        self.change_button = Button(master, text="Generate Story", height=2, command=self.get_story)
        self.change_button.pack(pady=1)

        self.truth_button = Button(master, text="Generate False Narrative", height=2, command=self.show_false)
        self.truth_button.pack(pady=1)

        self.clear_button = Button(master, text="Clear Display", height=2, command=self.clear_label)
        self.clear_button.pack(pady = 1)

        self.launch_button = Button(master, text="Begin!", height=2, command=self.launch_gui)
        #self.launch_button = Button(master, text="Fact Checking coming soon", command=None)
        self.launch_button.pack(pady=40)

        self.truth_button = Button(master, text="Reveal Truth", height=2, command=self.show_truth)
        self.truth_button.pack(pady=1)

        self.close_button = Button(master, text="Close", height=2, command=self.quit)
        self.close_button.pack(pady=1)

        self.bot_label = Label(master, text="Made by Brian, Greg, Suki, Forrest and Gabbi")
        self.bot_label.pack(pady=1)


    def get_story(self):
        new_text = ""
        for x in cards[self.i]:
            new_text += x + "\n"
        self.set_label(new_text)
        self.i += 1

    def set_label(self, new_text):
        self.label.config(text="                                              \n                                  " + 
            "                                              \n                                  " + 
            "                                              \n                                  " + 
            "                                              \n                                  ")
        self.master.after(10, lambda : self.actually_set(new_text))

    def actually_set(self, new_text):
        self.label.config(text=new_text)

    def clear_label(self):
        self.set_label("")
        self.master.after(10, lambda : self.set_label(""))

    def show_truth(self):
        new_text = ""
        for x in truths:
            new_text += x + "\n"
        self.set_label(new_text)

    def show_false(self):
        new_text = ""
        for x in lies:
            new_text += random.choice(x) + "\n"
        self.set_label(new_text)
    
    def countdown(self):
        print("hoots")
        timedelta = str(datetime.timedelta(seconds=self.secs))
        self.label.config(text=timedelta + " remaining!")
        self.secs -= 1
        self.master.after(1000, lambda : self.countdown())

    def launch_gui(self):
        self.countdown()
        launch_fact_check()

    def quit(self):
        for i in range(20):
            self.master.quit()

root = Tk()

root.title('The game')
#You can set the geometry attribute to change the root windows size
root.geometry("500x500") #You want the size of the app to be 500x500
root.resizable(0, 0)
back = Frame(master=root,bg="#486ebf")
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=BOTH, expand=1)

root_gui = ViralGui(root)
root.mainloop()



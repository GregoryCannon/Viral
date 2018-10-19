import numpy as np
import random

def getcard(catnames,inp,truths,lies):

    cats = np.random.choice(4,3,replace=False)
    print(cats)
    np.random.shuffle(cats)

    #Pick a truth
    show1 = catnames[cats[0]] + ' = ' + truths[cats[0]]
    #Pick a lie
    show2 = catnames[cats[1]] + ' = ' + np.random.choice(lies[cats[1]])
    #Pick an unknown
    if random.choice([True, False]):
        show3 = catnames[cats[2]] + ' = ' + truths[cats[2]]
    else:
        show3 = catnames[cats[2]] + ' = ' + np.random.choice(lies[cats[2]])
    print("show1", show1)
    print("show2", show2)
    print("show3", show3)
    show = [show1,show2]
    print("show", show)
    np.random.shuffle(show)
    print("ret", show)
    return show
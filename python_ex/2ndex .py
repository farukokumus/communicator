from math import *
import numpy as np

mylist=["Mev", "fako", "husam", "ali"]
mytuple = ("LAle", "ALOO") # this is a tuple which is the same thing unless you cant change value etc it is immutable

def change(sr,pos): #for some functions of lists     extend also concanate 2 diff lists
    mylist.append(sr)
    second_list=mylist.copy
    print("Index of the fako", mylist.index("fako"))
    if not(float(pos) < 0) and float(pos) > len(mylist):
        mylist.insert(int(pos),str(sr))
    elif float(pos) < 0:
        mylist.insert(0,str(sr))
    else:
        return 0

    print(mylist )
    return mylist
    #print(second_list)
def main():
    name=input("What is your name\n")
    pos=input("Inserted pos\n")
    newlist=change(name,pos)
    print(newlist[-1])

if __name__ == main():
    main()


from math import *
import numpy as np

mylist=["Mev", "fako", "husam", "ali"]
mytuple = ("LAle", "ALOO") # this is a tuple which is the same thing unless you cant change value etc it is immutable
myarray=np.array([[0,1,2,3],[1,2,3,4]], dtype=np.float32)

def change():
    print(myarray.shape) 
    for friend in mylist:
        print(friend)
    for index in range(len(mylist)):
        print(mylist[index][0])
    for index, friend in enumerate(mylist):
        print(index, friend)
    try:  
        for index in range(myarray.shape[1]):
            print(myarray[index][0])
    except: 
        print("Index is wrong")           

def main():
    #name=input("What is your name\n")
    #pos=input("Inserted pos\n")
    change()

if __name__ == main():
    main()


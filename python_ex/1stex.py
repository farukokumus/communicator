from math import *
import numpy as np


def rnd(number):
    
    print(np.random.rand(1,int(number)))
    


def upper(sr,islength):
    print(sr.upper())
    if islength:
        print(len(sr))
        print(str(sr[0])) # convert the string


def main():

    name=input("What is your name\n")
    cal= input ("Enter the max number\n")
    print("Hello world")
    print("My name is " + name)
    upper(name,True)
    rnd(cal)


if __name__ == main():
    main()


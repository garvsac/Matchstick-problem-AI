#Garv Sachdeva
#2015B4A70551P
#State generator and validator file

import math
import random
import turtle
import random

#helper function
def generatehelper( cell ):
    arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    T = [[21,25],[25,29],[29,33],[33,37]]
    for x in range(16):
        if cell[x] == 1:
            arr[x]=1
            arr[x+4]=1
            p = x%4
            r = int(x/4)
            arr[T[p][0]-1+r]=1
            arr[T[p][1]-1+r]=1
    return arr

#random state generator
def initial_state_generator1(percentage,cell):
    size=4
    factor = percentage/100
    if(percentage>100):
        factor = 1
    total_cells = 16
    required = int(16*factor)
    for x in range(required):
      k = random.randint(1,101)
      while( cell[k%16] == 1):
        k=k+1
      cell[k%16] = 1
    return generatehelper(cell)

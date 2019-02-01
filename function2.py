#Garv Sachdeva
#2015B4A70551P
#BFS DFS and other helper functions

import math
import queue
from generate2 import *


def pathcost(cell1,cell2):
    arr1 = generatehelper( cell1 )
    arr2 = generatehelper( cell2 )
    sum1 = sum(arr1,40)
    sum2 = sum(arr2,40)
    return abs(sum1 - sum2)

def currcell(cell):
    return sum(cell)

def nextState(cell,i):
    nextcell = cell.copy()
    nextcell[i]=0;
    return nextcell

def bfs(cell, targetcells):
        Q = queue.Queue()
        #Q.put(cell)
        curr = cell
        while ( currcell(curr)>=targetcells):
            #comment the next two lines to generate all possible states
            if(currcell(curr)==targetcells):
                return curr
            #print(curr)
            i=0
            while i < len(curr):
                if(curr[i]==1):
                    nextSt = nextState(curr,i)
                    Q.put(nextSt)
                i=i+1
                #pushnextstate
            #curr = Q.get()
            curr = Q.get()
            print("next")

        return curr

def dfs(cell, targetcells):
        Q = queue.LifoQueue()
        #Q.put(cell)
        curr = cell
        while ( currcell(curr)>=targetcells):
            if(currcell(curr)==targetcells):
                return curr
            #print(curr)
            i=0
            while i < len(curr):
                if(curr[i]==1):
                    nextSt = nextState(curr,i)
                    Q.put(nextSt)
                i=i+1
                #pushnextstate
            #curr = Q.get()
            curr = Q.get()
        return curr


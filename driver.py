#Garv Sachdeva
#2015B4A70551P
#Driver file

import math
from function2 import *
from generate2 import * 
from GUI2 import *
import turtle

size=4
#% of squares randomly generated
percentage = 70
#no of Squares in final state
final = 6
#arr = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
#cell = [0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0]

cell = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
arr=initial_state_generator1(percentage,cell)

#uncomment for checking bfs
#ans=bfs(cell,final)

#dfs solution is faster in this case
ans=dfs(cell,final)

path = generatehelper( ans )
#print(path)
#draws the randomly generated configuration
draw(turtle.Turtle(),arr, "white")
for i in range(40):
	if(arr[i]==1 and path[i]==0):
		path[i]=1
	else:
		path[i]=0

#comment this line if turtle hangs
input("Press Enter to continue...")


#deletes the edges not present in the final configuration
#does not delete in the correct sequence
drawdel(turtle.Turtle(),path, "black" , pathcost(cell,ans),currcell(cell))

print("Click on turtle window to exit")
turtle.Turtle().screen.exitonclick()




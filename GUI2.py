#Garv Sachdeva
#2015B4A70551P
#GUI file

import turtle
turtle.bgcolor("black")

size = 4
def draw( gu , arr , color):
    s=size
    gu.color("cyan")
    gu.penup()
    gu.goto (-200, 300)
    gu.pendown()
    gu.write("ID: 2015B4A70551P | AI Project-I",align="left",font=("Freestyle Script",30,"normal"))
    gu.speed(15)
    gu.color(color)
    start_pos=(-150,150)
    gu.penup()
    gu.setx(start_pos[0])
    gu.sety(start_pos[1])
    gu.dot()
    gu.pendown()
    for j in range(s+1):
        for i in range(s):
            if(arr[j*s+i] is 1):
                gu.forward(80)
                gu.dot()
            else:
                gu.penup()
                gu.dot()
                gu.forward(80)
                gu.dot()
                gu.pendown()
        gu.penup()
        gu.setx(start_pos[0])
        gu.sety(start_pos[1]-80*(j+1))
        gu.pendown()
    gu.penup()
    gu.setx(start_pos[0])
    gu.sety(start_pos[1])
    gu.pendown()
    gu.right(90)
    for j in range(0,s+1):

        for i in range(s):
            if(arr[(j+s+1)*s+i] is 1):
                gu.dot()
                gu.forward(80)
                gu.dot()
            else:
                gu.penup()
                gu.dot()
                gu.forward(80)
                gu.dot()
                gu.pendown()
        gu.penup()
        gu.setx(start_pos[0]+80*(j+1))
        gu.sety(start_pos[1])
        gu.pendown()


def drawdel( gu , arr , color, cost ,sq):
    gu.color("cyan")
    gu.penup()
    gu.goto (-45, 180)
    gu.pendown()
    gu.write("Path Cost:" + str(cost),align="left",font=("Freestyle Script",30,"normal"))
    gu.penup()
    gu.goto (-45, -320)
    gu.pendown()
    gu.write("Initial Squares:" + str(sq) ,align="left",font=("Freestyle Script",30,"normal"))
    s=size
    gu.speed(15)
    gu.color(color)
    start_pos=(-150,150)
    gu.penup()
    gu.setx(start_pos[0])
    gu.sety(start_pos[1])
    gu.pendown()
    for j in range(s+1):
        for i in range(s):
            if(arr[j*s+i] is 1):
                gu.forward(80)
            else:
                gu.penup()
                gu.forward(80)
                gu.pendown()
        gu.penup()
        gu.setx(start_pos[0])
        gu.sety(start_pos[1]-80*(j+1))
        gu.pendown()
    gu.penup()
    gu.setx(start_pos[0])
    gu.sety(start_pos[1])
    gu.pendown()
    gu.right(90)
    for j in range(0,s+1):
        for i in range(s):
            if(arr[(j+s+1)*s+i] is 1):
                gu.forward(80)
            else:
                gu.penup()
                gu.forward(80)
                gu.pendown()
        gu.penup()
        gu.setx(start_pos[0]+80*(j+1))
        gu.sety(start_pos[1])
        gu.pendown()
        
    


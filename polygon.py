

import turtle

str= turtle.Turtle()

wn= turtle.Screen()
wn.title("Outside in")
wn.bgcolor("Black")
str.color("white")

def sqrfunc(size):

    for i in range(4):
        str.forward(size)
        str.right(90)
        size+=5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)

from graphics import *
import random

# Do some simple drawing
window = GraphWin("Visualisation", 600, 600)

# Read in and print out the data in the data file
"""with open("data.txt",'r') as x:
    marks = x.readlines()
    marks = [] """
    
marks = [mark.rstrip('\n') for mark in open('data.txt')]
for mark in marks:
    #print "test" + marks[3]
    print mark
    ball = Circle(Point(300,300), float(mark))
    ball.setFill(color_rgb(255,255,0))
    ball.draw(window)
    
    
#all(isinstance(mark, float) for mark in marks)

    
# Function Example    
"""    
if(isTwoOne(mark,ball,window)):
    fsdafjsaflds

def isTwoOne(alpha, beta, gamma)
    return (mark >=50) and (mark <60);
"""



"""ball = Circle(Point(300,300), 300)
ball.setFill(color_rgb(255,255,0))
ball.draw(window)"""

"""
ball2 = Circle(Point(200,500), 60)
ball2.draw(window)

box = Rectangle(Point(200,50),Point(250,150))
box.setOutline(color_rgb(255,0,0))
box.draw(window)

line = Line(Point(200,500),Point(250,280))
line.setWidth(4)
line.draw(window)

text = Text(Point(50,200),"Hello")
text.draw(window)
"""
# Waits until the mouse is clicked before closing the window
window.getMouse()
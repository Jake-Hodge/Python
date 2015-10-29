from graphics import *
import random

# Do some simple drawing
window = GraphWin("Visualisation", 800, 800)

# Read in and print out the data in the data file
"""with open("data.txt",'r') as x:
    marks = x.readlines()
    marks = [] """
    
marks = [mark.rstrip('\n') for mark in open('data.txt')]
for mark in marks:
    print mark
    x = random.randint(100, 700)
    y = random.randint(100, 700)
    ball = Circle(Point(x,y), float(mark))
    colour1 = random.randint(0,255)
    colour2 = random.randint(0,255)
    colour3 = random.randint(0,255)
    ball.setFill(color_rgb(colour1,colour2,colour3))
    ball.draw(window)
    
    
    xspeedvar = 3
    yspeedvar = 3
    while True: #true is always true, loop 4eva
        currentPos = ball.getCenter()
        if(currentPos.getY() >= 800): yspeedvar = -yspeedvar
        if(currentPos.getY() <= 0): yspeedvar = -yspeedvar
        if(currentPos.getX() >= 800): xspeedvar = -xspeedvar
        if(currentPos.getX() <= 0): xspeedvar = -xspeedvar
        ball.move(xspeedvar, yspeedvar) #move by not move to    
   
    # Waits until the mouse is clicked before closing the window
window.getMouse()

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

from graphics import *

window = GraphWin("whatevs", 800, 800)

ball = Circle(Point(100,100), 50)
ball.setFill(color_rgb(255,255,0))
ball.draw(window)

xspeedvar = 1
yspeedvar = 1
    
while True: #true is always true, loop 4eva
        currentpos = ball.getCenter()
        
        if(currentPos.getY() >= 800): yspeedvar = -yspeedvar
        if(currentPos.getY() <= 0): yspeedvar = -yspeedvar
        if(currentPos.getX() >= 800): xspeedvar = -xspeedvar
        if(currentPos.getX() <= 0): xspeedvar = -xspeedvar
        ball.move(xspeedvar, yspeedvar) #move by not move to    
    


window.getMouse()




#array for more balls
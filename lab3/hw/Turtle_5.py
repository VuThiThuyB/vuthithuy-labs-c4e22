from turtle import *

def draw_star(x,y,length):
    
    goto(x, y)  #move the turtle to a location

    for i in range(5):
        forward(length)
        right(144)
    mainloop()
        
draw_star(0,0,100)


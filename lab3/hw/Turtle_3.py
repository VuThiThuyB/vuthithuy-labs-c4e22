from turtle import *
def draw_square(length,colors):
    for i in range(4):
        color(colors)
        forward(length)
        left(90)
    mainloop()
        
        
draw_square(100,"red")
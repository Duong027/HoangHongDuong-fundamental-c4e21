from turtle import *
def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    left(72)
    for i in range (5):
        forward(length)
        right(144)

mainloop()

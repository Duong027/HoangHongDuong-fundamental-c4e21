import turtle

screen = turtle.Screen() # create screen

duong = turtle.Turtle() # create a turtle assign it to duong

for num in range(3): # loop 3 times

    duong.forward(100)
    duong.left(120)
    duong.color("blue")
    
for num in range(4): # loop 4 times

    duong.forward(100)
    duong.left(90)
    duong.color("red")
    
for num in range(5): # loop 5 times

    duong.forward(100)
    duong.left(72)
    duong.color("blue")
 
    
for num in range(6): # loop 6 times

    duong.forward(100)
    duong.left(60)
    duong.color("red")   
    
screen.mainloop()

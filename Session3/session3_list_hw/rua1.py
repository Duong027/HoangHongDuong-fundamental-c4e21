import turtle

screen = turtle.Screen() # create screen

duong = turtle.Turtle() # create a turtle assign it to duong

colors = ['red','blue', 'brown', 'yellow', 'grey']

for i in range(0,5):
    for num in range(i+3): 
        
        duong.forward(100)
        duong.left(360/(i+3))
        duong.color([colors[i]])    

screen.mainloop()
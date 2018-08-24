import turtle

screen = turtle.Screen() # create screen

duong = turtle.Turtle() # create a turtle assign it to duong

colors = ['blue', 'brown', 'yellow', 'grey']

duong.color('red','red')
duong.begin_fill()
for i in range(4):
    duong.forward(50)
    duong.left(90)
duong.end_fill()

for j in range(len(colors)):

    duong.color(colors[j],colors[j])
    duong.begin_fill()
    duong.forward(100)
    duong.left(90)
    for t in range(3):
        duong.forward(50)
        duong.left(90)
    duong.end_fill()
    
screen.mainloop()
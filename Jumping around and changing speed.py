import turtle 

ninja = turtle.Turtle()

ninja.speed(120)

for i in range(500):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()

# Jumping around and changing speed made by Gautam 

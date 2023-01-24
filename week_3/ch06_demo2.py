# Topic : turtle , random Modules
# DEMO

import turtle as turtle
import random as random

# turtle.speed(1)
# turtle.color(0, 0, 1)
# turtle.forward(50) # 50 pixels
# # turtle.color(1, 0, 0)
# # turtle.right(90)
# # turtle.forward(100)
# turtle.done()

turtle.shape("turtle")
turtle.speed(10)
turtle.up()

def drawCircle(x, y):
    # Draw a circle there , and fill it with a random color .
    turtle.fillcolor(random.random(), random.random(), random.random())
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.up()

turtle.title ("Click on the canvas !")

# bind left mouse button to drawCircle function
turtle.onscreenclick(drawCircle)

# Initiate main loop
turtle.mainloop()


# spaceship game
# http://www.codeskulptor.org/#user43_7zb1ohzfMl_35.py

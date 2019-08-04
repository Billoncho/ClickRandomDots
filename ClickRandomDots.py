# ClickRandomDots.py
# Billy Ridgeway
# Creates random sized and colored polka dots on the screen where the user clicks.

import random                   # Imports the random library.
import turtle                   # Imports the turtle library.
t = turtle.Turtle()             # Creats a new pen called t.
t.speed(0)                      # Sets the pen's speed to fast.
t.hideturtle()                  # Hides the pen.
t.getscreen().bgcolor('black')  # Sets the background color to black.

def drawPolkaDot(x,y):                  # Defines the function to draw polka dots.
    size = random.randint(3,70)         # Randomly sets the size between 3 and 50.
    t.penup()                           # Stops the pen from drawing.
    t.setpos(x, y - size)               # Sets the pen's x y location.
    t.pendown()                         # Sets the pen to draw.
    
    # Randomly selects the polka dots fill color from r, g, b.
    t.fillcolor((random.random(), random.random(), random.random()))
    t.begin_fill()                      # Begins to fill in the polka dot.
    t.circle(size)                      # Sets the size of the polka dot.
    t.end_fill()                        # Ends filling in the polka dot.
turtle.onscreenclick(drawPolkaDot)      # When the screen is clicked call the draw
                                        # polka dot function and draw a polka dot on
                                        # the location of the mouse click.


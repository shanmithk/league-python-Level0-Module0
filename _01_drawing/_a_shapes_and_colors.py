import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
fred = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
fred.shape('turtle')
# Set your turtle's speed using .speed(2)
fred.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
fred.color('purple')
fred.pencolor('blue')
# Move your turtle forward using .forward(100)
for i in range(4):
    fred.forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
    fred.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
fred.goto(100, 40)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
fred.begin_fill()
fred.circle(36, steps=30)
fred.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!
fred.color('purple')
fred.penup()
fred.goto(100, 100)
fred.pendown()
for i in range(8):
    fred.forward(100)
    fred.left(45)
fred.color('black')
for i in range(12):
    fred.forward(100)
    fred.right(30)
fred.color('pink')
for i in range(6):
    fred.forward(100)
    fred.left(60)
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()

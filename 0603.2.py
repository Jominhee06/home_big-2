import turtle
import threading
import random

# Function for each turtle to draw a square with an additional parameter
def draw_square(t, x, y, size, color):
    for _ in range(4):
        t.forward(size)
        t.right(90)
    return
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    t.hideturtle()

# Function to start drawing for a turtle
def start_timer(t, x, y, size, color):
    timer = threading.Timer(0, lambda: draw_square(t, x, y, size, color))
    timer.start()

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create 9 turtles
turtles = []
colors = ["red", "blue", "green", "yellow", "purple", "orange", "black", "pink", "brown"]
size = 200
for i in range(3):
    for j in range(3):
        t = turtle.Turtle()
        t.color(colors[i])
        t.penup()
        t.goto(i * 20 - 80, 0)  # Position turtles so they don't overlap
        t.pendown()
        turtles.append(t)
        color = random.choice(colors)
        x = -300 + j * (size + 10)
        y = 300 - i * (size + 10)
        start_timer(t, x, y, size, color)  # Passing size 50 as an additional parameter

# Keep the window open until it is closed by the user
screen.mainloop()


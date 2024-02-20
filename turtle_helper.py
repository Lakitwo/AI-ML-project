# turtle_helper.py

import turtle
import time

initial_x = -170
initial_y = -170

def move_turtle(command):
    delay = 0.5
    step_size = 100

    if command == 'left':
        t.left(90)
        time.sleep(delay)
    elif command == 'right':
        t.right(90)
        time.sleep(delay)
    elif command == 'go':
        t.forward(step_size)
        time.sleep(delay)
    elif command == 'stop':
        print('Stopping the turtle')

def setup_turtle(tk_canvas):
    global t

    # Create a RawTurtle using the provided Tkinter Canvas
    t = turtle.RawTurtle(tk_canvas)
    t.turtlesize(2)
    # Set initial properties
    t.pensize(5)
    t.pencolor("blue")
    t.penup()  # Lift the pen to move without drawing a line
    t.goto(initial_x, initial_y)
    t.pendown()  # Put the pen down to start drawing

def reset_turtle():
    t.clear()
    t.penup()
    t.goto(initial_x, initial_y)
    t.setheading(0)
    t.pendown()
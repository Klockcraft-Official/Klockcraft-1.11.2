import turtle
import threading
import pyautogui
import keyboard

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LINE_LENGTH = 20  # Length of each line segment
LINE_WIDTH = 1  # Width of each line segment
LINE_COLOR = "black"
INVENTORY = []
ON_INVENTORY_SLOT = 1
HEALTH = 100
HUNGER = 100
XP = 0
MOUSE_X = 0
MOUSE_Y = 0

# Initialize screen
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.cv._rootwindow.config(cursor="none")
screen.title("Minecraft")

screen.tracer(0)  # Disable screen updates

crosshair_turtle = turtle.Turtle()
inventory_slot_turtle = turtle.Turtle()

crosshair_turtle.speed(0)
crosshair_turtle.hideturtle()

inventory_slot_turtle.speed(0)
inventory_slot_turtle.hideturtle()

def track_mouse():
    global MOUSE_X, MOUSE_Y
    while True:
        MOUSE_X, MOUSE_Y = pyautogui.position()
        # print('Mouse position:', MOUSE_X, MOUSE_Y)

# Function to draw the crosshair
def draw_crosshair():
    # Horizontal line
    crosshair_turtle.penup()
    crosshair_turtle.goto(-LINE_LENGTH / 2, 0)
    crosshair_turtle.pendown()
    crosshair_turtle.color(LINE_COLOR)
    crosshair_turtle.width(LINE_WIDTH)
    crosshair_turtle.forward(LINE_LENGTH)
    crosshair_turtle.penup()

    # Vertical line
    crosshair_turtle.goto(0, -LINE_LENGTH / 2)
    crosshair_turtle.setheading(90)
    crosshair_turtle.pendown()
    crosshair_turtle.forward(LINE_LENGTH)
    crosshair_turtle.penup()

def draw_inventory_slots():
    # Calculate the starting position for the inventory slots
    start_x = -SCREEN_WIDTH / 2 + (SCREEN_WIDTH - (50 * 9)) / 2
    start_y = -SCREEN_HEIGHT / 2 + 25

    # Draw the inventory slots
    for i in range(9):
        inventory_slot_turtle.penup()
        inventory_slot_turtle.goto(start_x + 50 * i, start_y)
        inventory_slot_turtle.pendown()
        inventory_slot_turtle.setheading(0)
        inventory_slot_turtle.forward(50)
        inventory_slot_turtle.setheading(90)
        inventory_slot_turtle.forward(50)
        inventory_slot_turtle.setheading(180)
        inventory_slot_turtle.forward(50)
        inventory_slot_turtle.setheading(270)
        inventory_slot_turtle.forward(50)
        inventory_slot_turtle.penup()

mouse_track_thread = threading.Thread(target=track_mouse)
mouse_track_thread.daemon = True
mouse_track_thread.start()

# Crosshair turtle
turtle.speed(0)  # Set fastest animation speed
turtle.hideturtle()

# Draw initial crosshair
draw_crosshair()

# Draw inventory slots
draw_inventory_slots()

# Main loop
turtle.mainloop()

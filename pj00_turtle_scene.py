"""PJ00!

Kailash Muthu
9/14/2020
UNC Chapel Hill
COMP110 - Prof. Kris Jordan

PJ00 - Turtle Scene Project

The following project uses the Turtle class and creates turtle objects to draw an art natural landscape art piece.

ADDITIONAL 15 POINTS REQUIREMENT FULLFILLED

[1] Avoid Complex Functions: CHECK LN255-268; LN266; LN271-287; LN290-320; LN301; LN150-179
[2] Attempting Newly:
                - Screen Object: CHECK LN75-78; LN59 (Remove '#' to work)
                - Randint(): CHECK LN167; LN259; LN301
                - Turtle Module Method Implementations
                    - turtle.circle(): CHECK LN249
                    - turtle.stamp(): CHECK LN195
                    - turtle.shape(): CHECK LN193; LN201
                    - turtle.shapesize(): CHECK LN194
                - Using "%" Modulus Div to make decisons: CHECK LN83, LN91, LN172, LN318
                - Nested While Loops: CHECK LN81, LN275, LN299


HAVE AN EPIC DAY 
-----------------------------
( ͡° ͜ʖ ͡°)                 ಠ_ಠ 
-----------------------------

"""


from turtle import Turtle, colormode, done, tracer, update   # , Screen
from random import randint
__author__ = "730411609"

RBG_VALUE: int = 255


def main() -> None:
    """The entrypoint of my lanscape art. Point of start!"""
    paint_brush: Turtle = Turtle()
    
    # max_screen()
    tracer(0, 0)
    create_canvas(paint_brush, 850, 450, "black", 50, 1)
    create_ground(paint_brush, -800, -100, 34, 223, 120, 1)
    create_sky(paint_brush, -800, 400, 57, 185, 241, 1)
    grow_grass(paint_brush)
    create_sun(paint_brush, -600, 250, 230, 211, 28, 10)
    create_lake(paint_brush, 0, -250, 13, 141, 214, 10)
    create_mountains(paint_brush, -800, 100, 140, 134, 134, 1)
    create_forest(paint_brush, -600, 0, 10, 64, 25, 1)

    update()

    done()


# def max_screen() -> None:
#    """Creates a screen object and uses the setup method to maximize the screen."""
#    screen: Screen = Screen()  # Creates a screen object
#    screen.setup(1.0, 1.0)  # maximizes the TurtleScreen


def create_canvas(brush: Turtle, x: float, y: float, border_color: str, border_size: int, brush_size: int) -> None:
    """Creates a canvas space."""
    brush.penup()
    brush.pensize(brush_size)
    brush.goto(x, y)
    brush.setheading(270)
    brush.fillcolor(border_color)

    i: int = 0 
    j: int = 0

    brush.begin_fill()

    while(i < 2):  # nested while-loop 

        if(i % 2 != 0):
            x -= border_size
            y -= border_size
            brush.goto(x, y)

        brush.pendown()

        while(j < 4):
            if(j % 2 == 0):
                brush.forward(y * 2)
            else:
                brush.forward(x * 2)
            brush.right(90)
            j += 1

        j = 0
        i += 1
        brush.penup()

    brush.end_fill()


def create_ground(brush: Turtle, x: float, y: float, r: int, g: int, b: int, brush_size: int) -> None:
    """Creates the ground of the canvas art."""
    brush.goto(x, y)
    brush.setheading(0)
    colormode(RBG_VALUE)
    brush.pensize(brush_size)
    brush.pencolor(r, g, b)
    brush.fillcolor(r, g, b)
    brush.pendown()

    brush.begin_fill()
    i: int = 0
    while(i < 2):
        brush.forward(abs(x) * 2)
        brush.right(90)
        brush.forward(300)
        brush.right(90)
        i += 1
    brush.end_fill()

    brush.penup()


def create_sky(brush: Turtle, x: float, y: float, r: int, g: int, b: int, brush_size: int) -> None:
    """Creates the sky of the canvas art."""
    brush.goto(x, y)
    brush.setheading(0)
    colormode(RBG_VALUE)
    brush.pensize(brush_size)
    brush.pencolor(r, g, b)
    brush.fillcolor(r, g, b)
    brush.pendown()

    brush.begin_fill()
    i: int = 0
    while(i < 2):
        brush.forward(abs(x) * 2)
        brush.right(90)
        brush.forward(500)
        brush.right(90)
        i += 1
    brush.end_fill()
    brush.penup()


def create_grass(brush: Turtle, x: float, y: float, r: int, g: int, b: int, brush_size: int) -> None:
    """Creates the grass of the canvas art of random sizes."""
    brush.goto(x, y)
    colormode(RBG_VALUE)
    brush.pensize(brush_size)
    brush.pencolor(r, g, b)
    brush.fillcolor(r, g, b)
    brush.pendown()

    i: int = 0
    grass_length: int = 0
    length_range_x: int = 5
    length_range_y: int = 15

    while(i < 3):

        brush.setheading(45)
        grass_length = randint(length_range_x, length_range_y)  # ranodmness in grass length
        brush.forward(grass_length)
        brush.setheading(315)
        brush.forward(grass_length)
        i += 1
        if(i % 2 != 0):
            length_range_x = 20
            length_range_y = 35
        else:
            length_range_x = 5
            length_range_y = 15

    brush.penup()


def create_lake(brush: Turtle, x: float, y: float, r: int, g: int, b: int, brush_size: int) -> None:
    """Creates a lake using by changing the shape of the turtle and stamping itself and reverts back."""
    brush.goto(x, y)
    brush.setheading(0)
    colormode(RBG_VALUE)
    brush.pensize(brush_size)
    brush.pencolor(r, g, b)
    brush.fillcolor(r, g, b)
    brush.pendown()

    brush.begin_fill()
    brush.shape("circle")
    brush.shapesize(10, 35)
    brush.stamp()

    brush.end_fill()

    brush.penup()

    brush.shape("classic")
    brush.shapesize(1, 1)


def create_mountains(brush: Turtle, x: float, y: float, r: int, g: int, b: int, brush_size: int) -> None:
    """Create a mountain landscape that changes in hue after every increase in layer."""
    brush.goto(x, y)
    brush.setheading(0)
    colormode(RBG_VALUE)
    brush.pensize(brush_size)

    mountain_peak_y: int = 300
    mountain_start_x: int = int(x)
    mountain_start_y: int = int(y)
    i: int = 0

    while(i < 3):
        brush.begin_fill()
        brush.pencolor(r, g, b)
        brush.fillcolor(r, g, b)
        brush.pendown()
        brush.goto(mountain_start_x, mountain_start_y)
        brush.goto(0, mountain_peak_y)
        brush.goto(abs(mountain_start_x), mountain_start_y)
        brush.goto(800, -100)
        brush.goto(-800, -100)
        brush.penup()
        i += 1
        mountain_peak_y -= 100
        mountain_start_y -= 100 
        r -= 5
        g -= 10
        b -= 10
        brush.end_fill()


def create_sun(brush: Turtle, x: float, y: float, r: int, g: int, b: int, brush_size: int) -> None:
    """Uses the circle method of the turtle object to create a circle."""
    brush.goto(x, y)
    brush.setheading(0)
    colormode(RBG_VALUE)
    brush.pensize(brush_size)
    brush.pencolor(r, g, b)
    brush.fillcolor(r, g, b)
    brush.pendown()

    brush.begin_fill()

    brush.circle(50)

    brush.end_fill()
    brush.penup()


def create_forest(brush: Turtle, x: float, y: float, r: int, g: int, b: int, brush_size: int) -> None:
    """Develops a forrest of 50 tress that are randomly located each time, by calling on the create_tree function."""
    i: int = 0
    while(i < 50):
        brush.goto(randint(-750, 750), y)
        brush.setheading(90)
        colormode(RBG_VALUE)
        brush.pensize(brush_size)
        brush.pencolor(r, g, b)
        brush.fillcolor(r, g, b)
        brush.pendown()
        create_tree(brush)    # calls create_tree procedure to create a tree
        brush.penup()
        i += 1


def create_tree(brush: Turtle) -> None:
    """Creates a standard tree on the canvas."""
    j: int = 0
    size: int = 50
    while(j < 3):
        brush.setheading(60)
        i: int = 0
        brush.begin_fill()
        while(i < 3):
            brush.right(120)
            brush.forward(size)
            i += 1
        brush.end_fill()
        brush.setheading(90)
        brush.backward(size * 0.5)
        size += 10
        j += 1


def grow_grass(brush: Turtle) -> None:
    """Grows the grass at random locations in the map."""
    i: int = 0
    j: int = 0
    x_left: int = -750
    x_right: int = -650
    y_left: int = -200
    y_right: int = -150

    while(i < 2):
        while(j < 4):
            create_grass(brush, randint(x_left, x_right), randint(y_left, y_right), 19, 124, 17, 10)
            j += 1
            if(j == 1):
                x_left += 200
                x_right += 200
            elif(j == 2):
                x_left = 650  # abs(x_right - 200)
                x_right = 700  # abs(x_left - 200)
            elif(j == 3):
                x_left -= 200
                x_right -= 150

        i += 1
        j = 0
        x_left = -750
        x_right = -650

        if(i % 2 != 0):
            y_left -= 150
            y_right -= 150


# Python Idiom (Convention) for a runnable Python module

if __name__ == "__main__":
    main()

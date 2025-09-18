from turtle import *

### write all new functions here ###

def draw_circle(turtle, radius, color):
    """Helper function to draw a filled circle."""
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_emoji(turtle):
    """
    Draw a simple smiley emoji.
    """
    # Draw face
    turtle.penup()
    turtle.goto(0, -100)  # Move so circle is centered
    turtle.pendown()
    draw_circle(turtle, 100, "#997950")

    # Draw left eye
    turtle.penup()
    turtle.goto(-35, 20)
    turtle.pendown()
    draw_circle(turtle, 15, "black")

    # Draw right eye
    turtle.penup()
    turtle.goto(35, 20)
    turtle.pendown()
    draw_circle(turtle, 15, "black")

    # Draw smile
    turtle.penup()
    turtle.goto(-40, -20)
    turtle.setheading(-60)  # Angle for smile arc
    turtle.width(10)
    turtle.pendown()
    turtle.circle(50, 120)  # Draw part of a circle (arc) for smile
    
    # Draw right eye
    turtle.penup()
    turtle.goto(20, 0)
    turtle.pendown()
    draw_circle(turtle, 15, "black")
    
     # Left ear
    turtle.penup()
    turtle.goto(-70, 120)
    turtle.pendown()
    draw_circle(turtle, 40, "brown")

 # Teeth (two rectangles)
    turtle.penup()
    turtle.goto(-15, -55)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(5, -55)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()



def main():
    """
    Create a screen, a turtle, and call draw_emoji.
    """
    screen = Screen()
    screen.bgcolor("lightblue")
    t = Turtle()
    t.speed(10)

    draw_emoji(t)

    screen.exitonclick()


if __name__ == '__main__':
    main()




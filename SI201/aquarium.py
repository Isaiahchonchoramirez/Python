# Your name: Isaiah R.
# Your student id: 31550177
# Your email: izzyrmrz@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Claude
# If you worked with generative AI also add a statement for how you used it.
# e.g.: See bottom description for details on how generative AI was used.
# Asked genAI hints for debugging and suggesting the general structure of the code
#Claude (Claude Sonnet 4). "Code Optimization and Structure Assistance for Python Turtle Graphics Project." Anthropic AI Assistant, Anthropic, 12 Sept. 2025, claude.ai.
#In-Text Citation Example:
#According to Claude, the code was tightened by "removing all commented-out code, consolidating redundant pen movements, using loops for repetitive code, removing unnecessary blank lines, and improving comments to be more concise and meaningful" (Claude).

from turtle import *
import random

### write all new functions here ###

def draw_aquarium(turtle, radius, color):
    """Helper function to draw a filled circle."""
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_egg(turtle, width, height, color):
    """Draw an egg-like oval using two big arcs (top) and two small arcs (bottom)."""
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(45)            # tilt for symmetry
    turtle.circle(height, 90)  # top arc (bigger)
    turtle.circle(width, 90)   # bottom arc (smaller)
    turtle.circle(height, 90)  # top arc again
    turtle.circle(width, 90)   # bottom arc again
    turtle.end_fill()
    turtle.right(45)  # reset tilt so later parts draw normally
    

    
def draw_oval(t, radius, stretch, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, 90)
        t.circle(radius*stretch, 90)
    t.end_fill()

def draw_i(turtle, x, y):
    """Draw the letter 'I' at specified position."""
    turtle.penup()
    turtle.goto(100, y)
    turtle.pendown()
    turtle.pensize(10)
    turtle.color("blue")
    
    # Draw the vertical line
    turtle.setheading(90)  # Pointing upwards
    turtle.forward(45)    # Draw the vertical line
    
    # Draw the top horizontal line
    turtle.right(90)      # Turn right to draw horizontal line
    turtle.forward(25)    # Draw top horizontal line
    turtle.backward(50)  # Draw back to the center and continue to the left side
    
    # Draw the bottom horizontal line
    turtle.penup()
    turtle.goto(x, y)     # Go back to the bottom of the vertical line
    turtle.pendown()
    turtle.setheading(0)  # Face right
    turtle.forward(25)    # Draw bottom horizontal line
    turtle.backward(50)  # Draw back to the center and continue to the left side

def draw_r(turtle, x, y):
    """Draw the letter 'I' at specified position."""
    turtle.penup()
    turtle.goto(175, y)
    turtle.pendown()
    turtle.pensize(10)
    turtle.color("blue")
    
    # Draw the vertical line
    turtle.setheading(90)  # Pointing upwards
    turtle.forward(45)    # Draw the vertical line
    
    # Draw the top horizontal line
    turtle.right(90)      # Turn right to draw horizontal line
    turtle.forward(25)    # Draw top horizontal line
    turtle.right(90)      # Turn right to draw the diagonal line
    turtle.forward(25)    # Draw the diagonal line
    turtle.right(90)      # Turn right to draw the diagonal line
    turtle.forward(25)    # Draw the diagonal line
    turtle.left(145)
    turtle.forward(35)
    
    # Draw the bottom horizontal line
    turtle.penup()
    turtle.goto(x, y)     # Go back to the bottom of the vertical line
    turtle.pendown()
    turtle.setheading(0)  # Face right
    turtle.forward(25)    # Draw bottom horizontal line
    turtle.backward(50)  # Draw back to the center and continue to the left side


def draw_emoji(turtle):
    """Draw a simple smiley emoji."""
    turtle.speed(0)
    
    
    
    # Draw bubbles
    num_bubbles = 50 # Number of bubbles to draw
    bubble_color = "#e7feff" # Light blue color for bubbles
    x_min, x_max = -280, 280  # Horizontal range for bubbles (screen boundaries)
    y_min, y_max = -180, 180  # Vertical range for bubbles
    
    turtle.penup() # Start with pen up to move without drawing lines all over
    for _ in range(num_bubbles): # Draw multiple bubbles (50 in this case)
        radius = random.randint(1, 10) # Random radius between 1 and 10 units any bigger the bubbles looked off.
        x = random.randint(x_min, x_max) # Starting with random x position within screen  max width
        y = random.randint(y_min, y_max) # Random y position within screen max height
        turtle.goto(x, y) # Call to x,y to move turtle to random position
        turtle.pendown() # Put pen down to start drawing
        draw_aquarium(turtle, radius, bubble_color) # Call to draw bubble at random position with random radius(1-10)
        turtle.penup() # Pen up again to move to next random position without drawing lines in between them all.
        
    # Rear Fins
    turtle.goto(-125, -110)
    turtle.setheading(55)
    turtle.pendown()
    draw_oval(turtle, 8, 6, "#94e276")  # Left fin
    
    turtle.penup()
    turtle.goto(-20, -110)
    turtle.setheading(-140)
    turtle.pendown()
    draw_oval(turtle, 8, 6, "#94e276")  # Right fin

    # Rear Fin Shades
    turtle.penup()
    turtle.goto(-125, -110)
    turtle.setheading(55)
    turtle.pendown()
    draw_oval(turtle, 6, 4, "#589920")  # Left shade
    
    turtle.penup()
    turtle.goto(-20, -110)
    turtle.setheading(-140)
    turtle.pendown()
    draw_oval(turtle, 6, 4, "#589920")  # Right shade
    
    # Front Fins
    turtle.penup()
    turtle.goto(-125, -25)
    turtle.setheading(55)
    turtle.pendown()
    draw_oval(turtle, 7, 4, "#94e276")  # Left fin
    
    turtle.penup()
    turtle.goto(-5, -35)
    turtle.setheading(-140)
    turtle.pendown()
    draw_oval(turtle, 7, 4, "#94e276")  # Right fin

    # Front Fin Shades
    turtle.penup()
    turtle.goto(-125, -25)
    turtle.setheading(55)
    turtle.pendown()
    draw_oval(turtle, 5, 3, "#589920")  # Left shade
    
    turtle.penup()
    turtle.goto(0, -35)
    turtle.setheading(-140)
    turtle.pendown()
    draw_oval(turtle, 5, 3, "#589920")  # Right shade
    
    # Draw face
    turtle.penup()
    turtle.goto(75, 15)
    turtle.setheading(30)
    turtle.pendown()
    draw_egg(turtle, 80, 40, "#4cbb17")
    turtle.setheading(0)
    
    # Draw body
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    draw_egg(turtle, 100, 50, "#4cbb17")   # egg body
    
    # Draw belly layers
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    draw_egg(turtle, 100, 5, "white")   # white belly
    
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    draw_egg(turtle, 100, 2, "tan")   # tan belly
  
    # Draw left eye
    turtle.penup()
    turtle.goto(-10, 20)
    turtle.pendown()
    draw_aquarium(turtle, 15, "black")
    draw_aquarium(turtle, 5, "white")

    # Draw right eye
    turtle.penup()
    turtle.goto(50, 20)
    turtle.pendown()
    draw_aquarium(turtle, 15, "black")
    draw_aquarium(turtle, 5, "white")
    
    # Draw smile
    turtle.penup()
    turtle.goto(-10, 0)
    turtle.setheading(-60)
    turtle.width(5)
    turtle.pendown()
    turtle.circle(25, 100)  # smile arc
    
    
    #
    draw_i(turtle, 100, -150)
    draw_r(turtle, 100, -150)
    
    """    
    # Draw feet
    for x_pos, heading in [(-125, -15), (-20, 15)]:
        turtle.penup()
        turtle.goto(x_pos, -110)
        turtle.setheading(heading)
        turtle.pendown()
        turtle.fillcolor("#94e276")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(15)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(90)
        turtle.end_fill()
    
    # Draw feet shades
    for x_pos, heading in [(-125, -15), (-20, 15)]:
        turtle.penup()
        turtle.goto(x_pos, -110)
        turtle.setheading(heading)
        turtle.pendown()
        turtle.fillcolor("#589920")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(10)
            turtle.right(90)
            turtle.forward(35)
            turtle.right(90)
        turtle.end_fill()
    """
    # Signature
    turtle.penup()
    turtle.goto(150, 150)
    turtle.pendown()
    turtle.write("By Isaiah R.", font=("Arial", 16, "normal"))

    

def main():
    """Create a screen, a turtle, and call draw_emoji."""
    screen = Screen()
    screen.bgcolor("#009dc4")
    screen.setup(width=600, height=400)
    t = Turtle()
    t.speed(10)
    draw_emoji(t)
    screen.exitonclick()

if __name__ == '__main__':
    main()

"""
Claude (Claude Sonnet 4). "Code Optimization and Structure Assistance for Python Turtle Graphics Project." Anthropic AI Assistant, Anthropic, 12 Sept. 2025, claude.ai.
In-Text Citation Example:
According to Claude, the code was tightened by "removing all commented-out code, consolidating redundant pen movements, using loops for repetitive code, removing unnecessary blank lines, and improving comments to be more concise and meaningful" (Claude).
"""
import turtle
def draw_border(length,height):
    turtle.penup()
    turtle.goto(length/2,-height/2)
    turtle.pendown()
    turtle.goto(length/2,height/2)
    turtle.goto(-length/2,height/2)
    turtle.goto(-length/2,-height/2)
    turtle.goto(length/2,-height/2)
    turtle.hideturtle()
    

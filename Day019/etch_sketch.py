from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("normal")
screen = Screen()


def move_forwards():
    timmy.fd(10)


def move_backwards():
    timmy.bk(10)
    
    
def move_counter_clockwise():
    global angle
    timmy.setheading(angle)
    angle -= 10
    
def move_clockwise():
    global angle
    timmy.setheading(angle)
    angle += 10
    
def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    
    
global angle
angle = 0

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_counter_clockwise)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
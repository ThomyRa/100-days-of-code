from turtle import Turtle, Screen
import turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")


my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

my_screen.screensize(400, 400)
print(f"The size of the screen is: {my_screen.screensize()}")
timmy.down()
timmy.fd(100)

my_screen.exitonclick()



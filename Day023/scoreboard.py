from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def increase_lvl(self):
        self.lvl += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
        
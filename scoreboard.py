from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("white")
        self.penup()
        self.goto(-240, 250)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"level:{self.level}",align="center",font=FONT)

    def increase_level(self):
        self.level+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.write("GAME OVER",align="center",font=FONT)



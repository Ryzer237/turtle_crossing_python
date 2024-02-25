from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.left(90)
        self.go_back()
        self.y_position=-280
    def  up(self):
        self.forward(MOVE_DISTANCE)

    def check_finsih(self):
        if self.ycor()>280:
            return True
        else:
            return False
    def go_back(self):
        self.goto(STARTING_POSITION)

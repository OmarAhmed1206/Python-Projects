from turtle import Turtle
MOVE_DISTANCE = 20
FINAL_DISTANCE = 280
TURTLE_START = [0,-330]
class Body(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(0,-330)
        self.x_lines = 390
        self.y_lines=-310

    def lines(self):
        self.shape("circle")
        self.setheading(180)
        self.width(2)
        self.hideturtle()
        self.goto(self.x_lines,self.y_lines)
        for _ in range (20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.y_lines += 85
    def go_up(self):
        self.forward(MOVE_DISTANCE)
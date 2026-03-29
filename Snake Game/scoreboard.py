from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("New_Data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self._draw()

    def _draw(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",
                   align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self._draw()

    def reset_stuff(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("New_Data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self._draw()


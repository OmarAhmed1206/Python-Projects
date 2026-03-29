import random
from turtle import Turtle, Screen
screen = Screen()
turtle_colors= ["red", "blue", "green", "purple", "orange", "yellow"]
user_bet = screen.textinput(title="Make Your Bet", prompt= "Which Turtle Will Win The Race? Enter A Color: ")
screen.setup(width=1000, height=600)
screen_width = screen.window_width()
screen_height = screen.window_height()
turtles = []


start_x = -450
start_y = -120
color = 0
for i in range(0,6):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(turtle_colors[i])
    racer.goto(x=start_x, y=start_y)
    turtles.append(racer)
    start_y +=50
print(turtles)
is_race_on = True
finish_line = 480
while is_race_on:
    for turtle in turtles:
        distance = random.randint(1, 10)
        turtle.forward(distance)
        if turtle.xcor() >= finish_line:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet.lower() == winning_color.lower():
                print(f"You've won! The {winning_color} turtle is the winner! 🏁")
            else:
                print(f"You've lost. The {winning_color} turtle won the race. 🐢")







screen.exitonclick()

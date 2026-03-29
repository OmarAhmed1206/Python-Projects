from turtle import Screen
import time
import random
from body import Body, TURTLE_START
from cars import Cars
from scoreboard import ScoreBoard
screen = Screen()
screen.tracer(0)
body = Body()
screen.listen()
screen.onkeypress(body.go_up, "w")
for _ in range(12):
    body.lines()
body.__init__()
scoreboard = ScoreBoard()
screen.bgcolor("#B0B0B0")
screen.setup(width= 800, height= 700)
all_cars = []
game_on = True
spawn_chance = 6
while game_on:
    screen.update()
    time.sleep(0.1)

    for car in all_cars:
        car.car_movement()

    if random.randint(1, spawn_chance-1) == 1:
        new_car = Cars()
        all_cars.append(new_car)

    if body.ycor() >300 :
        spawn_chance -=1
        for car in all_cars:
            car.increase_speed()
        scoreboard.other_side()
        body.goto(TURTLE_START)

    for car in all_cars:
        if body.distance(car) < 30:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
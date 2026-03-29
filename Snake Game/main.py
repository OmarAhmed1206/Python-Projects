from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.tracer(0)

screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Welcome To The Snake Game")
screen.listen()

snake = Snake()
food = Food()
keeping_score = Scoreboard()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.left, "a")
    snake.snake_move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        keeping_score.increase()
    if snake.head.xcor() > 290 or snake.head.xcor() <-300 or snake.head.ycor() >300 or snake.head.ycor() <-300:
        snake.reset()
        keeping_score.reset_stuff()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            snake.reset()
            keeping_score.reset_stuff()
screen.exitonclick()
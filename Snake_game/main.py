from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# setup screen
screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collison with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment()

    # detect collison wtih wall
    if snake.head.xcor() > 305 or snake.head.xcor() < -305 or snake.head.ycor() > 305 or snake.head.ycor() < -305:
        game_is_on = False
        scoreboard.game_over()

    # detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

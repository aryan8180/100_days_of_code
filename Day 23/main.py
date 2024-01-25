import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def go_up():
    user.move()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()  # Start listening for key events
screen.onkey(go_up, "Up")  # Bind the go_up function to the "Up" key

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Check if the player has reached the finish line
    if user.ycor() > 280:
        # Implement logic for reaching the finish line, like increasing the score or resetting the player's position.
        user.goto(0, -280)

    # You can add more game logic and interactions as needed.
    for car in car_manager.all_cars:
        if car.distance(user) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_count = 1

    def create_car( self ):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            car_pos = random.randint(-250,250)
            new_car.goto(x=300,y=car_pos)
            self.all_cars.append(new_car)

    def move_car( self ):
        for car in self.all_cars:
            car.backward(self.car_speed)
            self.car_count += 1

    def level_up( self ):
        self.car_speed += MOVE_INCREMENT

    def number_of_cars( self ):
        pass



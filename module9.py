#module 9

class Car:
    def __init__(self, reg_num, max_speed, current_speed = 0, travel_dist = 0):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travel_dist


    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time):
        self.travelled_distance += self.current_speed * time # (d = vt)
#ex 4
import random
cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

distance_max = 0

while distance_max < 10000:
    for car in cars:
        # Adjust speed randomly between -10 and +15
        car.accelerate(random.randint(-10, 15))
        # Drive for one hour
        car.drive(1)
        distance_max = max(car.travelled_distance, distance_max)

for car in cars:
    print(f"{car.registration_number},: {car.maximum_speed}, {car.current_speed}, {car.travelled_distance}")

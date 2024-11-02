from module9 import Car

class ElectricCar(Car):
    def __init__(self, regPlate, MaxSpeed, Battery_capacity):
        super().__init__(regPlate, MaxSpeed)
        self.Battery_capacity = Battery_capacity

    def print_travelled_distance(self):
        print("Travelled distance: " + str(self.travelled_distance))

class GasolineCar(Car):
    def __init__(self, regPlate, MaxSpeed, tank_capacity):
        super().__init__(regPlate, MaxSpeed)
        self.tank_capacity = tank_capacity

    def print_travelled_distance(self):
        print("Travelled distance: " + str(self.travelled_distance))

electric_car1 = ElectricCar("ABC-15", 180, 60.5)
gas_car1 = GasolineCar("ACD-40", 170, 35)
electric_car1.accelerate(30)
gas_car1.accelerate(100)
electric_car1.drive(3); gas_car1.drive(3)
electric_car1.print_travelled_distance(); gas_car1.print_travelled_distance()



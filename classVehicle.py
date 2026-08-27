class Vehicle:

    def _init_(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
car1 = Vehicle(180, 20)
print(car1.max_speed)
print(car1.mileage)

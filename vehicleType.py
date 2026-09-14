class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print(self.brand, self.max_speed)

class Car(Vehicle):
    def __init__(self, brand, max_speed, model, seats):
        self.model = model
        self.seats = seats
        super().__init__(brand, max_speed)

    def show_details(self):
        print(self.model, self.seats)
        super().show_details()

    def fuel_type(self):
        print("Electric")

my_car = Car("Tesla", 250, "Model S", 5)
my_car.show_details()
my_car.fuel_type()

print(issubclass(Car, Vehicle))

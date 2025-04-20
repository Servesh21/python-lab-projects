
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
    
    def display_car_info(self):
        self.display_info()
        print(f"Fuel Type: {self.fuel_type}")


class ElectricCar(Car):
    def __init__(self, brand, model, fuel_type, battery_capacity):
        super().__init__(brand, model, fuel_type)
        self.battery_capacity = battery_capacity
    
    def display_electric_car_info(self):
        self.display_car_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


electric_car = ElectricCar("Tesla", "Model S", "Electric", 100)
electric_car.display_electric_car_info()




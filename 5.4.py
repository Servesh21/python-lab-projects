
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
    
class Car:
    def __init__(self, make, model, year, color, engine_type, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_type = engine_type
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Engine Type: {self.engine_type}")

    # Moved the display_car_info method to the Car class
    def display_car_info(self):
        self.display_info()
        print(f"Fuel Type: {self.fuel_type}")


class ElectricCar(Car):
    def __init__(self, brand, model, fuel_type, battery_capacity):
        super().__init__(brand, model, fuel_type)
        self.battery_capacity = battery_capacity
    
class Car:  # Added for context; assumes Car class exists or is needed
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_electric_car_info(self):
        """
        Displays electric car information, including the base car info
        and the battery capacity. Moved from external function to here.
        """
        self.display_car_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


electric_car = ElectricCar("Tesla", "Model S", "Electric", 100)
electric_car.display_electric_car_info()




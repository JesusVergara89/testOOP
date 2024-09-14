from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.__brand = brand 
        self.__model = model 
    

    @abstractmethod
    def start_engine(self):
        pass

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def start_engine(self):
        return f"{self.get_brand()} {self.get_model()} engine started with a key."


class Motorbike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def start_engine(self):
        return f"{self.get_brand()} {self.get_model()} engine started with a button."


def vehicle_start(vehicle: Vehicle):
    print(vehicle.start_engine())


my_car = Car("Toyota", "Corolla", 4)
my_bike = Motorbike("Yamaha", "MT-07", 689)


print(f"Car brand: {my_car.get_brand()}")
print(f"Motorbike brand: {my_bike.get_brand()}")


vehicle_start(my_car)   
vehicle_start(my_bike)  

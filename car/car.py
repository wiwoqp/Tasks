from random import randint
import time

class Car:
    def __init__(self, engine_type, gas_tank):
        self.id = time.time()
        self.engine_type = engine_type
        self.gas_tank = gas_tank
        self.gas_station = gas_tank
        self.price = 10_000

        if engine_type == 'diesel':
            self.fuel_price = 1.8
            self.fuel_consumption = 6
            self.major_repair = 700
            self.top_down_price = 105
            self.max_mileage_limit = 150_000
        else:
            self.fuel_price = 2.4
            self.fuel_consumption = 8
            self.major_repair = 500
            self.top_down_price = 95
            self.max_mileage_limit = 100_000

        # счётчики
        self.__tachograph = 0
        self.fuel_fill_counter = 0
        self.how_much_spent_fuel = 0
        self.mileage_last_overhaul = 0
        self.tachograph_each_1000 = 0
        self.total_major_repair = 0

    def drive(self, miles):
        while miles > 0:
            step = min(100, miles)
            self.check_major_repair()
            fuel_needed = self.calculate_fuel(step)
            if self.gas_tank < fuel_needed:
                self.refuel()
            self.update_mileage(step, fuel_needed)
            self.depreciate()
            miles -= step

    def check_major_repair(self):
        if self.mileage_last_overhaul >= self.max_mileage_limit:
            self.total_major_repair += self.major_repair
            self.mileage_last_overhaul = 0

    def refuel(self):
        self.fuel_fill_counter += 1
        self.how_much_spent_fuel += self.gas_station * self.fuel_price
        self.gas_tank = self.gas_station

    def calculate_fuel(self, step):
        return step / self.fuel_consumption

    def update_mileage(self, step, fuel_needed):
        self.__tachograph += step
        self.tachograph_each_1000 += step
        self.gas_tank -= fuel_needed
        self.mileage_last_overhaul += step

    def depreciate(self):
        if self.tachograph_each_1000 >= 1000:
            self.price -= self.top_down_price
            self.fuel_consumption *= 1.01
            self.tachograph_each_1000 = 0

    def __repr__(self):
        return (f"<Car id={self.id}, mileage={round(self.__tachograph)}, "
                f"price={self.price}, fuel_spent={self.how_much_spent_fuel}>")

    def info(self):
        return {
            "mileage": round(self.__tachograph),
            "price": self.price,
            "fuel_spent": self.how_much_spent_fuel,
            "fuel_fills": self.fuel_fill_counter,
            "remaining_mileage": self.max_mileage_limit - self.mileage_last_overhaul,
            "repairs": self.total_major_repair
        }


class CarFactory:
    def __init__(self):
        self.cars = []

    def produce(self, n_cars=100):
        for i in range(1, n_cars + 1):
            engine_type = "diesel" if i % 3 == 0 else "petrol"
            gas_tank = 75 if i % 5 == 0 else 60
            route = randint(55_000, 286_000)
            car = Car(engine_type, gas_tank)
            car.drive(route)
            self.cars.append(car)

    def total_price(self):
        return sum(car.price for car in self.cars)

if __name__ == "__main__":
    factory = CarFactory()
    factory.produce()

    diesel_cars = [c for c in factory.cars if c.fuel_price == 1.8]
    petrol_cars = [c for c in factory.cars if c.fuel_price == 2.4]

    diesel_sorted = sorted(diesel_cars, key=lambda c: c.info()["price"], reverse=True)
    petrol_sorted = sorted(petrol_cars, key=lambda c: c.info()["remaining_mileage"], reverse=True)

    print(factory.total_price())
    print(factory.cars[0])

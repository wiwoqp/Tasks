from random import randint

class Car:
    def __init__(self, id, fuel_price, gas_tank, fuel_consumption,
                 major_repair, top_down_price, max_mileage_limit):
        self.id = id
        self.fuel_price = fuel_price
        self.gas_tank = gas_tank
        self.fuel_consumption = fuel_consumption
        self.major_repair = major_repair
        self.top_down_price = top_down_price
        self.price = 10_000
        self.route = randint(55_000, 286_000)
        self.max_mileage_limit = max_mileage_limit
        self.gas_station = gas_tank

        self.__tachograph = 0
        self.fuel_fill_counter = 0
        self.how_much_spent_fuel = 0
        self.mileage_last_overhaul = 0
        self.tachograph_each_1000 = 0
        self.total_major_repair = 0

    def drive(self, miles):
        while miles > 0:
            if self.mileage_last_overhaul >= self.max_mileage_limit:
                self.total_major_repair += self.major_repair
                self.mileage_last_overhaul = 0

            if self.gas_tank <= 0:
                self.fuel_fill_counter += 1
                self.how_much_spent_fuel += self.gas_station * self.fuel_price
                self.gas_tank = self.gas_station

            step = min(100, miles)
            fuel_needed = step / self.fuel_consumption

            if self.gas_tank < fuel_needed:
                self.fuel_fill_counter += 1
                self.how_much_spent_fuel += self.gas_station * self.fuel_price
                self.gas_tank = self.gas_station

            self.__tachograph += step
            self.tachograph_each_1000 += step
            self.gas_tank -= fuel_needed
            self.mileage_last_overhaul += step
            miles -= step

            if self.tachograph_each_1000 >= 1000:
                self.price -= self.top_down_price
                self.fuel_consumption *= 1.01
                self.tachograph_each_1000 = 0

    def __repr__(self):
        return (f"<Car id={self.id}, mileage={round(self.__tachograph)}, "
                f"price={self.price}, fuel_spent={self.how_much_spent_fuel}>")

    @property
    def info(self):
        return (
            round(self.__tachograph),
            self.price,
            self.how_much_spent_fuel,
            self.fuel_fill_counter,
            self.max_mileage_limit - self.mileage_last_overhaul,
            self.total_major_repair
        )


class CarFactory:
    def __init__(self):
        self.cars = []

    def produce(self):
        for i in range(1, 101):
            fuel_price = 2.4 if i % 3 == 0 else 1.8
            gas_tank = 75 if i % 5 == 0 else 60
            fuel_consumption = 6 if i % 3 == 0 else 8
            major_repair = 700 if i % 3 == 0 else 500
            top_down_price = 105 if i % 3 == 0 else 95
            max_mileage_limit = 150_000 if i % 3 == 0 else 100_000

            car = Car(i, fuel_price, gas_tank, fuel_consumption,
                      major_repair, top_down_price, max_mileage_limit)
            route = randint(55_000, 286_000)
            car.drive(route)
            self.cars.append(car)

    def total_price(self):
        return sum(car.price for car in self.cars)

factory = CarFactory()
factory.produce()

diesel_cars = [c for c in factory.cars if c.fuel_price == 1.8]
petrol_cars = [c for c in factory.cars if c.fuel_price == 2.4]

diesel_sorted = sorted(diesel_cars, key=lambda c: c.info[1], reverse=True)
petrol_sorted = sorted(petrol_cars, key=lambda c: c.info[4], reverse=True)

print(factory.total_price())
print(factory.cars[0])
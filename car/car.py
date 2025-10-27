from random import randint
class Car:

    def __init__(self, id):
        self.id = id
        self.fuel_price = 2.4 if self.id % 3 == 0 else 1.8
        self.gas_tank = 75 if self.id % 5 == 0 else 60
        self.fuel_consumption = 6 if self.id % 3 == 0 else 8
        self.major_repair = 700 if self.id % 3 == 0 else 500
        self.top_down_price = 105 if self.id % 3 == 0 else 95
        self.price = 10_000
        self.route = randint(55_000, 286_000)
        self.max_mileage_limit = 150_000 if self.id % 3 == 0 else 100_000
        self.__tachograph = 0
        self.fuel_fill_counter = 0
        self.how_much_spent_fuel = 0

        self.mileage_last_overhaul = 0
        self.tachograph_each_1000 = 0
        self.gas_station = self.gas_tank
        self.total_major_repair = 0

    def drive(self):
        while self.route > 0:
            while self.mileage_last_overhaul < self.max_mileage_limit:
                while self.gas_tank > 0:
                    self.__tachograph += 100 / self.fuel_consumption
                    self.tachograph_each_1000 += 100 / self.fuel_consumption
                    self.gas_tank -= 1
                    self.route -= 100 / self.fuel_consumption
                    self.mileage_last_overhaul += 100 / self.fuel_consumption
                    if self.tachograph_each_1000 >= 1000:
                        self.price -= self.top_down_price
                        self.fuel_consumption *= 1.01
                        self.tachograph_each_1000 = 0

                self.fuel_fill_counter += 1
                self.how_much_spent_fuel += self.gas_station * self.fuel_price
                self.gas_tank = self.gas_station # заливаем бак

            self.total_major_repair += self.major_repair
            self.mileage_last_overhaul = 0


    @property
    def info(self):
        return (
            round(self.__tachograph),  # mileage
            self.price,  # actual price
            self.how_much_spent_fuel,
            self.fuel_fill_counter,
            self.max_mileage_limit - self.mileage_last_overhaul, # milage before major repair
            self.total_major_repair  #total sum of major repair
        )

cars = []
total_price = 0

for i in range(1, 101):
    car = Car(i)
    car.drive()
    cars.append(car)
    total_price += car.price

diesel_cars = [i for i in cars if i.cost_fuel == 1.8]
petrol_cars = [i for i in cars if i.cost_fuel == 2.4]

diesel_sorted = sorted(diesel_cars, key=lambda c: c.info[1], reverse=True)
petrol_sorted = sorted(petrol_cars, key=lambda c: c.info[4], reverse=True)


print(total_price)





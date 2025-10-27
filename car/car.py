from random import randint
class Car:

    def __init__(self, id):
        self.id = id
        self.cost_fuel = 2.4 if self.id % 3 == 0 else 1.8  # стоимость топлива
        self.gas_tank = 75 if self.id % 5 == 0 else 60  # объем топливного бака
        self.fuel_consumption = 6 if self.id % 3 == 0 else 8  # расход на 100 км в литрах
        self.major_repair = 700 if self.id % 3 == 0 else 500 # стоимость кап ремонта
        self.top_down_cost = 105 if self.id % 3 == 0 else 95  # потеря стоимости каждые 1000 км
        self.price = 10_000 # начальная цена каждого авто
        self.way = randint(55_000, 286_000) # длина маршрута
        self.max_mileage_limit = 150_000 if self.id % 3 == 0 else 100_000  # максимальный пробег до кап ремонта
        self.__tachograph = 0 # считывает пробег авто
        self.fuel_fill_counter = 0 # сколько раз заправлялись
        self.how_much_spent_fuel = 0  # сколько потратили на заправку

        self.mileage_last_overhaul = 0  # пробег с последним кап ремонта
        self.tachograph_each_1000 = 0  # внутренний тахограф на 1000 км
        self.gas_station = self.gas_tank # копия данных объема топлива
        self.total_major_repair = 0  # общая стоимость кап ремонтов

    def drive(self):
        while self.way > 0:
            while self.mileage_last_overhaul < self.max_mileage_limit:
                while self.gas_tank > 0:
                    self.__tachograph += 100 / self.fuel_consumption # добавляем километраж за один литр топлива
                    self.tachograph_each_1000 += 100 / self.fuel_consumption
                    self.gas_tank -= 1 # минус один литр
                    self.way -= 100 / self.fuel_consumption  # отнимаем расстояние от общего маршрута
                    self.mileage_last_overhaul += 100 / self.fuel_consumption # переменная для цикла
                    if self.tachograph_each_1000 >= 1000: # каждые 1000 км уменьшаем стоимость увеличиваем расход на 1%
                        self.price -= self.top_down_cost
                        self.fuel_consumption *= 1.01
                        self.tachograph_each_1000 = 0
                # Заправка
                self.fuel_fill_counter += 1  # количество заправок
                self.how_much_spent_fuel += self.gas_station * self.cost_fuel # сколько тратим
                self.gas_tank = self.gas_station # заливаем бак


            # Капитальный ремонт
            self.total_major_repair += self.major_repair
            self.mileage_last_overhaul = 0

    @property
    def info(self):
        return (
            round(self.__tachograph),  # Пробег
            self.price,  # Остаточная стоимость
            self.how_much_spent_fuel,  # Сколько потрачено на топливо
            self.fuel_fill_counter,  # количество заправок
            self.max_mileage_limit - self.mileage_last_overhaul, # сколько осталось до кап ремонта
            self.total_major_repair  # общая стоимость кап ремонта
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





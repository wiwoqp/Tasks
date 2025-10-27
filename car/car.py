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

        self.for_second_while = 0  # переменная для второго внутреннего цикла
        self.tachograph_each_1000 = 0  # внутренний тахограф на 1000 км
        self.gas_tank_copy = self.gas_tank # копия данных объема топлива
        self.total_major_repair = 0
        self.max_mileage_limit_copy = self.max_mileage_limit

    def __drive(self):
        while self.way > 0:
            while self.for_second_while < self.max_mileage_limit:
                while self.gas_tank > 0:
                    self.__tachograph += 100 / self.fuel_consumption # добавляем километраж за один литр топлива
                    self.tachograph_each_1000 += 100 / self.fuel_consumption
                    self.gas_tank -= 1 # минус один литр
                    self.way -= 100 / self.fuel_consumption  # отнимаем расстояние от общего маршрута
                    self.for_second_while += 100 / self.fuel_consumption # переменная для цикла
                    if self.tachograph_each_1000 >= 1000: # каждые 1000 км уменьшаем стоимость увеличиваем расход на 1%
                        self.price -= self.top_down_cost
                        self.fuel_consumption *= 1.01
                        self.tachograph_each_1000 = 0
                # Заправка
                while True:
                    self.fuel_fill_counter += 1  # количество заправок
                    self.how_much_spent_fuel += self.gas_tank_copy * self.cost_fuel # сколько тратим
                    self.gas_tank = self.gas_tank_copy # заливаем бак
                    break

            # Капитальный ремонт
            while True:
                self.total_major_repair += self.major_repair
                break







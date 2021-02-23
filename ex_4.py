class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(
            f'new car: {self.name} (color {self.color}), police car - {self.is_police}')

    def go(self):
        print(f'{self.name}: Car started.')

    def stop(self):
        print(f'{self.name}: Car stopped.')

    def turn(self, direction):
        print(
            f'{self.name}: Car turned: {"left" if direction == 0 else "right"}.')

    def show_speed(self):
        return f'{self.name}: car speed: {self.speed}.'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: car speed: {self.speed}. exceeded the speed!' \
            if self.speed > 60 else f"{self.name}: car speed: {self.speed}."


class Truck(Car):

    def show_speed(self):
        return f'{self.name}: car speed: {self.speed}. exceeded the speed!' \
            if self.speed > 40 else f"{self.name}: car speed: {self.speed}."


class SportCar(Car):
    '''sport car'''


class PoliceCar(Car):
    '''police car'''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar("Audi", "green", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = Truck('"truck"', 'grey', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('"sport car"', 'yellow', 120)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"car"', 'white', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\ncar {town_car.name} (color {town_car.color})')
print(f'car {police_car.name} (color {police_car.color})')

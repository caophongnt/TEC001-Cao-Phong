import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        print(f"\nRace status: {self.name}")
        print(f"{'Reg.Number':<12} {'Max.Speed':<10} {'Cur.Speed':<10} {'Distance':<10}")
        print("-" * 50)
        for car in self.cars:
            print(f"{car.registration_number:<12} {car.max_speed:<10} {car.current_speed:<10} {car.travelled_distance:<10.1f}")
        print("-" * 50)
    def race_finished(self):
        return any(car.travelled_distance >= self.kilometers for car in self.cars)
def main():
    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_speed = random.randint(150, 200)
        cars.append(Car(reg_num, max_speed))
    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()
    race.print_status()
    print(f"\nRace finished in {hours} hours!")
if __name__ == "__main__":
    main()

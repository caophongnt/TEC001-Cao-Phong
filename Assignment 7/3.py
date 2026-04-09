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
def main():
    car = Car("ABC-123", 142)
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print("Current speed after accelerations:", car.current_speed, "km/h")
    car.drive(1.5)
    print("Travelled distance after driving:", car.travelled_distance, "km")
    car.accelerate(-200)
    print("Final speed after emergency brake:", car.current_speed, "km/h")
if __name__ == "__main__":
    main()

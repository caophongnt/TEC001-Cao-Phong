class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator is now at floor {self.current}")
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator is now at floor {self.current}")
    def go_to_floor(self, target):
        if target < self.bottom or target > self.top:
            print("Invalid floor")
            return
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number")
    def fire_alarm(self):
        print("Fire alarm! All elevators moving to bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} returning to bottom floor")
            elevator.go_to_floor(self.bottom)


# Chương trình chính để test
if __name__ == "__main__":
    building = Building(1, 10, 3)
    building.run_elevator(0, 5)
    building.run_elevator(1, 8)
    building.run_elevator(2, 6)
    building.fire_alarm()

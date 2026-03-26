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


# Chương trình chính để test
if __name__ == "__main__":
    h = Elevator(1, 10)   
    h.go_to_floor(5)      
    h.go_to_floor(1)      
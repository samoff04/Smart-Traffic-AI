class Stats:
    def __init__(self):
        self.cars_passed = 0

    def update(self, cars):
        for car in cars:
            if car.y < -50 and not car.counted:
                self.cars_passed += 1
                car.counted = True
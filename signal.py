class TrafficSignal:
    def __init__(self):
        self.state = "GREEN"
        self.timer = 0

    def update(self):
        self.timer += 1

        if self.timer < 200:
            self.state = "GREEN"
        elif self.timer < 350:
            self.state = "RED"
        else:
            self.timer = 0
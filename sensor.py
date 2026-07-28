class Sensor:
    def __init__(self):
        self.readings = []
        self.stuck_count = 0

    def get_reading(self, value):
        self.readings.append(value)

        if len(self.readings) > 1:
            if self.readings[-1] == self.readings[-2]:
                self.stuck_count += 1
            else:
                self.stuck_count = 0

        return value

    def is_stuck(self):
        return self.stuck_count >= 5

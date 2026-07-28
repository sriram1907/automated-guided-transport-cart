from state_machine import StateMachine

class Controller:

    THRESHOLD = 20
    REQUIRED_COUNT = 3

    def __init__(self):
        self.machine = StateMachine()
        self.low_count = 0

    def process(self, distance, sensor_fault):

        if sensor_fault:
            self.machine.change_state(StateMachine.FAULT)
            return "FAULT"

        if distance < self.THRESHOLD:
            self.low_count += 1
        else:
            self.low_count = 0

        if self.low_count >= self.REQUIRED_COUNT:
            self.machine.change_state(StateMachine.OBSTACLE_STOP)
            return "STOP"

        self.machine.change_state(StateMachine.MOVING)
        return "MOVE"

    def reset(self):
        self.low_count = 0
        self.machine.change_state(StateMachine.IDLE)

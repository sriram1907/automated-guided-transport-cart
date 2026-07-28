class StateMachine:
    IDLE = "IDLE"
    MOVING = "MOVING"
    OBSTACLE_STOP = "OBSTACLE_STOP"
    FAULT = "FAULT"

    def __init__(self):
        self.state = self.IDLE

    def change_state(self, new_state):
        print(f"State Change: {self.state} -> {new_state}")
        self.state = new_state

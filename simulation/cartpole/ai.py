import random
from helpers import quat_to_euler

class RandomAI:
    def __init__(self):
        self.num_actions = 4


    def act(self, state):
        return random.randint(0, self.num_actions)
    

    def process_state(self, world, plate, cylinder):
        return quat_to_euler(*cylinder.get_quaternion())
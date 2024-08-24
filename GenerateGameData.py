import math
import random


class GenerateGameData:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.minimum_guess = 0

    def generate_minimum_guess(self):
        self.minimum_guess = math.log2(self.upper_bound - self.lower_bound + 1)
        return math.ceil(self.minimum_guess)

    def number_to_guess(self):
        number = random.randint(self.lower_bound, self.upper_bound)
        return number





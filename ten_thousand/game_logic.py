import random

"""
(TODO)
1. Define a GameLogic class

2. Handle calculating score for dice roll
    - Add calculate_score static method to GameLogic class.
    - The input to calculate_score is a tuple of integers that represent a dice roll.
    - The output from calculate_score is an integer representing the roll’s score according to rules of game

3. Handle rolling dice
    - Add roll_dice static method to GameLogic class.
    - The input to roll_dice is an integer between 1 and 6.
    - The output of roll_dice is a tuple with random values between 1 and 6.
    - The length of tuple must match the argument given to roll_dice method.
"""


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
        Rolls n number of dice
        :param n: number of dice
        :return: a tuple with random values between 1 and 6
        """
        dice = []
        for i in range(n):
            dice.append(random.randint(1, 6))
        return tuple(dice)

    @staticmethod
    def calculate_score():
        pass


if __name__ == "__main__":
    pass

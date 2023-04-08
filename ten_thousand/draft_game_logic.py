import random
from collections import Counter

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
# """
#
# roll()
# find_patterns()
# assign_points()
# go_again()
# def turn(number_of_dice, points):
#     roll = [1, 2, 3, 4, 5, 6]
#     roll.sort()
#     ## look for x of a kind
#     points = 0
#     num_dice_counted = 0
#     if sorted(roll) == [1, 2, 3, 4, 5, 6]:
#         points += 1500
#         num_dice_counted = 6
#     else:
#         prev = None  # compare the current value against the previous value
#         of_a_kind_count = 0
#         of_a_kind_value = None
#         pair_count = 0
#         triplet_count = 0
#         triplet_value = None
#         one_count = 0
#         five_count = 0
#         ## find_values
#         for value in roll:
#             ## count the number of 1's and 5's
#             if value == 1:
#                 one_count += 1
#             if value == 5:
#                 five_count += 5
#             if value == prev:
#                 of_a_kind_count += 1
#                 of_a_kind_value = value
#             elif of_a_kind_count == 2:
#                 pair_count += 1
#             elif of_a_kind_count == 3:
#                 triplet_count += 1
#                 triplet_value.push(value)  ## Lauren do this
#             prev = value
#
#         ## assign points
#         if pair_count == 3:
#             points = 1500
#             num_dice_counted = 6
#         elif triplet_count == 2:
#             ## Lauren do this
#             num_dice_counted = 6
#         elif of_a_kind_count > 3:
#             ## points - LAUREN DO THIS
#             ## assign the correct number of points for the of_a_kind_value and of_a_kind_count and num_dice_counted
#         ## understand more about when to assign value for 1's and 5's
#         elif one_count > 0 or five_count > 0:
#             points += one_count * 100
#             points += five_count * 50
#             num_dice_counted = one_count + five_count
#
#     remaining_dice = 6 - num_dice_counted
#     if remaining_dice == 0:
#         ## definitely roll HOT DICE
#     else:
#         # ask the user - roll again?


class GameLogic:


    score_combinations = {
        "1": 100,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 50,
        "6": 0,
        "3 of a kind": {
            "1": 1000,
            "2": 200,
            "3": 300,
            "4": 400,
            "5": 500,
            "6": 600
        },
        "4 of a kind": {
            "1": 2000,
            "2": 400,
            "3": 600,
            "4": 800,
            "5": 1000,
            "6": 1200
        },
        "5 of a kind": {
            "1": 3000,
            "2": 600,
            "3": 900,
            "4": 1200,
            "5": 1500,
            "6": 1800
        },
        "6 of a kind": {
            "1": 4000,
            "2": 800,
            "3": 1200,
            "4": 1600,
            "5": 2000,
            "6": 2400
        },
        "straight": 1500,
        "3 pairs": 1500,
    }

    @staticmethod
    def roll_dice(n):
        """
        Rolls n number of dice
        :param n: number of dice
        :return: a tuple with random values between 1 and 6
        """

        dice = []
        for _ in range(n):
            dice.append(random.randint(1, 6))
        return tuple(dice)

    @staticmethod
    def calculate_score(combination):
        """
        Calculates the score depending on the combination of 6 randomly generated numbers in a tuples
        :param combination: tuple of 6 integers representing different dice combinations
        :return: An integer representing a score
        """

        total_score = 0
        counts = Counter(combination)

        if sorted(combination) == [1, 2, 3, 4, 5, 6]:
            total_score += GameLogic.score_combinations['straight']
            return total_score
#waht si the big O cost of using the most_common method
        if len(counts.most_common()) >= 2 and counts.most_common()[0][1] == 3 and counts.most_common()[1][1] == 3:
            total_score = GameLogic.score_combinations['3 of a kind'][str(counts.most_common()[0][0])] \
                          + GameLogic.score_combinations['3 of a kind'][str(counts.most_common()[1][0])]
            return total_score

        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            total_score += GameLogic.score_combinations['3 pairs']
            return total_score

        for key in ['6 of a kind', '5 of a kind', '4 of a kind', '3 of a kind']:
            for value in combination:
                if combination.count(value) >= int(key[0]):
                    total_score += GameLogic.score_combinations[key][str(value)]
                    combination = [x for x in combination if x != value]
                    if key == '6 of a kind':
                        combination = []
                    break
        ## This is wrong - do we assign the values of 1's and 5's in addition to straights/of a kinds etc?
        for value in combination:
            total_score += GameLogic.score_combinations[str(value)]
        print(total_score)
        return total_score


if __name__ == "__main__":
    pass

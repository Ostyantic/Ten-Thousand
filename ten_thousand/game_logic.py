import random
from collections import Counter



class GameLogic:

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

        total_score = 0
        num_dice_counted = Counter(combination).most_common()

        if not num_dice_counted:
            return total_score

    #3,4,5, and 6 of a kind

        if(num_dice_counted[0][1]) >= 3:
            if num_dice_counted[0][0] !=1:
                total_score += num_dice_counted[0][0] *100*(num_dice_counted[0][1]-2)
            else:
                total_score += 1000 *(num_dice_counted[0][1]-2)
            num_dice_counted = num_dice_counted[1:]

    #two 3 of a kinds

        if len(num_dice_counted) == 1 and num_dice_counted[0][1] == 3:
            if num_dice_counted[0][0] != 1:
                total_score += num_dice_counted[0][0]* 100
            else:
                total_score += 1000


    #straight

        if len(num_dice_counted) == 6:
            total_score += 1500
            return total_score

    #three pairs

        if len(num_dice_counted) == 3 and num_dice_counted[2][1] == 2:
            total_score += 1500
            return total_score

    #single 5 or 1

        else:
            for combination in num_dice_counted:
                if combination[0] == 5:
                    total_score += combination[1] *50
                if combination[0] == 1:
                    total_score += combination[1] *100

            return total_score

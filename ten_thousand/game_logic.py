import random
from collections import Counter



class GameLogic:
    def __init__(self, mock_rolls=None):
        self.mock_rolls = mock_rolls

    def mock_roller(self, _,):
        return self.mock_rolls.pop(0)

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
       #first check to see if there is a most.common element occurring 3 times
        if(num_dice_counted[0][1]) >= 3:
            #then check to be sure it isn't the exception 3 1s
            if num_dice_counted[0][0] !=1:
                #then multiple each die face by 100, each die face is worth 100 points,
                # then subtract 2, from the count of the dice, which is 6, so that we are left with 3 dice
                total_score += num_dice_counted[0][0] *100*(num_dice_counted[0][1]-2)
            else:
                #this treats the special case of 1 being the most common with the same logic as above
                total_score += 1000 *(num_dice_counted[0][1]-2)
                #stash the dice already counted, and then continue to look through the remaining dice
                # I need to do this because there are the possibility of 4,5,6
            num_dice_counted = num_dice_counted[1:]
        #return total_score

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

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        # for i in range(len(dice)):

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(val)

        return tuple(scorers)






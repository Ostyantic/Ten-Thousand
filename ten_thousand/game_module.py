from game_logic import *

# currently_playing = True


def welcome():
    print("""Welcome to Ten Thousand
    (y)es to play or (n)o to decline""")
    prompt = input("> ")

    if prompt == "n":
        decline()
    else:
        total_score = play_game()
        if total_score != -1:
            print(f"Thanks for playing. You earned {total_score} points")


def decline():
    print("OK. Maybe another time")


def play_game(roll=GameLogic.roll_dice):
    total_score = 0
    round_number = 1

    while round_number <= 20:
        print(f"Starting round {round_number}")  # function
        round_score, total_score = play_round(roll, total_score, round_number)
        if round_score == -1:
            return total_score
        round_number += 1

    # print(f"Thanks for playing. You earned {total_score} points")
    # return total_score


def play_round(roll, total_score, r):
    # banked_dice = []
    round_number = r
    dice_rolled = roll
    round_score = 0
    dice_count = 6

    while True:
        print(f"Rolling {len(dice_rolled(dice_count))} dice...")  # goes to dice function
        print('***', *dice_rolled(dice_count), '***')
        player_choice = banked_dice()
        dice_count -= len(player_choice)
        if len(dice_rolled(dice_count)) == 0:
            player_choice = hot_dice()
        # print("player choice: ", player_choice)
        # print("testing the play round function")
        if player_choice == "q":
            return -1, total_score

        temp_score = GameLogic.calculate_score(player_choice)
        # remaining = remaining_dice(player_choice)
        print(f"You have {GameLogic.calculate_score(player_choice)} unbanked points and {dice_count} dice remaining")
        choice = players_choice_rbq()
        if choice == "b":
            round_score += temp_score
            total_score += round_score
            print(f"You banked {round_score} points in this round")
            return round_score, total_score
        elif choice == "r":
            updated_banked_dice = player_choice
            while True:
                zilcher = is_zilch(dice_rolled(remaining))
                print(zilcher)
                if zilcher:
                    print(f"""****************************************
**        Zilch!!! Round over         **
****************************************
You banked {round_score} points in round {round_number}
Total score is {total_score} points""")
                print(f"Rolling {dice_count} dice...")
                print('***', *dice_rolled(dice_count), '***')
                new_roll = banked_dice()
                if new_roll == "q":
                    return -1, total_score

                updated_banked_dice += new_roll

                temp_score += GameLogic.calculate_score(new_roll)
                # remaining = remaining_dice(updated_banked_dice)
                # print(updated_banked_dice)
                print(f"You have {round_score} unbanked points and {dice_count} dice remaining")
                choice = players_choice_rbq()
                if choice == "b":
                    round_score += temp_score
                    total_score += round_score
                    print(f"You banked {round_score} points in this round")
                    return round_score, total_score
                elif choice == "q":
                    return -1, total_score
            # possible fix(?) below
            # round_score += GameLogic.calculate_score(updated_banked_dice)
            # total_score += round_score
            # round_score = 0
        #elif choice == "q":
            # return -1, total_score



def is_zilch(roll):
    """
    Determines if a roll of dice results in a zilch in the game of Ten Thousand
    :param roll: A list or tuple of integers representing the numbers rolled on each die.
    :return: True if roll is a zilch, otherwise returns False
    """
    points = GameLogic.calculate_score(roll)
    if points > 0:
        return False
    return True


def banked_dice():
    player_choice = input_to_tuple(input("Enter dice to keep, or (q)uit:\n> "))
    if player_choice == "q":
        return "q"
    return player_choice


def input_to_tuple(input_string):
    input_string = input_string.replace(' ', '')
    roll_list = []
    if input_string == "q":
        return "q"
    for i in input_string:
        roll_list.append(int(i))
    # requires some type of iterable data
    return tuple(roll_list)


# def remaining_dice(kept_dice, total_dice=6):
#     remaining = total_dice - len(kept_dice)
#     return remaining


def players_choice_rbq():
    player_choice = input("""
    (r)oll again, (b)ank your points or (q)uit:
    > """)
    return player_choice

def hot_dice(roll=GameLogic.roll_dice):
        # print("hot dice")
        score = 0
        dice_count = 6

        dice_rolled = roll(dice_count)
        print ("testing dice rolled", dice_rolled)

            # if dice_count == 6:
        print("PRINT HOT DICE")
        print('***', *dice_rolled, '***')

        player_choice = banked_dice()
        dice_count -= len(player_choice)
        hot_dice_score = GameLogic.calculate_score(player_choice)
        print(f"You have {hot_dice_score} unbanked points and {dice_count} dice remaining HOT DICE FUNCTION")
        hot_dice_choice = input("""Do you want to (r)oll again, (b)ank your points, or (q)uit? 
             >""")
        if hot_dice_choice == "r":
            while True:
                # round_score = GameLogic.calculate_score(dice_rolled)
                # choice = players_choice_rbq()
                #
                print(f"Rolling {len(dice_rolled)} dice...")
                print('***', *dice_rolled, '***')
                # print("testing dice rolled if player choice is r", dice_rolled)
                return dice_rolled

        if hot_dice_choice == "b":
            score += hot_dice_score
            print(f"You banked {hot_dice_score} points in this round")
            return score
        if hot_dice_choice == "q":
            return "q"




if __name__ == "__main__":
    welcome()

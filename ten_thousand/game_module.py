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


def play_round(roll, total_score, r):
    # banked_dice = []
    round_number = r
    dice_rolled = roll
    round_score = 0
    dice_count = 6

    while True:
        dice = dice_rolled(dice_count)
        print(dice)
        print(f"Rolling {len(dice_rolled(dice_count))} dice...")
        # print('***', *dice_rolled(dice_count), '***')

        while True:
            print('***', *dice, '***')
            player_choice = banked_dice()
            validate = check_for_cheater(dice, player_choice)
            if validate == "q":
                return -1, total_score
            if validate is True:
                print("Cheater!!! Or possibly made a typo...")
            elif not validate:
                break
        # while True:
        #     print('***', *dice, '***')
        #     player_choice = banked_dice()
        #     validate = check_for_cheater(dice, player_choice)
        #     if validate == "q":
        #         return -1, total_score
        #     if not validate:
        #         print("Cheater!!! Or possibly made a typo...")
        #     elif validate is True:
        #         break

        dice_count -= len(player_choice)
        round_score += GameLogic.calculate_score(player_choice)
        fire_dice = hot_dice(dice_count)
        if fire_dice:
            dice_count = 6
            print("*** HOT DICE!! ***")
            continue
        print(f"You have {round_score} unbanked points and {dice_count} dice remaining")
        choice = players_choice_rbq()
        if choice == "b":
            total_score += round_score
            print(f"You banked {round_score} points in this round")
            return round_score, total_score
        elif choice == "q":
            return -1, total_score
        elif choice == "r":
            updated_banked_dice = player_choice
            while True:
                zilcher = is_zilch(dice_rolled(dice_count))
                print(zilcher)
                if zilcher:
                    round_score = 0
                    print(f"""****************************************
**        Zilch!!! Round over         **
****************************************
You banked {round_score} points in round {round_number}
Total score is {total_score} points""")
                    return round_score, total_score
                dice = dice_rolled(dice_count)
                print(f"Rolling {dice_count} dice...")

                while True:
                    print('***', *dice, '***')
                    new_roll = banked_dice()
                    validate = check_for_cheater(dice, new_roll)
                    if validate == "q":
                        return -1, total_score
                    if validate is True:
                        print("Cheater!!! Or possibly made a typo...")
                    elif not validate:
                        break

                dice_count -= len(new_roll)
                if new_roll == "q":
                    return -1, total_score
                updated_banked_dice += new_roll
                round_score += GameLogic.calculate_score(new_roll)
                fire_dice = hot_dice(dice_count)
                if fire_dice:
                    dice_count = 6
                    print("*** HOT DICE!! ***")
                    break
                print(f"You have {round_score} unbanked points and {dice_count} dice remaining")
                choice = players_choice_rbq()
                if choice == "b":
                    total_score += round_score
                    print(f"You banked {round_score} points in this round")
                    return round_score, total_score
                elif choice == "q":
                    return -1, total_score


def check_for_cheater(roll, saved_dice):

    if saved_dice == "q":
        return "q"

    return bool(Counter(saved_dice) - Counter(roll))

    # for die in saved_dice:
    #     if die in roll:
    #         return True




def is_zilch(roll):
    """
    Determines if a roll of dice results in a zilch in the game of Ten Thousand
    :param roll: A list or tuple of integers representing the numbers rolled on each die.
    :return: True if roll is a zilch, otherwise returns False
    """
    points = GameLogic.calculate_score(roll)
    if points > 0:
        return False
    if points == 0:
        return True


def banked_dice():
    player_choice = input_to_tuple(input("Enter dice to keep, or (q)uit:\n> "))
    if player_choice == "q":
        return "q"
    return player_choice


def input_to_tuple(input_string):
    if input_string == "q":
        return "q"
    roll_list = tuple(int(num) for num in input_string if num.isnumeric())
    return tuple(roll_list)


def players_choice_rbq():
    player_choice = input("""
    (r)oll again, (b)ank your points or (q)uit:
    > """)
    return player_choice


def hot_dice(length):
    if length == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    welcome()

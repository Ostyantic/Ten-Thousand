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
        round_score, total_score = play_round(roll, total_score)
        if round_score == -1:
            return total_score
        round_number += 1

    # print(f"Thanks for playing. You earned {total_score} points")
    # return total_score


def play_round(roll, total_score):
    # banked_dice = []
    dice_rolled = roll
    round_score = 0
    dice_count = 6

    while True:
        print(f"Rolling {len(dice_rolled(dice_count))} dice...")  # goes to dice function
        print('***', *dice_rolled(dice_count), '***')
        # in process, subject to change

        player_choice = banked_dice()
        print("player choice: ", player_choice)
        # print("testing the play round function")
        if player_choice == "q":
            return -1, total_score

        # """ hot dice logic
        if len(player_choice) == 6:
            player_choice= hot_dice()
            remaining = 6
        # round_score += GameLogic.calculate_score(player_choice)
            if type(player_choice) == tuple:

                # print(f"You have {GameLogic.calculate_score(player_choice)} unbanked points and {remaining} dice remaining PLAY ROUND")
                player_choice = banked_dice()
            # else type(player_choice) == str:
            # """

        round_score += GameLogic.calculate_score(player_choice)
        remaining = remaining_dice(player_choice)
        print(f"You have {GameLogic.calculate_score(player_choice)} unbanked points and {remaining} dice remaining")
        choice = players_choice_rbq()
        if choice == "b":
            total_score += round_score
            print(f"You banked {round_score} points in this round")
            return round_score, total_score
        elif choice == "r":
            updated_banked_dice = player_choice
            while True:
                remaining = remaining_dice(updated_banked_dice)
                if remaining == 0:
                    break
                print(f"Rolling {remaining} dice...")
                print('***', *dice_rolled(remaining), '***')
                new_roll = input_to_tuple(input("""Enter dice to keep, or (q)uit:
                    > """))
                if new_roll == "q":
                    return -1, total_score
                updated_banked_dice += new_roll
                round_score += GameLogic.calculate_score(new_roll)
                remaining = remaining_dice(updated_banked_dice)
                print(updated_banked_dice)
                print(f"You have {round_score} unbanked points and {remaining} dice remaining")
                choice = players_choice_rbq()
                if choice == "b":
                    total_score += round_score
                    print(f"You banked {round_score} points in this round")
                    return round_score, total_score
                elif choice == "q":
                    return -1, total_score
            round_score += GameLogic.calculate_score(updated_banked_dice)
            total_score += round_score
            round_score = 0
        elif choice == "q":
            return -1, total_score


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


def remaining_dice(kept_dice, total_dice=6):
    remaining = total_dice - len(kept_dice)
    return remaining


def players_choice_rbq():
    player_choice = input("""
    (r)oll again, (b)ank your points or (q)uit:
    > """)
    return player_choice

def hot_dice(roll=GameLogic.roll_dice):
        # print("hot dice")
        dice_count = 6
        while True:
            dice_rolled = roll(dice_count)
            print ("testing dice rolled", dice_rolled)

            if dice_count == 6:
                # print(f"Rolling {len(dice_rolled)} dice...")
                # print('***', *dice_rolled, '***')
                print(f"You have {GameLogic.calculate_score(dice_rolled)} unbanked points and {dice_count} dice remaining HOT DICE FUNCTION")
                hot_dice_score = GameLogic.calculate_score(dice_rolled)
                hot_dice_choice = input("""Do you want to (r)oll again, (b)ank your points, or (q)uit? 
             >""")
                # if player_choice == "q":
                #     return
                if hot_dice_choice == "r":
                    # round_score = GameLogic.calculate_score(dice_rolled)
                    # choice = players_choice_rbq()
                    #
                    print(f"Rolling {len(dice_rolled)} dice...")
                    dice_rolled = roll(dice_count)
                    print('***', *dice_rolled, '***')
                    # print("testing dice rolled if player choice is r", dice_rolled)
                    return dice_rolled

                if hot_dice_choice == "b":
                    # print(f"You banked {round_score} points in this round")
                    # return banked_dice()
                    return hot_dice_choice
                elif hot_dice_choice == "q":
                    # return decline()
                    return hot_dice_choice
                # return dice_rolled, hot_dice_choice

if __name__ == "__main__":
    welcome()

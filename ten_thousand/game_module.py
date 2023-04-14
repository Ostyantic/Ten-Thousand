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

    return total_score

    # print(f"Thanks for playing. You earned {total_score} points")
    # return total_score


def play_round(roll, total_score):
    # banked_dice = []
    # dice_rolled = roll
    dice_count = 6
    original_dice = roll(dice_count)
    round_score = 0

    while True:
        print(f"Rolling {len(original_dice)} dice...")  # goes to dice function
        print('***', *original_dice, '***')
        # in process, subject to change

        player_choice = banked_dice(original_dice)
        # banked_dice = input_to_tuple(input("""Enter dice to keep, or (q)uit:
        # > """))
        if player_choice == "q":
            return -1, total_score

        # Verify that player only kept provided dice
        if not set(player_choice).issubset(set(original_dice)):
            print("Cheater!!! Or possibly made a typo...")
            continue

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
                updated_dice = roll(remaining)
                print('***', *updated_dice, '***')
                new_roll = input_to_tuple(input("""Enter dice to keep, or (q)uit:
                    > """))
                if new_roll == "q":
                    return -1, total_score
                if not set(new_roll).issubset(set(updated_dice)):
                    print("Cheater!!! Or possibly made a typo...")
                    continue
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


def banked_dice(original_dice):
    while True:
        player_choice = input_to_tuple(input("Enter dice to keep, or (q)uit:\n> "))
        if player_choice == ("q", ):
            return "q"
        elif not check_for_cheater(original_dice, player_choice):
            return player_choice


# def check_for_cheater(original_dice, player_choice):
#     if not set(player_choice).issubset(set(original_dice)) or \
#             set(player_choice) != set(filter(lambda x: x in player_choice, original_dice)):
#
#         print("Cheater!!! Or possibly made a typo...")
#         print('***', *original_dice, '***')
#         return True
#     return False

# def check_for_cheater(original_dice, player_choice):
#     original_dice_list = list(original_dice)
#     player_choice_list = list(player_choice)
#
#     # sort the lists
#     original_dice_list.sort()
#     player_choice_list.sort()
#
#     # check if the player's choice is equal to the original dice
#     if player_choice_list != original_dice_list:
#         print("Cheater!!! Or possibly made a typo...")
#         print(f"Original dice: {original_dice}")
#         return True
#     return False

def check_for_cheater(original_dice, player_choice):
    for value in tuple(player_choice):
        if player_choice.count(value) > original_dice.count(value):
            print("Cheater!!! Or possibly made a typo...")
            print('***', *original_dice, '***')
            return True
    return False


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


if __name__ == "__main__":
    welcome()

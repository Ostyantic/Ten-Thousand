from game_logic import *

#currently_playing = True

def welcome():
    print("""Welcome to Ten Thousand
    (y)es to play or (n)o to decline""")
    prompt = input("> ")

    if prompt == "n":
        decline()
    else:
        play_game()


def decline():
        print ("OK. Maybe another time")


def play_game(roll=GameLogic.roll_dice):
    total_score = 0
    round_number = 1

    while round_number <= 20:
        print(f"Starting round {round_number}")  # function
        round_score, total_score = play_round(roll, total_score)
        if round_score == -1:
            return total_score
        round_number += 1

    print(f"Thanks for playing. You earned {total_score} points")
    return total_score


def play_round(roll, total_score):
    banked_dice = []
    dice_rolled = roll
    round_score = 0

    while True:
        print(f"Rolling {len(dice_rolled(6))} dice...")  # goes to dice function
        print(*dice_rolled(6))
        # in process, subject to change
        banked_dice = input_to_tuple(input("""Enter dice to keep, or (q)uit:
        > """))
        if banked_dice == "q":
            return -1, total_score

        round_score += GameLogic.calculate_score(banked_dice)
        remaining = remaining_dice(banked_dice)
        print(f"You have {GameLogic.calculate_score(banked_dice)} unbanked points and {remaining} dice remaining")
        choice = players_choice_rbq()
        if choice == "b":
            total_score += round_score
            print(f"You banked {round_score} points in this round")
            return round_score, total_score
        elif choice == "r":
            updated_banked_dice = banked_dice
            while True:
                remaining = remaining_dice(updated_banked_dice)
                if remaining == 0:
                    break
                print(f"Rolling {remaining} dice...")
                print(*dice_rolled(remaining))
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


def input_to_tuple(input_string):
    roll_list = []
    if input_string == "q":
        return "q"
    for i in input_string:
        roll_list.append(int(i))
    #requires some type of iterable data
    return tuple(roll_list)

def remaining_dice(banked_dice, total_dice = 6):
    remaining = total_dice - len(banked_dice)
    return remaining

def players_choice_rbq():
    player_choice = input ("""
    (r)oll again, (b)ank your points or (q)uit:
    > """)
    return player_choice

welcome()
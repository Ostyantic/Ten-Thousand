from ten_thousand.game_logic import *

# currently_playing = True


def play(roll=GameLogic.roll_dice):
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    prompt = input("> ")

    if prompt == "n":
        print("OK. Maybe another time")
        return
    else:
        total_score = play_game(roll)
        if total_score != -1:
            print(f"Thanks for playing. You earned {total_score} points")


def play_game(roll):
    total_score = 0
    round_number = 1

    while round_number <= 20:
        print(f"Starting round {round_number}")  # function
        round_score, total_score = play_round(roll, total_score, round_number)
        if round_score == 0:
            return total_score
        round_number += 1


def play_round(roll, total_score, r):
    round_number = r
    round_score = 0
    dice_count = 6

    while True:
        dice = roll(dice_count)
        zilcher = is_zilch(dice)
        # print(zilcher)
        print(f"Rolling {len(dice)} dice...")

        while True:
            print(f"*** {' '.join([str(i) for i in dice])} ***")
            # print('***', *dice, '***')
            if zilcher:
                round_score = 0
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                print(f"You banked {round_score} points in round {round_number}")
                print(f"Total score is {total_score} points")
                return round_score, total_score
            player_choice = banked_dice()
            validate = check_for_cheater(dice, player_choice)
            if validate == "q":
                return total_score
            if validate is True:
                print("Cheater!!! Or possibly made a typo...")
            elif not validate:
                break
        dice_count -= len(player_choice)
        round_score += GameLogic.calculate_score(player_choice)
        fire_dice = hot_dice(dice_count)
        if fire_dice:
            dice_count = 6
        print(f"You have {round_score} unbanked points and {dice_count} dice remaining")
        choice = players_choice_rbq()
        if choice == "b":
            total_score += round_score
            print(f"You banked {round_score} points in round {round_number}")
            print(f"Total score is {total_score} points")
            return round_score, total_score
        elif choice == "q":
            return total_score
        elif choice == "r":
            continue


def check_for_cheater(roll, saved_dice):

    if saved_dice == "q":
        return "q"

    return bool(Counter(saved_dice) - Counter(roll))


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
    print("Enter dice to keep, or (q)uit:")
    player_choice = input_to_tuple(input("> "))
    if player_choice == "q":
        return "q"
    return player_choice


def input_to_tuple(input_string):
    if input_string == "q":
        return "q"
    roll_list = tuple(int(num) for num in input_string if num.isnumeric())
    return tuple(roll_list)


def players_choice_rbq():
    print("(r)oll again, (b)ank your points or (q)uit:")
    player_choice = input("> ")
    return player_choice


def hot_dice(length):
    if length == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # test_three_pairs = GameLogic([(1, 1, 2, 2, 3, 3)])
    # play(test_three_pairs.mock_roller)
    play()

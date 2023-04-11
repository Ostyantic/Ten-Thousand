from game_logic import *

#currently_playing = True
def welcome():
    print("""Welcome to Ten Thousand
    (y)es to play or (n)o to decline""")
    prompt = input("> ")

    if prompt == "n":
        decline()
    else:
        play()


def decline():
        print ("OK. Maybe another time")



def play(roll = GameLogic.roll_dice):
    total_score = 0
    round_number = 1
    banked_dice = []
    dice_rolled = roll
    round_score = 0
    unbanked_points = 0
    round_total = 0


    while round_number <= 20:
        print (f"Starting round {round_number}") #function
        print (f"Rolling { len(dice_rolled(6))} dice...") #goes to dice function
        print (*dice_rolled(6))
        #in process, subject to change
        banked_dice = input_to_tuple(input("""Enter dice to keep, or (q)uit:
        > """))
        if banked_dice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break

        round_score += GameLogic.calculate_score(banked_dice)
        remaining = remaining_dice(banked_dice)
        print (f"You have {GameLogic.calculate_score(banked_dice)} unbanked points and {remaining} dice remaining")
        choice = players_choice_rbq()
        if choice == "b":
            total_score += GameLogic.calculate_score(banked_dice)
            round_score += GameLogic.calculate_score(banked_dice)
            print(f"You banked {round_score} points in round {round_number}")
            round_number += 1
            round_score = 0
            continue
        elif choice == "r":
            round_score += GameLogic.calculate_score(banked_dice)
            # unbanked_points += round_score
            print(f"Rolling {remaining} dice...")
            print(*dice_rolled(remaining))
            new_roll = input_to_tuple(input("""Enter dice to keep, or (q)uit:
                > """))
            updated_banked_dice = banked_dice + new_roll
            round_score += GameLogic.calculate_score(new_roll)
            remaining -= len(new_roll)
            # if remaining 0: potential for further development
            #in this roll, re-rolling the dice, getting a updated_banked_dice tuple to simulate our added points
            #Anthony's code
            #updated_banked_dice = banked_dice + input_to_tuple(input("""Enter dice to keep, or (q)uit:
                # > """))
            ##variable that is tracking unbanked points, their unbanked points, unbanked points, becomes zero
            #can use on all the dice, as well, doesn't be banked, on the user dice, could be passed as an arugement
            # and then added to unbanked points
            #needs to be put in its own function, meaning each
            round_number += 1
            round_score = 0

            print (updated_banked_dice)
            print(f"You have {round_score} unbanked points and {6 - len(updated_banked_dice)} dice remaining")
            # needs to be put in its own function, meaning each
        elif choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break


# def play(roll=GameLogic.roll_dice):
#     total_score = 0
#     round_number = 1
#     banked_dice = []
#     round_score = 0
#     while True:
#         print(f"Starting round {round_number}")
#         dice_rolled = roll(6 - len(banked_dice))
#         print(f"Rolling {len(dice_rolled)} dice...")
#         print(*dice_rolled)
#         banked_dice += input_to_tuple(input("Enter dice to keep, or (q)uit:\n>"))
#         if banked_dice == "q":
#             print(f"Thanks for playing. You earned {total_score} points")
#             break
#         round_score = GameLogic.calculate_score(banked_dice)
#         remaining = remaining_dice(banked_dice)
#         print(f"You have {round_score} unbanked points and {remaining} dice remaining")
#         choice = players_choice_rbq()
#         if choice == "b":
#             total_score += round_score
#             print(f"You banked {round_score} points in round {round_number}")
#             banked_dice = []
#             round_score = 0
#             round_number += 1
#             continue
#         elif choice == "r":
#             continue
#         elif choice == "q":
#             print(f"Thanks for playing. You earned {total_score} points")
#             break


#would it turn into the integer, or 111, iterate over a string and convert each character into a list
# and return the tuple, push them into a list, pass the list as an argument
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
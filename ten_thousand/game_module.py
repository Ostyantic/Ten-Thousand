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
            print(f"Rolling {remaining} dice...")
            print(*dice_rolled(remaining))
            # if remaining 0: potential for further development
            #in this roll, re-rolling the dice, getting a updated_banked_dice tuple to simulate our added points
            updated_banked_dice = banked_dice + input_to_tuple(input("""Enter dice to keep, or (q)uit:
                > """))
            print (updated_banked_dice)
        elif choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break



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


play()
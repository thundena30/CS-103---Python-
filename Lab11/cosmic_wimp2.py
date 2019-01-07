# Pratyusha Thundena
# December 1, 2017
# Collaborated with Matt Campbell and Stack Overflow


# imports all functions from module called random
from random import *

# defined the function greeting
def greeting():
    """ To welcome the player to the dice rolling game.
    Test data:
    input: N/A
    output: Welcome to the modified version of Cosmic Wimpout, player!
    Params: N/A
    returns: greeting (string)
    """

    # displays the greeting to the user
    print("Welcome to the modified version of Cosmic Wimpout, player!")
greeting()

# defined the function options
def options():
    """ To provide the player with the option to either continue playing the game (when applicable) or to quit.
    Test data:
    input: y or n
    output: N/A
    Params: N/A
    returns: dice rolls if input was y (integers)
    """
    # allows user to input y or n
    again = input('Do you want to roll again(y or n)? ')
    return again == 'y'    # returns True if player want's to roll again


# defined the function dice roll
def diceRoll(n):
    """ To get the player to roll the dice during his or her turn, to tally the points, and to display the score to the player. "
    Test data:
    input: N/A
    output: The special die rolled: ; Points in this turn: ; Total points so far: ;
    Params: n (integer)
    returns: any special die rolled (integer);  points from each turn (integer) ; total points accumulated so far in the game (integer)
    """
    total_points = 0
    for i in range(0, n):
        turn_points = 0
        while True:
            points = []
            rollList = []
            # iterates through a range of values
            for i in range(5):
                rollList.append(randint(1, 6))
            print(rollList)

            specialdie = rollList[0]
            # displays the special die rolled
            print("The special die rolled: ", specialdie)
            if specialdie == 3:
                if rollList.count(1) == 2:
                    points.append(100)
                elif rollList.count(2) == 2:
                    points.append(20)
                elif rollList.count(3) == 2:
                    points.append(30)
                elif rollList.count(4) == 2:
                    points.append(40)
                elif rollList.count(5) == 2:
                    points.append(50)
                elif rollList.count(6) == 2:
                    points.append(60)
                else:
                    points.append(5)

            if specialdie != 3:
                # if all five dice are ones, then the player automatically loses the game
                if rollList.count(1) == 5:
                    print("You've lost!")
                    return
                # if all five dice are six, then the player automatically wins the game
                if rollList.count(6) == 5:
                    print("You've won the game!")
                    return
                # if three 1's, then rewarded 100 points
                elif rollList.count(1) == 3:
                    points.append(100)
                elif rollList.count(2) == 3:
                    points.append(20)
                elif rollList.count(3) == 3:
                    points.append(30)
                # if three 4's, then rewarded 40 points
                elif rollList.count(4) == 3:
                    points.append(40)
                elif rollList.count(5) == 3:
                    points.append(50)
                elif rollList.count(6) == 3:
                    points.append(60)
                else:

                    for num in rollList:
                    # if you don't score the above, each die that comes up 5, you get 5 points
                        if num == 5:
                            points.append(5)
                    # if you don't score the aboce, each die that comes up 1, you get 10 points
                        if num == 1:
                            points.append(10)
            # points per turn
            a = sum(points)
            # total points accumulated
            total_points += a
            print('Points in this turn: ' + str(a))
            print('Total points so far: ' + str(total_points))
            if a == 0:
                print("Your turn has ended!")
                print("Your total points were", str(total_points))
                break


            roll_again = options()
            if not roll_again:
                break
        if not roll_again:
            break


greeting()
diceRoll(1000)
# Pratyusha Thundena
# December 1, 2017
# Collaborated with Matt Campbell


from random import *




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
            for i in range(5):
                rollList.append(randint(1, 6))
            print(rollList)

            specialdie = rollList[0]
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

                if rollList.count(1) == 5:
                    print("You've lost!")
                    return
                if rollList.count(6) == 5:
                    print("You've won the game!")
                    return
                elif rollList.count(1) == 3:
                    points.append(100)
                elif rollList.count(2) == 3:
                    points.append(20)
                elif rollList.count(3) == 3:
                    points.append(30)
                elif rollList.count(4) == 3:
                    points.append(40)
                elif rollList.count(5) == 3:
                    points.append(50)
                elif rollList.count(6) == 3:
                    points.append(60)
                else:
                    for num in rollList:
                        if num == 5:
                            points.append(5)
                        if num == 1:
                            points.append(10)

            a = sum(points)

            total_points += a
            print('Points in this turn: ' + str(a))
            print('Total points so far: ' + str(total_points))
            if a == 0:
                print("Your turn has ended!")
                print("Your total points were", str(total_points))

diceRoll(1000)

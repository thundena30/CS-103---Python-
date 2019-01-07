import random

def greeting():
    print("Welcome to the game, player!")
    print("What ")
greeting()

def RollDie(sides):
    r = random.randrange(1, sides + 1)
    return r

def is_count(a, num, count):
    return a.count(num) == count

def five_twos(a):
    return is_count(a, 2, 5)

def five_sixes(a):
    if is_count(a, 6, 5):
        print("You've won the game.Congrats!!!!")
        return True
    return False

def five_ones(a):
    if is_count(a, 1, 5):
        print("You've lost the game. Sorry!")
        return True
    return False


def five_fours(a):
    return is_count(a, 4, 5)

def five_fives(a):
    return is_count(a, 5, 5)

def three_twos(a):
    return is_count(a, 2, 3)

def three_fives(a):
    return is_count(a, 5, 3)

def three_threes(a):
    return is_count(a, 3, 3)

def three_sixes(a):
    return is_count(a, 6, 3)

def three_fours(a):
    return is_count(a, 4, 3)

def three_ones(a):
    return is_count(a, 1, 2)
#modified function
def func(a):
    points = 0
    for i in a:
        #checks if  roll is 5, adds 5 to points
        if i is 5:
            points = points + 5
        # checks if  roll is 1,adds 10 to points
        if i is 1:
            points = points + 10
    return points

# dice should be rolled and then checked all conditions rather than rolling in each function
# rolling 5 dice and storing the result in array a
a = [RollDie(6) for i in range(0,5)]
print(a)
if not five_sixes(a):
    if not five_ones(a):
        points = 0
        if five_twos(a):
            points = 200
        elif five_fours(a):
            points = 400
        elif five_fives(a):
            points = 500
        elif three_twos(a):
            points = 20
        elif three_fives(a):
            points = 50
        elif three_threes(a):
            points = 30
        elif three_sixes(a):
            points = 60
        elif three_fours(a):
            points = 40
        elif three_ones(a):
            points = 100
        else: points = func(a)

        print("you have gained " + str(points) + " points")



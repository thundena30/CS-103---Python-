
# Pratyusha Thundena
# October 27,2017
# Collaborated with Matt Campbell


def fib():
    """ To create a program that determines Fibonacci numbers by iteration; specifically, using dictionary keys: 0 and 1
    Test data:
    input:
    output: 0:0, 1:1, ....., 50: 12586269025
    Params:
    Returns: Fibonacci sequence for term numbers 0 to 50 in dictionary(integer)
    """

    # dictonary named numbers is declared
    numbers = {}
    # First key, value inserted which are 0,0
    numbers[0] = 0
    # Second key, value inserted which are 1,1
    numbers[1] = 1

    for i in range(2,51):
        numbers[i]= numbers.get(i-1) + numbers.get(i-2)
        # incrementing the count
        i += 1
    # Printing the items of the numbers dictionay as key and values
    for key,value in numbers.items():
        print(str(key ) + ":" +  str(value))

# call function fib
fib()


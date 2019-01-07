# Pratyusha THundena
# November 9, 2017

# dict subclass that remembers the order entries that were added
from collections import OrderedDict

def write_roman(num):
    """ To create an ordered dictionary that converts given integer to its Roman numeral equivalent
    Test data:
    input: N/A
    output: N/A
    Params: num(integer)
    return: N/A
    """
    # iterate downwards the list
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        """ To convert the given integer from the main method to its Roman numeral equivalent
        Test data:
        input: N/A
        output: N/A
        Params: num(integer)
        return: Roman numeral equivalent(string)
        """
        for r in roman.keys():
            # generate matches using recursion
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if (num > 0):
                roman_num(num)
            else:
                break
    # generates a text string
    return("".join([a for a in roman_num(num)]))

def main():
    """ To allow user to enter input, to determine if input is valid, and to call other functions that convert integer to
    its Roman numeral equivalent, and to display the output
    Test data:
    input: 99, 1000, 50, 102, 335, 40, 9, 11
    output: XCIX, M, L, CII, CCCXXXV, XL, IX, XI
    Params: N/A
    return: Roman numeral equivalent(string)
    """
    while True:
    # allows user to enter number into keyboard
        num = input('Enter a number: ')
        try:
            num = int(num)
            print(write_roman(num))
        # if user enters invalid data then the try block is skipped and except clause is executed
        except:
            print('Enter valid data')
        ch = input("Do you want to try more numbers(y/n)?")
        if(ch == 'y' or ch == 'Y'):
            continue
        else:
            break
main()




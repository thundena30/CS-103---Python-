# Pratyusha Thundena
# September 11, 2017
# Objective: To determine if an integer(x) is an even number
# Collaborated with Matt Campbell

def even():
    """ Determine if integer(x) is an even number
       Test data:
       input: 64
       output: The number is even.
       Params: (int) integer
       Returns: (string) "number is even"
       """
    x = int(input("Enter a whole number to determine if it is even. "))
    if x % 2 == 0:
        return (" The number is even. ")
    else:
        return("The number is odd. ")
print (even())



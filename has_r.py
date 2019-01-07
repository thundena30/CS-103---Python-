# Pratyusha Thundena
# September 11, 2017
# Objective: To determine if the string contains a lowercase r or uppercase R

def first(s):
    """ To determine if a string contains a lowercase or uppercase r
    Test data:
    input: 'garden'
    output: The string contains a lowercase r
    Params: s(string)
    Returns: (string)"contains lowercase r "
    """
    for c in s:
        if (c == 'r'):
            return("The string contains a lowercase r")
        elif (c == 'R'):
            return ("The string contains a uppercase R")


print(first("garden"))


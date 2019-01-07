# Pratyusha Thundena
# October 19, 2017
# Collaborated with Matt Campbell



def fib(n):
    """
    To create a program that includes a recursive function that finds and displays Fibonacci numbers from 1 to 50
    Test Data:
    input: whole number
    output: list of fibonacci numbers for the value entered by the user
    params: integer(int)
    returns: fibonacci numbers(int)
    """
    if(n <= 1): #if n is less than or equals to 1 print n
        return n
    return(fib(n-1) + fib(n-2)) #call two recursive calls one as n-1 and other as n-2


for i in range(1, 53): #iteratives i value from 1 to 11
    print(fib(i)) #prints the return type of function by sending parameter as i




1
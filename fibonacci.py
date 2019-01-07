



def fib(n):


    if(n <= 1): #writing the if statement with variable n less or equal to 1

        return n # returns n value after satisfying the n value

    return(fib(n-1) + fib(n-2)) #Now performing two recursive calls


for i in range (1,51) : # performing iteration between 1 to 50 

    print(fib(i)) # prints the return type of function by sending parameter as i



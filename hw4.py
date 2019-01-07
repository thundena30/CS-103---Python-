# Pratyusha Thundena
# November 13,2017
# Collaborated with Matt Campbell 


def decToBin(num):
    # creates an empty list
    binary = []

    while (num > 0):
        a = int(float(num % 2))
        # modifies the binary list
        binary.append(a)
        # takes a decimal number and repeatedly divides it by 2
        num = (num - a) / 2
    binary.append(0)
    string = ""

    for j in binary[::-1]:
        # creates binary text string
        string = string + str(j)
        # Sufficient zeroes pre-fixed to the front of binary string
    return(string.zfill(8))


def binToDec(binary):
    decimal = 0
    # creates a loop that converts the binary string to decimal number
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return (decimal)


def binAdd():
    a = input("What is your first binary string? ")
    b = input("What is your second binary string? ")
    # adds 2 binary strings
    c = (binToDec(a)) + (binToDec(b))
    # returns the total addition of 2 binary strings
    return (decToBin(c))


def binSub():
    # prompts user to enter the first binary string
    a = input("What is your first binary string? ")
    b = input("What is your second binary string? ")
    # subtracts 2 binary strings
    c = (binToDec(a)) - (binToDec(b))

    return (decToBin(c))

# Provides 5 different options that the user can choose
print("Option 1: Convert a decimal number to binary\n")
print("Option 2: Add two binary strings\n")
print("Option 3: Subtract two binary strings\n")
print("Option 4: Exit\n")
print("Option 5: Convert a binary number to decimal\n")
k = int(input("What would you like to do ? "))


if k == 1:
    print(decToBin(int(input("What is your number? "))))
elif k == 2:
    print(binAdd())
elif k == 3:
    print(binSub())
elif k == 4:
    quit()
elif k == 5:
    # prompts user for binary number that has to be later converted to decimal number
    print(binToDec(input("What is your binary number? ")))
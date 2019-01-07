def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        t = b
        b = a % t
        a = t
    return a


def read_file():
    w = open('GCD_result.txt', 'a')
    myfile = open("GCD.txt")
    mytxt = myfile.readline()
    while mytxt:
        line = mytxt.split()
        a=int(line[0])
        b=int(line[1])
        w.write("GCD of "+str(a)+" and "+str(b)+" is "+str(gcd(a,b)) + ".\n")
        mytxt = myfile.readline()
    myfile.close()
    w.close()

while True:
    print("Option 1: Read from a file")
    print("Option 2: Input information onto the keyboard")
    k = int(input("What would you like to do? "))
    if k == 2:
        print("What is your 2 numbers that you would like to find the Greatest Common Divisor for? ")
        i = int(input())
        j = int(input())
        print("The Greatest Common Divisor(GCD) for your input is", gcd(i, j))

        w = open('gcdR.txt', 'a')
        w.write("GCD of "+str(i)+" and "+str(j)+" is "+str(gcd(i,j)) + ".\n")
        w.close()
    elif k == 1:
        read_file()
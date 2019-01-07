
# Pratyusha Thundena
# October 26,2017

def heartRate():
    """ To create a program that calculates target heart rates after taking person's age and resting heart rate into account
        Test data:
        input: Pratyusha, 24, 65
        output: Pratyusha, for your age: 24 , Resting heart rate:  65, Your target heart rate is  150-176 beats per minute.
        Params: Person's name (string), age (integer), resting heart rate(integer)
        Returns: Person's name(string), age (integer), resting heart rate (integer) , target heart rate(integer)
    """
    # First get input from the user
    name = input("Enter your name: ")
    age= int(input("Enter your age: "))
    restHR = int(input("Enter your resting heart rate: "))

    # Maximum heart rate
    max_HR = 220 - age


    # Low range
    low = int((max_HR - restHR)*.65) + restHR

    # High range
    high = int(( max_HR - restHR)* .85) + restHR

    # Print response
    print(str(name) +', for your age: ' + str(age))
    print("Resting heart rate: " + str(restHR))
    print("Your target heart rate is " + str(low) + " to "+ str(high) + " beats per minute.")


    # Create and open a file in write mode

    outputFile = open("HEARTRATE.txt","w")

    # Write the response to the file

    outputFile.write(str(name) + ', for your age: ' + str(age))

    outputFile.write("\nResting heart rate: " + str(restHR))

    outputFile.write("\nYour target heart rate is " + str(low) + " to " + str(high) + " beats per minute.")

    # Close the file

    outputFile.close()

    print("\nOutput written to hearRate.txt")

heartRate()



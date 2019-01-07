def int_to_roman():
    '''
    convert integer to roman numeral
    Test data: (int)1500
    Input: (integer)1500
    Output: (str)MD
    Returns: the roman numeral(string) that represents the given integer
    '''
    number = integer #scoping
    roman_List = [['M',1000], ['D',500], ['C',100], ['L',50], ['X',10], ['V',5], ['I',1],] #list of lists
    answer = [] #empty list
    for letter, value in roman_List:
        while value <= number: #closest value to the number from list
            number = number - value #subtract  number from value to find remainder
            answer.append(letter)#adds both the closest value and remainder to new list
            
    return( ''.join(answer))#join the list of letters to one word

while True:
    try:
        integer = int(input('Enter an integer: '))
    except:
        print('Goodbye!')
        break
    if integer < 0:
        print('\n','Error! Enter positive integers between 1 and 1000!')
    print(int_to_roman())
        
        
#respond elegantly to cause the user to only enter valid data

#demonstrate its operation with at least three sets of valid coefficients input,\
#plus as many additional test cases as you need

#IF NEGATIVE input
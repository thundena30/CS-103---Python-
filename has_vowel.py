# Pratyusha Thundena
# September 11, 2017
# Objective: To determine if the string contains a vowel

def vowel(z):
    """ To determine if a string contains a vowel: a, e, i, o, u, or y
    Test data:
    input: 'garden'
    output: Given string garden contains any one of the characters: a,e,i,o,u,y
    Params: s(string)
    Returns: (string)" contains any one of the characters:a,e,i,o,u,y"
    """
str = "garden"
found = False
for i in range(len(str)):
    if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'y':
        found = True
        break
if found:
    print("Given string",str,"contains any one of the characters: a,e,i,o,u,y")
else:
    print("Given string",str,"contains none of the characters: a,e,i,o,u,y")






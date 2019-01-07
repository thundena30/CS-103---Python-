def word2capitalize(string):
    if not {'and','not','the'}:
        return sentence.ustrip()


myList = [word[0].upper() + word[1:] for word in string.split()]
string = " ".join(myList)
return string

s = input("Type in any string: ")
sen = word2capitalize(s)
print(sen)

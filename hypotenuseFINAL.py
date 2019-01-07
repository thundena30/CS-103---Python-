def hypotenuse(a, b):
    
    """TEST DATA:
       INPUT:
       OUTPUT:
       PARAMS: a, b
       RETURNS: Hypotenuse of two sides
    """

    final = (a**2 + b**2)**(1/2)

    return(final)


inputvalues = open('valuestoread', 'r')
f = open('hypotenuses', 'w')

for i in inputvalues:
    
    a, b = map(int, i.split(' '))
    c = str(hypotenuse(a, b))
    print("Your sides are", a ,"and", b ,"and your hypotenuse is", hypotenuse(a, b) ,"\n")
    f.write("Your sides are " + str(a) + " and " + str(b) + " and your hypotenuse is " + c + "\n")
                 
inputvalues.close()
f.close()










    


    





    




    









    








    

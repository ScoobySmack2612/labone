from time import sleep
result = ''
def adder():
    global result 
    in1 = input("enter your first value: ")
    in2 = input("enter your second value: ")
    if type(in1) == type(in2) and type(in1) and type(in2) == int:
        result = "Result of adding your integers is: %s" % (in1 + in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == float:
        result = "Result of adding your floats is: %s" % (in1 +in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == str:
        result = "Result of adding your strings is: %s" % (in1 +in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == tuple:
        result = "Result of adding your tuples is: %s" % (in1 +in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == list:
        result = "Result of adding your lists is: %s" % (in1 +in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == bool:
        result = "Result of adding your boolean logic operators is: %s" % (in1+in2)
    else:
        result = "ERROR: YOUR INPUTS NEED TO BE OF SAME TYPE. PLEASE TRY AGAIN WHEN NO LONGER INEBRIATED"
    return result

repeat = True
while repeat == True:

    adder()

    print "Calculating..."
    sleep (1)
    print result
    again = "would you like to play again?(1 for yes, 0 for no)"
    print again
    answer = input()
    if answer == 1:
        repeat = True
    else:
        quit()
    


    

    

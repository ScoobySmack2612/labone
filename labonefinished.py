from time import sleep
result = ''

def combiner(operation):
    global result
    print "you've chosen to engage the %ser" % (operation)
    sleep(1)
    in1 = input("enter your first value: ")
    in2 = input("enter your second value: ")
    if type(in1) == type(in2) and type(in1) and type(in2) == int:
        if operation == "add":
            result = "Result of adding your integers is: %s" % (in1 + in2)
        else:
            result = "Result of subtracting your integers is: %s" % (in1 - in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == float:
        if operation == "add":
            result = "Result of adding your floats is: %s" % (in1 + in2)
        else:
            result = "Result of subtracting your floats is: %s" % (in1 - in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == str:
        if operation == "add":
            result = "Result of adding your strings is: %s" % (in1 + in2)
        else:
            result = "Result of subtracting your strings is: %s" % (in1 - in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == tuple:
        if operation == "add":
            result = "Result of adding your tuples is: %s" % (in1 + in2)
        else:
            result = "Result of subtracting your tuples is: %s" % (in1 - in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == list:
        if operation == "add":
            result = "Result of adding your lists is: %s" % (in1 + in2)
        else:
            result = "Result of subtracting your lists is: %s" % (in1 - in2)
    elif type(in1) == type(in2) and type(in1) and type(in2) == bool:
        if operation == "add":
            result = "Result of adding your boolean values is: %s" % (in1 + in2)
        else:
            result = "Result of subtracting your boolean values is: %s" % (in1 - in2)
    else:
        result = "ERROR: YOUR INPUTS NEED TO BE OF SAME TYPE. PLEASE TRY AGAIN WHEN NO LONGER INEBRIATED"
    return result

repeat = True
operator = "What oporator would you like to add or subtract?"
again = "would you like to play again?(1 for yes, 0 for no)"
while repeat == True:
    print operator
    answer = input("Please put your answer in quotations: ")
    combiner(answer)

    print "Calculating..."
    sleep (.75)
    print result

    print again
    answer = input()
    if answer == 1:
        repeat = True
    else:
        quit()
    


    

    

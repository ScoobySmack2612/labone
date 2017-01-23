from time import sleep

def start_up():
    operationText = "Welcome to the data type adder"
    operation = raw_input("What operation would you like to perform? You may add or subtract: ")
    return(operation)
def op_validity(operation):
    if operation == "add" or operation == "Add" or operation == "subtract" or operation == "Subtract":
        op_check = "pass"
        return op_check
    else:
        op_check = "failed"
        return op_check
def inputs_and_check():
    in1 = input("Please enter first value: ")
    in2 = input("Please enter second value: ")
    if type(in1) != type(in2):
        print "FAILED"
        again = start_up()
    else:
        in1, in2 = in1, in2
        return in1, in2
    if in1 == "" or in2 == "":
        print "blank"
    else:
        pass
    
def op_add(in1,in2):
    if type(in1) and type(in2) == int:
        result = (in1 + in2)
        return result
    elif type(in1) and type(in2) == float:
        result = (in1 + in2)
        return result
    elif type(in1) and type(in2) == str:
        result = (in1 + in2)
        return result
    elif type(in1) and type(in2) == tuple:
        result = (in1 + in2)
        return result
    elif type(in1) and type(in2) == list:
        result = (in1 + in2)
        return result
    elif type(in1) and type(in2) == bool:
        result = (in1 and in2)
        return result
    else:
        print "There was an error, Please try again"
        operation=start_up()

        return result
def op_sub(in1,in2):
    if type(in1) and type(in2) == int:
        result = (in1 - in2)
        return result
    if type(in1) and type(in2) == float:
        result = (in1 - in2)
        return result
    if type(in1) and type(in2) == str:
        result = "Error, can not subtract strings"
        return result
    if type(in1) and type(in2) == tuple:
        result = "Error, can not subtract tuples"
        return result
    if type(in1) and type(in2) == list:
        result = "Error, can not subtract lists"
        return result
    if type(in1) and type(in2) == bool:
        result = "Error, can not subtract boolean values"
        return result

def result_checker(result,in1):
    if type(result) == type(in1):
        result_check = "pass"
        return result_check
    else:
        result_check = "fail"
        return result_check

def restart():
    restartMsg = "would you like to play again?: yes or no?"
    answer = raw_input(restartMsg + ":")
    if answer == "yes":
        again = True
        return again
    elif answer == "no":
        again = False
        return again
    else:
        print "Sorry I didn't catch that. Try again."

run = True
welcome = "Welcome to my adder"

print welcome
sleep(1)
print
while run:
    operation = start_up()
    op_check = op_validity(operation)


    if op_check == "pass":
        in1, in2 = inputs_and_check()
    elif op_check == "failed":
        print "Unsupported operation type"
        continue
    

    if operation == "add":
        result = op_add(in1,in2)
    elif operation == "subtract" or "Subtract":
        result = op_sub(in1,in2)
    else:
        print "sorry something went wrong"
    
    result_check = result_checker(result, in1)

    print "Calculating..."
    sleep (1)
    print

    if result_check == "pass":
        resultMsg = "The result of %sing your inputs is: %s" %(operation,result)
        print resultMsg
        print
    else:
        print "sucky huge bug"
    again = restart()
    if again == True:
        pass
    else:
        run = False
quit()


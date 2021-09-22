from sys import argv

script, first, second, third = argv
#receive arguments from command line
if(first.isdigit() and third.isdigit()):
    if(second == "+" or second == "-" or second == "*"):
        print("Result is:", eval(first+second+third))
    elif (second == "/" and third =="0"):
        print("Division by zero")
    else:
        print(eval(first+second+third))
        
    
else:
    print("Error")
#sum string and convert them to int and count result

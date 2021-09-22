from sys import argv

script, first, second, third = argv
#receive arguments from command line
if(second.isdigit() and third.isdigit()):
    if first=="add":
            print("Result is:", int(second)+int(third))
    elif first=="mul":
            print("Result is:", int(second)*int(third))
    
    elif first=="sub" :
            print("Result is:", int(second)-int(third))
    
    elif first=="div":
        if third=="0":
            print("division by zero")
        else:
            print(" Result is:", int(second)/int(third))
    else:
        print("Unknown function")
else:
    print("No numbers!")

#chech what operation we need and make an operation between received arguments

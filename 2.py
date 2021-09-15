from sys import argv

script, first, second, third = argv
#receive arguments from command line


if(first=="add"):
    print("Result is:", int(second)+int(third))
    
if(first=="mul"):
    print("Result is:", int(second)*int(third))
    
if(first=="sub"):
    print("Result is:", int(second)-int(third))
    
if(first=="div"):
    print("Result is:", int(second)/int(third))
#chech what operation we need and make an operation between received arguments

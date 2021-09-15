from sys import argv

script, first = argv
#receive arguments from command line

def check(first):
    """
    This function check logic formula and if this logic formula is right,
    this function calls another function "solving". If a logic formula is wrong,
    it shows that
    """
    str = first
    for i in range(len(first)+1):
        if(len(first)==0):
    #at the start of every iteration, we check whether out logic formula finished, and if
    #formula is finished, we call a function which count a result of logic formula
            print("True")
            solving(str)
            break
        elif(first[0]=="+" or first[0]=="-" or first[0]=="*" or first[0]=="/"):
            if(first[1]=="+" or first[1]=="-" or first[1]=="*" or first[1]=="/"):
    #this block check whether logic formula has a repetitive logical operators, and if
    # it exists, break for loop
                print("False, None")
                break
            else:
    #if repetitive logical operator doesnt exist, we remove first element of our string
                first = first[1:]      
        elif(first[0].isdigit()):
    #if first element of our string is digit, we remove first element of our string
    #in other way, break the loop
            first = first[1:]
        else:
    
            print("False, None")
            break

           
def solving(first):
    """
    This function print result of logic formula 
    """
    print (eval(first))
    
    


check(first)






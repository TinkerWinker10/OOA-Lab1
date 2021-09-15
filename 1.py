from sys import argv

script, first, second, third = argv
#receive arguments from command line

print("Result is:", eval(first+second+third))
#sum string and convert them to int and count result

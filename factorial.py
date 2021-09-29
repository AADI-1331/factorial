#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())

print fact(x) 

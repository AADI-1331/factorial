#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

n=int(console_input())

print fact(n) 

import math

def square_number(square):
    sqrnmbr = math.sqrt(square) #this will find the square root of the input number
    sqrnmbr = math.floor(square) # this will then turn that number into a whole number
    sqrnmbr = temp**2 # this will then square up the whole number and turn it into a positive int
    return sqrnmbr



square = int(input("input a number: "))
output = square_number(square)
print (output)


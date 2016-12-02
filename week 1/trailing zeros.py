#Trailing Zeros
import math

def Trailing_Zeros(numbers): 
    zeros_count = 0
    
    while(numbers%10==0):
        numbers = numbers/10
        zeros_count = zeros_count+1
       

    return zeros_count


numbers =  int(input ("please enter a number between 1 and 20: "))
product = 1
for i in range(1,numbers+1):
    product = product * i
print(product)
t = Trailing_Zeros(product)
print (t)


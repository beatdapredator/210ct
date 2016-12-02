def is_prime(number,t=3):
    if number == 0:
        result = False
    elif number == 2:
        result = True
    elif number <= 1 or number % 2 == 0:
        result = False
    elif t*t > number:
        result = True
    elif number % t == 0:
        result = False

    else:
        return is_prime(number,t+2)

    return result

while True:
    
    number = int(input("please enter a number to check if it is prime: "))
    t = 3
    output = is_prime(number)
    print (output)

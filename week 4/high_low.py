def high_low(arr,high,low):
    left = 0
    right = int(len(arr))
    while left <= right:
        middle = int((left + right)/2)
        if arr[middle] <= high and arr[middle] >= low:
            return True
        elif arr[middle] > high:
            right = middle - 1
        elif arr[middle] < low:
            left = middle + 1
    return False

thelist = []
for i in range (30):
    thelist.append(i*3)

a = int(input("please enter a low number: "))
b = int(input("please enter a high number: "))
j = high_low(thelist,b,a)
print(j)



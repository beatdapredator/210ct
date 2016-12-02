mylist = [6,7,5,7,6,5,3,5,3,3,6,4,3,6,5,7,5,34,3,5,7,2,9]

start = 0
largest = 0
i = 0

for i in range (len(mylist)):
    count = 1
    for j in range (i+1,len(mylist),1): # i know that using a nested loop is not the most effcient way to do this but it is easier for me to read
        if mylist[j] <= mylist[j-1]:
            break
        else:
            count+=1

    if count>largest:
        largest=count
        start = i


print ("my string starts at: ",start,"the length of my sequence is: ",largest)
print (mylist[start:start+largest])



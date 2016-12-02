import random
 
 
def shuffle(mylist):
    new_list = []
    while len(mylist) > 0:
        change = random.randrange(len(mylist))
        new_list.append(mylist[change])
        mylist.remove(mylist[change])
    return new_list
 
mylist = [5,3,8,6,1,9,2,7]
print(mylist)
x = shuffle(mylist)
print(x)

def reverse(words):
    split = words.split(" ") # this will split up the elements when there is a space
    output = ""

    for i in range(len(split)):
        j = len(split)-i-1 # this will go back on position in the list and will find the last element
        output = output + split[j] + " " # will then put the sentence in order of last element and go backwards
    return output

y = reverse( input("enter a sentence: "))
print (y)


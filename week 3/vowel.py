def vowel_remove(s):
    if not s:
        return s
    elif s[0].lower() in "aeiou":
        return vowel_remove(s[1:])
    return s[0] + vowel_remove(s[1:])

s = input("please enter a word with vowels: ")
print(vowel_remove(s))
        

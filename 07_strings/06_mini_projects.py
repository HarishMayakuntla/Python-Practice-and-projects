
## ================ Check Palindrome ===========

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



## =================== Count Vowels and Consonants ===================

text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)


## ============================  Anagram ================

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")
else:
    print("Not Anagram")
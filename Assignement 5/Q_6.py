# Program to check if a string has at least one vowel


string = input("Enter a string: ")


vowels = "aeiouAEIOU"


has_vowel = False


for ch in string:
    if ch in vowels:
        has_vowel = True
        break 


if has_vowel:
    print("The string has at least one vowel.")
else:
    print("The string does not contain any vowel.")

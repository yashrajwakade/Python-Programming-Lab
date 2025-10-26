# Program to print the first two characters of every word in a string


sentence = input("Enter a sentence: ")


words = sentence.split()


for word in words:
    if len(word) >= 2:
        print(word[:2])  
    else:
        print(word)  

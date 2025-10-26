# Program to check if a given character is present in a string or not
# and print its index or count of occurrences (without built-in functions)


string = input("Enter a string: ")
char = input("Enter a character to search: ")

found = False      
count = 0          
indexes = []       


for i in range(len(string)):
    if string[i] == char:
        found = True
        count += 1
        indexes.append(i)


if not found:
    print("Character not found in the string.")
else:
    if count == 1:
        print(f"Character '{char}' found at index {indexes[0]}")
    else:
        print(f"Character '{char}' occurs {count} times at indexes {indexes}")

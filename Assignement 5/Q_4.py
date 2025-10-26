# Program to create a new string made up of 4 copies 
# of the last 2 characters of a specified string


string = input("Enter a string: ")


if len(string) < 2:
    print("String length must be at least 2.")
else:
    last_two = string[-2:]         
    new_string = last_two * 4      
    print("New string:", new_string)

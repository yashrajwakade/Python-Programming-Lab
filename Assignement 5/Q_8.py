import re

# Program to match a string that starts with digits followed by a space and then characters


text = input("Enter a string: ")


pattern = r'^[0-9]+ [A-Za-z].*'


if re.match(pattern, text):
    print("✅ The string matches the pattern.")
else:
    print("❌ The string does NOT match the pattern.")

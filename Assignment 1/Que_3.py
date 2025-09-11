s = "The lyrics is not that poor!!"


not_index = -1
poor_index = -1

for i in range(len(s) - 2):
    if s[i:i+3] == "not":
        not_index = i
        break

for i in range(len(s) - 3):
    if s[i:i+4] == "poor":
        poor_index = i
        break


if not_index != -1 and poor_index != -1 and poor_index > not_index:
    new_str = s[:not_index] + "good" + s[poor_index+4:]
else:
    new_str = s

print("Result:", new_str)

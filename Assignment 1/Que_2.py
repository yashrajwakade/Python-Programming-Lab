s = "restart"
first = s[0]
result = first

for i in range(1, len(s)):
    if s[i] == first:
        result += "S"
    else:
        result += s[i]

print("Modified String:", result)

data = {"a": 5, "b": 1, "c": 9, "d": 3}

items = []
for k in data:
    items.append((k, data[k]))


for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] > items[j+1][1]:
            temp = items[j]
            items[j] = items[j+1]
            items[j+1] = temp

sorted_dict = {}
for k, v in items:
    sorted_dict[k] = v

print("Sorted Dictionary:", sorted_dict)

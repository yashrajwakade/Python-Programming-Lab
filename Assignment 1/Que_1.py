
data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j][1] > data[j + 1][1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

print("Sorted List:", data)

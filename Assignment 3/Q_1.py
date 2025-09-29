
primes = []
for num in range(2, 100):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)


n = len(primes)  # total primes
size = 1
while size * size < n:
    size += 1


spiral = [[0 for _ in range(size)] for _ in range(size)]


top, left = 0, 0
bottom, right = size - 1, size - 1
index = 0

while top <= bottom and left <= right and index < n:
    for j in range(left, right + 1):
        if index < n:
            spiral[top][j] = primes[index]
            index += 1
    top += 1
    for i in range(top, bottom + 1):
        if index < n:
            spiral[i][right] = primes[index]
            index += 1
    right -= 1
    for j in range(right, left - 1, -1):
        if index < n:
            spiral[bottom][j] = primes[index]
            index += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        if index < n:
            spiral[i][left] = primes[index]
            index += 1
    left += 1


for row in spiral:
    for val in row:
        if val != 0:
            print(f"{val:3}", end=" ")
        else:
            print("   ", end=" ")
    print()

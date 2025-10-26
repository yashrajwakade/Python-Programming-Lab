n = input("Enter the string : ")

if (len(n)%4 == 0):
    k = n[::-1]
    print(k)

else:
    print("The length of the string is not divisible by 4")
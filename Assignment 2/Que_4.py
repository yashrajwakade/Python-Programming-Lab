# Absolute Value : Write a program to find the absolute value of a given number without using the abs() function.
def get_abs_value(number):
    if number < 0:
        return -number
    else:
        return number

a,b,c = -7,0,32

print(f"The absolute value of {a} is: {get_abs_value(a)}")
print(f"The absolute value of {b} is: {get_abs_value(b)}")
print(f"The absolute value of {c} is: {get_abs_value(c)}")
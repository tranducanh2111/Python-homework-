# ex1:
def areaOfCircle(radius_):
    import math
    area_of_circle = math.pi * (radius_)**2
    return area_of_circle

areaofcircle = areaOfCircle(int(input("Enter a radius here")))
print(areaofcircle)

# ex2:
def reverseString(string):
    string_end= string [::-1]
    return string_end

print(reverseString(input("Nhap một chuỗi vào đây: ")))

# ex3:
def palindrome_check(string):
    reverse_string = string [::-1]
    if reverse_string == string:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
    return

check = palindrome_check(input("Nhap ký tự vào đây"))

# ex4:
def factorial_calculate(integer):
    factorial = 1
    for i in range(1, int(integer) + 1):
        factorial *= i
    return factorial

calculus = factorial_calculate(input("insert a number: "))
print(calculus)

# ex7:
n=int(input("Enter a number here"))
for i in range( 1, n + 1 , 1 ):
    print(i * "*")
for i in range ( n - 1, 0 , -1 ):
    print(i*"*")


# ex8:
i=int(input("Enter a number bigger than 3"))
f1= 0
f2= 1
print(f1)
print(f2)
for f3 in range(2,i):
    f3 = f1 + f2
    print(f3)
    f1 = f2
    f2= f3

# ex9(case1):
number=int(input("Enter a number here"))
for i in range(2,number+1,1):
    while number % i == 0:
        print(i)
        number /= i

# ex9 (case 2):
import math
number=int(input("Enter a number here"))
while number % 2 ==0:
    print(2)
    number/=2
for i in range(3, int(math.sqrt(number)) + 1, 2):
    while number % i == 0:
        print(i)
        number /= i
while number > 1:
    print(int(number))
    number /= number

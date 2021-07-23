# # ex11:
list_a=[1,2,3,4,5,6,7]
max_list_a=1
min_list_a=1
length_list_a=0
sum_list_a=0
for i in range(0, len(list_a)):
    if list_a[i] > max_list_a:
        max_list_a = list_a[i]
    if list_a[i] < min_list_a:
        min_list_a = list_a[i]
    length_list_a += 1
    sum_list_a += list_a[i]
mean_list_a = sum_list_a / length_list_a
print(max_list_a)
print(min_list_a)
print(sum_list_a)
print(length_list_a)
print(mean_list_a)

# # ex12 (case 1):
# a=-1
# b=3
# c=5
# d=2
# e=4
# f=-15
# g=-97
# list_a=[a,b,c,d,e,f,g]
# product=a*b*c*d*e*f*g
# if product < 0:
#     print("-1")
# if product == 0:
#     print("0")
# if product > 0:
#     print("1")

# # ex12 (case 2):
# a=-1
# b=3
# c=5
# d=2
# e=4
# f=-15
# g=-97
# list_a=[a,b,c,d,e,f,g]
# product=1
# for i in range(0, len(list_a)):
#     if list_a[i] < 0:
#         product *= -1
#     if list_a[i] == 0:
#         product *= 0
#     if list_a[i] > 0:
#         product *= 1
# print(product)

# # ex13:
# number=int(input("Enter a number bigger than 1:"))
# for i in range(1, number + 1):
#     if i % 15 == 0:
#         print("FizzBuzz")
#         continue
#     if i % 3 == 0:
#         print("Fizz")
#         continue
#     if i % 5 == 0:
#         print("Buzz")
#         continue
#     else:
#         print(i)

# # ex14(bonus):
# number=int(input("Enter a number here"))
# for i in range (1, number + 1, 1):
#     space= (number - i) * " "
#     i *= "*"
#     print(space+i)

# # ex15(bonus):
# number=int(input("Enter a number here"))
# for i in range(1, number +1):
#     space=(number-i) * " "
#     i *= "* "
#     print(space+i)

# # ex16:
# list_a=[10,7,4,6,8,10,11]
# count_a = 0
# for i in range(0, len(list_a)):
#     if list_a[i] == list_a[i-1] + (i-1)*(list_a[i]-list_a[i-1]):
#         count_a += 1
# print(count_a)

# # ex17:
# list_a=[-7,1,3,5,7, 12, 8, 3, -15, 6, -3, -4]
# list_a.sort()
# max_a = list_a[-1] * list_a[-2]
# max_b = list_a[0] * list_a[1]
# if max_a >= max_b:
#     print(max_a)
# else:
#     print(max_b)

# # ex18:
# for x in range(1, int(input("enter a number:")) + 1):
#     print(int(x*"1")**2)

# #  ex21(case 1):
# list_a=[10,1,2,3,4,5,6,7,8,9,6,8,2,4]
# list_a.sort()
# sum_a=0
# for i in range(0, len(list_a)):
#     if list_a[i] - list_a[i-1] == 0:
#         continue
#     else:
#         sum_a += list_a[i]
# print(sum_a)

# # ex21(case 2):
# list_a=[10,1,2,3,4,5,6,7,8,9,6,8,2,4]
# list_set= list(set(list_a))
# sum_set = 0
# for i in range(0, len(list_set)):
#     sum_set += list_set[i]
# print(sum_set)
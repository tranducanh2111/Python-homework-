def special_sort(lst):
    dct_lst = dict((x,y) for x, y in lst)
    return list(reversed(sorted(dct_lst.items(), key = lambda value: value[1])))
    

lst = [(1,4),(9,2),(3,4),(5,-3),(7,-8),(-9,-5)]
print(special_sort(lst))

# ex24;
def fizz_buzz(num):
    modified_lst = ["Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else x for x in range(1, num + 1)]
    return modified_lst

num = int(input("Enter a number: "))
print(fizz_buzz(num))
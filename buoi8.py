# ex11:
# def sum_of_unique_elements(lst):
#     storage = {}
#     for i in range(len(lst)):
#         key = lst[i]
#         if key in storage:
#             storage[key] += 1
#         else:
#             storage[key] = 1
#     sum = 0
#     for key in storage:
#         if storage[key] == 1:
#             sum += key
#         else:
#             continue
#     return sum

# lst = [1,2,3,1,4,5,3,2,4,6,7,2]
# sum = sum_of_unique_elements(lst)
# print(sum)

# ex22:
# def contains_duplicate(nums):
#     lst = {}
#     for i in range(len(nums)):
#         key = nums[i]
#         if key in lst:
#             lst[key] += 1
#         else:
#             lst[key] = 1
#     duplicate_times = 0
#     for value in lst.values():
#         if value > 1:
#             duplicate_times += 1
#     if duplicate_times == 0:
#         print(False)
#     else:
#         print(True)
#     return

# nums = [1,2,3,4]
# check = contains_duplicate(nums)

# ex21(case 1):
# def number_of_good_pairs(lst):
#     count = 0
#     for i in range(len(lst)):
#         a = lst[i]
#         for j in range(len(lst)):
#             if i == j:
#                 continue
#             b = lst[j]
#             if a == b and i < j:
#                 count += 1
#     return count

# lst = [1,2,3,1,1,3]
# check = number_of_good_pairs(lst)
# print(check)

def number_of_good_pairs(lst):
    count={}
    times = 0 
    for num in range(len(lst)):
        key = lst[num]
        if key in count:
            count[key] += 1
        else:
            count[key] = 1
    for value in count.values():
        if value > 1:
            times += value 
    return times

lst = [1,2,3,1,1,3]
check = number_of_good_pairs(lst)
print(check)
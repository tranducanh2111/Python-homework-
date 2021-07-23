#   ex5:
typed_number=int(input("Enter a number bigger than 10 with 2 or 3 digits only"))
while 100 > typed_number > 10:
    chu_so_thu_1 = (typed_number // 10)
    chu_so_thu_2 = (typed_number - chu_so_thu_1*10)
    print(chu_so_thu_2)
    print(chu_so_thu_1)
    typed_number-=typed_number
while 1000 > typed_number > 100:
    chu_so_thu_1 = (typed_number //100)
    chu_so_thu_2 = ((typed_number - chu_so_thu_1*100)//10)
    chu_so_thu_3 = (typed_number - 100*chu_so_thu_1 - 10*chu_so_thu_2)
    print(chu_so_thu_3)
    print(chu_so_thu_2)
    print(chu_so_thu_1)
    typed_number-=typed_number

    # ex6:
initial_balance = int(input("Enter a your initial balance with 3 digits"))
profit=int(input("Enter the profit you are expecting"))
desired_balance = int(input("Enter your goal"))
while initial_balance < desired_balance and 1000> initial_balance > 99:
    initial_balance = (initial_balance * (1 + profit / 100))
    print(initial_balance)
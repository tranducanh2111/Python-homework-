# 2) code function eval_who_bmi(bmi):
# Return 1 string chỉ trạng thái cơ thể 
# Ví dụ: “cân nặng thấp (gầy)” 
# 3) code function eval_idi_bmi(bmi):
# Return 1 string chỉ trahng thái cơ thể như trên
# Công thức như ảnh trên
# 4) function main sẽ hỏi người dùng kiểu
# Chiều cao của bạn là gì
# Cân nặng của bạn là gì
# Bạn muốn tính bmi theo công thức who hay idi
# Tình trạng cơ thể của bạn là ….

# ex1:
def calc_bmi(weight,height):
    calc_bmi = weight / (height * 2)
    return calc_bmi

# ex2:
def eval_who_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("Healthy weight")
    elif 24.9 < bmi <= 29.9:
        print("Overweight")
    elif 29.9 < bmi <= 34.9:
        print("Obese level 1")
    elif 34.9 < bmi <= 39.9:
        print("Obese level 2")
    else:
        print("Obese level 3")
    return

# ex3:
def eval_idi_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 22.9:
        print("Healthy weight")
    elif 22.9 < bmi <= 24.9:
        print("Overweight")
    elif 24.9 < bmi <= 29.9:
        print("Obese level 1")
    elif 29.9 < bmi <= 34.9:
        print("Obese level 2")
    else:
        print("Obese level 3")
    return

# ex4:
def body_status(height,weight):
    print("Enter your height in meters")
    print("Enter your weight in kilograms")
    height= float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    ask = input("Would you prefer to calculate your BMI by IDI or WHO methodology? ")
    bmi = calc_bmi(weight,height)
    if ask.lower() == "idi":
        result=eval_idi_bmi(bmi)
    elif ask.lower() == "who":
        result = eval_who_bmi(bmi)
    else:
        print("Invalid request")
    return result

height = 0
weight = 0
body_check= body_status(height,weight)

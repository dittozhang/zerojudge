# 判斷是否為質數
# 質數回傳 True
# 否則回傳 False

def Prime(number):
    for i in range(2,int(number ** (1/2))+1):
        if i > 2 and i % 2 == 0:
            continue
        elif i > 3 and i % 3 == 0:
            continue
        elif i > 5 and i % 5 == 0:
            continue
        elif i > 7 and i % 7 == 0:
            continue
        elif number % i == 0:
            return False
    return True

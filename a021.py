# a021 大數運算
# 未完成
from decimal import Decimal

while True:
    try:
        num1, s, num2 = input().split()
        num1, num2 = Decimal(num1), Decimal(num2)
        if s == '+':
            print(num1 + num2)
        elif s == '-':
            print(num1 - num2)
        elif s == '*':  # 不精確
            print(num1 * num2)
        else:
            print(num1 // num2)
    except EOFError:
        break

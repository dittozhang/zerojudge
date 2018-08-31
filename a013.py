# a013 羅馬數字


def Roma2Arab(s):
    roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(s)):
        roma.get(s[i])
        if i == len(s) - 1:
            sum += roma.get(s[i])
            break
        if roma.get(s[i]) < roma.get(s[i+1]):
            sum -= roma.get(s[i])
        else:
            sum += roma.get(s[i])
    return sum


def Arab2Roma(num):
    roma = {4: 'M', 4.5: 'D', 3: 'C', 2: ''}
    romaList = []
    sNum = str(num)
    for index in len(sNum):


while True:
    try:
        num1, num2 = input().split()
        num1, num2 = Roma2Arab(num1), Roma2Arab(num2)
        sum = abs(num1, num2)
        if sum == 0:
            print("ZERO")
        else:
            print(Arab2Roma(sum))

    except (EOFError, ValueError):
        break

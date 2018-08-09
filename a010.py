#zerojudge a010
#因數分解

def Prime(number):  #質數判斷
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

while True:
    try:
        #宣告變數
        Divisors = {}
        s = ''
        num = int(input())

        while True:
            if Prime(num):  #質數則為 True
                if num in Divisors: #判斷 dict 內是否有該值
                    Divisors[num] += 1
                else:
                    Divisors[num] = 1
                break

            for i in range( 2 , num + 1 ):
                if Prime(i) == False:    #非質數則判斷為 True
                    break
                if num % i == 0:
                    num = int(num / i)
                    if i in Divisors:   #判斷 dict 內是否有該鍵
                        Divisors[i] += 1
                    else:
                        Divisors[i] = 1

        for i in Divisors:
            if Divisors[i] == 1:
                s += str(i) + " * "
            else:
                s += str(i) + '^' + str(Divisors[i]) + " * "
        print(s.strip(' * ') + '計算完畢')

    except EOFError:
        break

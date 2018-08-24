#a040 阿姆斯壯數

while True:
    try:
        min , max = input().split() #輸入範圍
        min , max = int(min) , int(max) #將輸入由字串轉換為整數
        numList = []
        numOfArmstrong = 0  #計算取得的 Armstrong number 個數

        for num in range(min, max +1):
            sum = 0
            numList = []

            for s in str(num):  #設定 numList ，儲存所有位數
                numList.append(int(s))

            for j in numList:   #計算
                sum += j ** len(numList)

            if num == sum:  #取得 Armstrong number
                print(num ,end = ' ')
                numOfArmstrong += 1

        if numOfArmstrong == 0:
            print("none")
        else:
            print("") 

    except EOFError:
        break

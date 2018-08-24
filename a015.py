#a015 矩陣的翻轉

while True:
    try:
        row , col = input().split()
        row , col = int(row) , int(col)
        matrixList = [0] * row  #assign list size
        for i in range(len(matrixList)):
            matrixList[i] = input().split()
        row , col = col , row   #Transpose
        for i in range(row):    #print row
            for j in range(col):    #print column
                print(matrixList[j][i],end = ' ')
            print()

    except EOFError:
        break

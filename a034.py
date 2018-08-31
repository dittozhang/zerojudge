# a034 二進位轉換

while True:
    try:
        print(bin(int(input()))[2:])
    except EOFError:
        break

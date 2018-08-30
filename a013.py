#a013
#還沒寫完
import sys

global roma
roma = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }

def Roma2Arab(str):
    global roma
    sum = 0
    for i in range(len(str)):
        roma.get(str[i])
        if i == len(str) -1:
            sum += roma.get(str[i])
            break
        if roma.get(str[i]) < roma.get(str[i+1]):
            sum -= roma.get(str[i])
        else:
            sum += roma.get(str[i])
    return sum

def Arab2Roma(int):
    pass

for s in sys.stdin:
    if s == '#':
        break

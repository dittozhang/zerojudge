import sys

for s in sys.stdin:
    numlist = s.split()
    M = int(numlist[0])
    D = int(numlist[1])
    S = int(( M * 2 + D ) % 3 )
    if S == 0:
        print('普通')
    elif S == 1:
        print('吉')
    else:
        print('大吉')

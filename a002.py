import sys
for s in sys.stdin:
    numlist = s.split()
    print(int(numlist[0]) + int(numlist[1]))

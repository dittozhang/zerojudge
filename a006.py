#zerojudge - a006

while  True:
    try:
        #input
        a, b, c = input().split()
        a, b, c = int(a), int(b), int(c)

        #判別式
        z1 = (b ** 2) - (4 * a * c)
        z2 = ( ( z1 ) ** (1/2) ) / 2 * a
        #公式解
        x = -b / (2 * a)

        #output
        if z1 > 0:
            print("Two different roots x1={:.0f} , x2={:.0f}".\
            format(max(x+z2,x-z2),min(x+z2,x-z2)))
        elif z1 == 0:
            print("Two same roots x={:.0f}".format(x))
        else:
            print("No real root")

    except EOFError:
        break
    except ValueError:
        print("Over")
        break

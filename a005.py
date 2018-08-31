# a005: Eva 的回家作業

while True:
    try:
        a = [0] * 4
        a[0], a[1], a[2], a[3] = input().split()
        for i in range(len(a)):
            a[i] = int(a[i])

        if a[3] == a[0] * ((a[1]/a[0]) ** 3):
            a.append(int(a[0] * ((a[1]/a[0]) ** 4)))
            print(*a)
        else:
            a.append(int(a[3] + (a[1] - a[0])))
            print(*a)

    except ValueError:
        pass
    except EOFError:
        break

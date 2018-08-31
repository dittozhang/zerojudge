# a022 迴文

while True:
    try:
        s = input()
        s1 = s[:len(s)//2]
        if len(s) % 2 == 0:
            s2 = s[len(s)//2:]
        else:
            s2 = s[len(s)//2+1:]
        s2 = s2[::-1]  # slice to reverse s2
        if s1 == s2:
            print('yes')
        else:
            print('no')

    except EOFError:
        break

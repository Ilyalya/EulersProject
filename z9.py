for c in range(4,500):
    for b in range(4,500):
        for a in range(4,500):
            if (a+b+c == 1000) and (a<b<c) and (a*a + b*b == c*c):
                print(a, b, c)
                print(a*b*c)


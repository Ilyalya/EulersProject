n = 1000000
k = 0
l = 100000
for i in range(1, n):
    k += i
    j = 0
    m = 0
    for j in range(1, l):
        if (k % j == 0):
            m += 1
            if m == 501:
                print('Это число:', k ,'Это сколько делителей:', m ,'Это какой делитель:',j)
                break

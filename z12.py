n = 1000
k = 0
l = 100
m = []
for i in range(n):
    k += i
    for j in range(l):

        if k % j == 0:
            m.append(j)
            print(m)

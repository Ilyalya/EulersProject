s = []
n = 2
w = 0
s.append(1)
s.append(2)
print(s)
while w < 4000000:
    s.append(s[n - 2] + s[n - 1])
    print(s)
    if (s[n] % 2) == 0:
        w = w + s[n]
    n += 1
print(w)
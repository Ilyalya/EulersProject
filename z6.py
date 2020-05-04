x = 1
z = 0
s = 0
n = 0
while x <= 100:
    z = x*x
    n = n + x
    s = s + z
    x += 1
print((n*n)-s)
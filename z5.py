x = 200000000
n = 1
min = 0
while n <= 20:
    if (x%n == 0):
        min = x
        n += 1
    else:
        x += 1
        n = 1
print(min)
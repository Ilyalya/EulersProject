x = 999
y = 999
max = 0
def kek(x,y):
    max=0
    while y > 100:
            if str(x*y) == str(x*y)[::-1]:
                if max < x*y:
                    max = x*y
            y -= 1
    return max
while x > 100:
    x -= 1
    y = 999
    max1 = kek(x,y)
    if max1>max:
        max=max1
print("Максимальный палиндром:", max)
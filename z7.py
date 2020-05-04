import time
lst = []
n = 105000
i = 2
start_time = time.time()
while i <= n:
    a = i
    if all(a % i for i in range(2, a)):
        lst.append(a)
    i += 1
print(lst[10001])
print("--- %s seconds ---" % (time.time() - start_time))
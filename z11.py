kek = []
matr = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8,],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0,],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65,],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91,],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,],
[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,],
[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21,],
[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,],
[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95,],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92,],
[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57,],
[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,],
[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40,],
[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,],
[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,],
[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36,],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16,],
[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54,],
[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
n = 19
m = 1788696
for i in range(n):
    for j in range(n):
        if (i <= 16) and (j <= 16):
            if (matr[i][j] >= 26) and (matr[i+1][j+1] >= 63) and (matr[i+2][j+2] >= 78) and (matr[i+3][j+3] >= 14):
                k = matr[i][j] * matr[i + 1][j + 1] * matr[i + 2][j + 2] * matr[i + 3][j + 3]
                if k > m:
                    m = k
                    print('|',i,',',j, '|', i+1,',', j+1,'|', i+2,',', j+2, '|',i+3,',', j+3,'|')
                    print(matr[i][j], '*', matr[i+1][j+1], '*', matr[i+2][j+2], '*', matr[i+3][j+3], '=', matr[i][j]*matr[i+1][j+1]*matr[i+2][j+2]*matr[i+3][j+3])
                    kek.append(m)
m1 = 1788696
for i1 in range(n):
    for j1 in range(n):
        if (i1 >= 4) and (j1 >= 4):
            if (matr[i1][j1] >= 26) and (matr[i1-1][j1-1] >= 63) and (matr[i1-2][j1-2] >= 78) and (matr[i1-3][j1-3] >= 14):
                l = matr[i1][j1] * matr[i1 - 1][j1 - 1] * matr[i1 - 2][j1 - 2] * matr[i1 - 3][j1 - 3]
                if l > m1:
                    m1 = l
                    print('|',i1,',',j1, '|', i1+1,',', j1+1,'|', i1+2,',', j1+2, '|',i1+3,',', j1+3,'|')
                    print(matr[i1][j1], '*', matr[i1-1][j1-1], '*', matr[i1-2][j1-2], '*', matr[i1-3][j1-3], '=', matr[i1][j1]*matr[i1-1][j1-1]*matr[i1-2][j1-2]*matr[i1-3][j1-3])
                    kek.append(m1)
m2 = 1788696
for i2 in range(n):
    for j2 in range(n):
        if (i2 <= 16) and (j2 <= 16):
            if (matr[i2][j2] >= 26) and (matr[i2][j2+1] >= 63) and (matr[i2][j2+2] >= 78) and (matr[i2][j2+3] >= 14):
                s = matr[i2][j2] * matr[i2][j2 + 1] * matr[i2][j2 + 2] * matr[i2][j2 + 3]
                if s > m2:
                    m2 = s
                    print('|',i2,',',j2, '|', i2,',', j2+1,'|', i2,',', j2+2, '|',i2,',', j2+3,'|')
                    print(matr[i2][j2], '*', matr[i2][j2+1], '*', matr[i2][j2+2], '*', matr[i2][j2+3], '=', matr[i2][j2]*matr[i2][j2+1]*matr[i2][j2+2]*matr[i2][j2+3])
                    kek.append(m2)
m3 = 1788696
for i3 in range(n):
    for j3 in range(n):
        if (i3 <= 16) and (j3 <= 16):
            if (matr[i3][j3] >= 26) and (matr[i3+1][j3] >= 63) and (matr[i3+2][j3] >= 78) and (matr[i3+3][j3] >= 14):
                z = matr[i3][j3] * matr[i3+1][j3] * matr[i3+2][j3] * matr[i3+3][j3]
                if z > m3:
                    m3 = z
                    print('|',i3,',',j3, '|', i3+1,',', j3,'|', i3+2,',', j3, '|',i3+3,',', j3,'|')
                    print(matr[i3][j3], '*', matr[i3+1][j3], '*', matr[i3+2][j3], '*', matr[i3+3][j3], '=', matr[i3][j3]*matr[i3+1][j3]*matr[i3+2][j3]*matr[i3+3][j3])
                    kek.append(m3)
print(max(kek))
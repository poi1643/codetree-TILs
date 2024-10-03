import math
n, a, b, c, d = map(int, input().split())

#max_work = n // max(a,c) + 1

min_energy = math.inf

status = 0
energy = 0
for i in range(1, n//a+1):
    status = a * i
    energy = b * i
    if status >= n:
        if energy < min_energy:
            print(a)
            min_energy = energy
    else:
        for j in range(1, n// c+1):
            status = a * i + j * c
            energy = b * i + j * d
            #print(i, j, b, d, energy)
            if status >= n:
                if energy < min_energy:
                    #print(i, j)
                    min_energy = energy


print(min_energy)
'''
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
'''

import math

n, a, b, c, d = map(int, input().split())

min_energy = math.inf

# 작업 효율 계산
efficiency_a = a / b
efficiency_c = c / d

# 효율이 높은 작업을 기준으로 먼저 처리
if efficiency_a >= efficiency_c:
    # a 작업이 더 효율적인 경우
    for i in range(n // a + 1):
        remaining_status = n - i * a
        
        if remaining_status > 0:
            c_work = math.ceil(remaining_status / c)
        else:
            c_work = 0
        
        total_energy = i * b + c_work * d
        min_energy = min(min_energy, total_energy)
else:
    # c 작업이 더 효율적인 경우
    for i in range(n // c + 1):
        remaining_status = n - i * c
        
        if remaining_status > 0:
            a_work = math.ceil(remaining_status / a)
        else:
            a_work = 0
        
        total_energy = i * d + a_work * b
        min_energy = min(min_energy, total_energy)

print(min_energy)
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

# 첫 번째 전략: a 작업을 먼저 사용하고 남은 것을 c 작업으로 처리
for i in range(n // a + 1):
    # i개의 a 작업을 사용한 후 남은 상태
    remaining_status = n - i * a
    if remaining_status > 0:
        c_work = math.ceil(remaining_status / c)
    else:
        c_work = 0
    
    # 총 에너지 계산
    total_energy = i * b + c_work * d
    # 최소 에너지 갱신
    min_energy = min(min_energy, total_energy)

# 두 번째 전략: c 작업을 먼저 사용하고 남은 것을 a 작업으로 처리
for i in range(n // c + 1):
    # i개의 c 작업을 사용한 후 남은 상태
    remaining_status = n - i * c
    if remaining_status > 0:
        a_work = math.ceil(remaining_status / a)
    else:
        a_work = 0
    
    # 총 에너지 계산
    total_energy = i * d + a_work * b
    # 최소 에너지 갱신
    min_energy = min(min_energy, total_energy)

print(min_energy)
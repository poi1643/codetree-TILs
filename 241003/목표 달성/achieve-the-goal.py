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

# c 작업(더 큰 작업)을 최대한 많이 사용하고, 나머지를 a 작업으로 채우기
for i in range(n // c + 1):
    # 남은 상태
    remaining_status = n - i * c
    # 필요한 a 작업의 횟수
    if remaining_status > 0:
        a_work = math.ceil(remaining_status / a)
    else:
        a_work = 0
    
    # 총 에너지 계산
    total_energy = i * d + a_work * b
    # 최소 에너지 갱신
    min_energy = min(min_energy, total_energy)

print(min_energy)
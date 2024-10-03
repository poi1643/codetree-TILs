n, a, b, c, d = map(int, input().split())

min_energy = float('inf')

# a 작업을 먼저 처리하는 방식
for i in range(n // a + 1):
    # a 작업으로 처리한 후 남은 작업량 계산
    remaining_work = n - i * a
    if remaining_work > 0:
        # c 작업으로 남은 작업 처리
        j = remaining_work // c
        if remaining_work % c != 0:
            j += 1
    else:
        j = 0
    
    # i개의 a 작업과 j개의 c 작업에 대한 총 에너지 계산
    total_energy = i * b + j * d
    min_energy = min(min_energy, total_energy)

# c 작업을 먼저 처리하는 방식도 고려
for i in range(n // c + 1):
    # c 작업으로 처리한 후 남은 작업량 계산
    remaining_work = n - i * c
    if remaining_work > 0:
        # a 작업으로 남은 작업 처리
        j = remaining_work // a
        if remaining_work % a != 0:
            j += 1
    else:
        j = 0
    
    # i개의 c 작업과 j개의 a 작업에 대한 총 에너지 계산
    total_energy = i * d + j * b
    min_energy = min(min_energy, total_energy)

print(min_energy)
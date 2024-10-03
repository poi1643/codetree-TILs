import math

# 입력 받기
n, a, b, c, d = map(int, input().split())

# 최소 에너지를 무한대로 초기화
min_energy = math.inf

# 첫 번째 작업 단위(a, b)를 i번 사용하고, 남은 일을 두 번째 작업(c, d)로 처리하는 경우를 탐색
for i in range(n // a + 1):
    # i개의 a 작업을 사용한 후 남은 일의 양
    remaining_work = n - i * a

    # 남은 일이 있으면 c 작업으로 처리, 없으면 처리할 필요 없음
    if remaining_work > 0:
        # 필요한 c 작업의 횟수 계산
        c_work = math.ceil(remaining_work / c)
    else:
        c_work = 0

    # 총 에너지 계산 (a 작업의 에너지 + c 작업의 에너지)
    total_energy = i * b + c_work * d

    # 최소 에너지 갱신
    min_energy = min(min_energy, total_energy)

# 결과 출력
print(min_energy)
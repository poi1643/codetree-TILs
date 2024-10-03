N, A, B = map(int, input().split())
S_positions = []
NS_positions = []

# S와 NS의 위치를 저장
for _ in range(N):
    label, num = input().split()
    num = int(num)
    if label == 'S':
        S_positions.append(num)
    else:
        NS_positions.append(num)

# 결과 계산
count = 0

# A부터 B까지 모든 숫자에 대해 가장 가까운 S와 NS를 각각 찾음
for num in range(A, B + 1):
    # 가장 가까운 S를 찾음
    s_distance = float('inf')
    for s in S_positions:
        s_distance = min(s_distance, abs(s - num))

    # 가장 가까운 NS를 찾음
    ns_distance = float('inf')
    for ns in NS_positions:
        ns_distance = min(ns_distance, abs(ns - num))

    # S와 NS의 거리 비교
    if s_distance <= ns_distance:
        count += 1

# 결과 출력
print(count)
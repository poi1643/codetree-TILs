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

# S와 NS의 위치를 정렬
S_positions.sort()
NS_positions.sort()

# 결과 계산
count = 0

# 두 포인터를 사용하여 A부터 B까지 각 숫자에 대한 가장 가까운 S와 NS의 거리를 계산
s_index = 0
ns_index = 0

for num in range(A, B + 1):
    # S에서의 거리 계산
    while s_index + 1 < len(S_positions) and abs(S_positions[s_index + 1] - num) <= abs(S_positions[s_index] - num):
        s_index += 1
    s_distance = abs(S_positions[s_index] - num)

    # NS에서의 거리 계산
    while ns_index + 1 < len(NS_positions) and abs(NS_positions[ns_index + 1] - num) <= abs(NS_positions[ns_index] - num):
        ns_index += 1
    ns_distance = abs(NS_positions[ns_index] - num)

    # 가장 가까운 S와 NS 비교하여 조건을 만족하면 카운트 증가
    if s_distance <= ns_distance:
        count += 1

# 결과 출력
print(count)
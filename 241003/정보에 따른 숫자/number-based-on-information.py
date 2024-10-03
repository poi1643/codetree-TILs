import bisect

# 입력 처리
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

# 특정 위치에서 가장 가까운 위치를 이분 탐색으로 찾는 함수
def find_closest_position(positions, target):
    if not positions:
        return float('inf')  # 해당 리스트가 비어있으면 무한대를 반환
    # 이분 탐색으로 위치 찾기
    idx = bisect.bisect_left(positions, target)
    
    # 현재 위치와 가까운 값을 찾음
    closest = float('inf')
    if idx < len(positions):
        closest = positions[idx] - target
    if idx > 0:
        closest = min(closest, target - positions[idx - 1])
    
    return closest

# 결과 계산
count = 0
for num in range(A, B + 1):
    # 가장 가까운 S와 NS의 위치 차이를 구함
    s_distance = find_closest_position(S_positions, num)
    ns_distance = find_closest_position(NS_positions, num)
    
    # 조건에 맞으면 카운트 증가
    if s_distance <= ns_distance:
        count += 1

# 결과 출력
print(count)
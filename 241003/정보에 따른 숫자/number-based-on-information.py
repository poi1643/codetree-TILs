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

# 특정 위치에서 가장 가까운 S나 NS의 거리를 이분 탐색으로 찾는 함수
def find_closest(positions, target):
    if not positions:
        return float('inf')
    
    idx = bisect.bisect_left(positions, target)
    
    closest_distance = float('inf')
    
    # 현재 위치에서 가까운 두 값 중 최소 거리를 반환
    if idx < len(positions):
        closest_distance = abs(positions[idx] - target)
    if idx > 0:
        closest_distance = min(closest_distance, abs(positions[idx - 1] - target))
    
    return closest_distance

# 결과 계산
count = 0

# A부터 B까지 각 숫자에 대해 가장 가까운 S와 NS의 거리를 비교
for num in range(A, B + 1):
    # 가장 가까운 S와 NS의 거리 계산
    s_distance = find_closest(S_positions, num)
    ns_distance = find_closest(NS_positions, num)
    
    # 조건에 맞으면 카운트 증가 (가까운 S가 더 가깝거나 거리가 같을 때)
    if s_distance <= ns_distance:
        count += 1

# 결과 출력
print(count)
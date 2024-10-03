'''
n = int(input())

result = [0] * 300
place = 150
for i in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        for i in range(1, x+1):
            result[place - i] += 1
        place -= x
    else:
        for i in range(1, x+1):
            result[place + i] += 1
        place += x


ans = 0
for i in result:
    if i > 1:
        ans += 1

print(ans)
'''

n = int(input())

result = [0] * 300  # 큰 배열 생성
place = 150  # 시작 위치를 배열의 중간으로 설정

for _ in range(n):
    x, direction = input().split()  # 입력을 받음
    x = int(x)
    
    if direction == 'L':
        # 왼쪽으로 x칸 이동
        for i in range(1, x + 1):  # 현재 위치 제외하고 이동
            result[place - i] += 1
        place -= x  # 최종적으로 이동한 위치 갱신
    else:
        # 오른쪽으로 x칸 이동
        for i in range(1, x + 1):  # 현재 위치 제외하고 이동
            result[place + i] += 1
        place += x  # 최종적으로 이동한 위치 갱신

# 두 번 이상 방문한 구간 계산
ans = 0
for i in result:
    if i > 1:
        ans += 1

print(ans)
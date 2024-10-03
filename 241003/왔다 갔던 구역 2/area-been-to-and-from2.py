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

result = [0] * 10000
place = 500
for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        for i in range(1, x + 1):  # 시작 위치는 중복되므로 1부터 시작
            result[place - i] += 1
        place -= x
    else:
        for i in range(1, x + 1):  # 시작 위치는 중복되므로 1부터 시작
            result[place + i] += 1
        place += x

ans = 0
for i in result:
    if i > 1:
        ans += 1

print(ans)
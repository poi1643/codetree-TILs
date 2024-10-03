n = int(input())

result = [0] * 300
place = 150
for i in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        for i in range(x):
            result[place - i -1] += 1
        place -= x
    else:
        for i in range(x):
            result[place + i] += 1
        place += x


ans = 0
for i in result:
    if i > 1:
        ans += 1

print(ans)
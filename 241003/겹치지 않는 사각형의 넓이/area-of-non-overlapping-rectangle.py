result = [[0]* 2200 for _ in range(2200)]
x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
x2 += 1000
y1 += 1000
y2 += 1000

for i in range(x1, x2):
    for j in range(y1, y2):
        result[i][j] = 1

x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
x2 += 1000
y1 += 1000
y2 += 1000

for i in range(x1, x2):
    for j in range(y1, y2):
        result[i][j] = 1

x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
x2 += 1000
y1 += 1000
y2 += 1000

for i in range(x1, x2):
    for j in range(y1, y2):
        result[i][j] = 0

ans = 0
for i in result:
    ans += i.count(1)

print(ans)
N = int(input())

result = [[0]*250 for _ in range(250)]
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    x2 += 100
    y1 += 100
    y2 += 100

    for i in range(x1, x2):
        for j in range(y1, y2):
            result[i][j] = 1

ans = 0
for i in result:
    ans += i.count(1)

print(ans)
n = int(input())
result = [[0] * 300 for _ in range(300)]
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 150
    y1 += 150
    x2 += 150
    y2 += 150

    for j in range(x1, x2):
        for k in range(y1, y2):
            if i%2 == 0:
                result[j][k] = 0
            else:
                result[j][k] = 1

ans = 0
for i in result:
    ans += i.count(1)

print(ans)
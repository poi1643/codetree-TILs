n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

flag = 0
cnt = 0
for i in range(m):
    for j in range(1, n+1):
        if i%2 == 0:
            arr[j-1][i] = cnt
            cnt += 1
        else:
            arr[-j][i] = cnt
            cnt += 1



for i in arr:
    print(' '.join(map(str, i)))
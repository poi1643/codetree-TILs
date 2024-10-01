n, m = map(int, input().split())

arr = [[0 for i in range(m)] for j in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = cnt
        cnt+=1

for i in arr:
    print(' '.join(map(str, i)))
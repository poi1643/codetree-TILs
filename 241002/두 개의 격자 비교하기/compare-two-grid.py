n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(m)]
arr2 = [list(map(int, input().split())) for _ in range(m)]

result = [[1]*n for _ in range(m)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            result[i][j] = 0

for row in result:
    print(' '.join(map(str, row)))
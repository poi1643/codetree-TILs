n = int(input())

arr = [[0]*n for _ in range(n)]
arr[0][0] = 1
for i in range(1, n):
    for j in range(i+1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


for i in range(n):
    for j in range(i+1):
        print(arr[i][j],end=' ')
    print()
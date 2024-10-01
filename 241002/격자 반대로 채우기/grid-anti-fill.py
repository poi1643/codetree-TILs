n = int(input())

arr = [[0]*n for _ in range(n)]

cnt = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i%2 == 1:
            arr[-j][-i] = cnt
            cnt += 1
        else:
            arr[j-1][-i] = cnt
            cnt += 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
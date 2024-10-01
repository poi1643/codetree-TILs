n, m = map(int, input().split())
target = int(n*m)
arr = [[0] * m for _ in range(n)]
cnt = 1
for i in range(0, n*m):
    for j in range(0,i+1):
        if(j<m and i-j < n):
            arr[j][i-j] = cnt
            cnt+=1
            
        if cnt > target:  # cnt가 목표값을 넘으면 종료
                break
    if cnt > target:
        break


for i in arr:
    for j in i:
        print(j, end=' ')
    print()
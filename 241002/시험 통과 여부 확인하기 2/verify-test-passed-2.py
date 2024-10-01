n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    result = 0
    for j in arr[i]:
        result += j
    if result/4 >= 60:
        print('pass')
        cnt+=1
    else:
        print('fail')

print(cnt)
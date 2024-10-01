n = int(input())
arr = list(map(int, input().split()))
cnt = 1
min = arr[0]
for i in (1,n):
    if arr[i] < min:
        min = arr[i]
        cnt = 1
    elif arr[i] == min:
        cnt += 1
    else:
        continue

print(min, cnt)
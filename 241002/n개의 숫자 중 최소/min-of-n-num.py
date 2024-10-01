n = int(input())
arr = list(map(int, input().split()))
cnt = 1
min = arr[0]
for i in arr:
    if i < min:
        min = i
        cnt = 1
    elif i == min:
        cnt += 1
    else:
        continue

print(min, cnt)
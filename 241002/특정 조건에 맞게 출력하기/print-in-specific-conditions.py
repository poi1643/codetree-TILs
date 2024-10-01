arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    if i == 0:
        break
    else:
        cnt += 1

for i in range(0, cnt):
    if arr[i] % 2 == 0:
        print(int(arr[i]/2) , end = ' ')
    else:
        print(arr[i] +3, end = ' ')
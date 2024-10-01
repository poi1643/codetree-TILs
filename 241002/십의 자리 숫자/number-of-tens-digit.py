arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == 0:
        break
    else:
        cnt += 1

count = [0] * 11

for i in range(0,cnt):
    a = arr[i] // 10
    count[a] += 1

for i in range(1,10):
    print('%d - %d' %(i, count[i]))
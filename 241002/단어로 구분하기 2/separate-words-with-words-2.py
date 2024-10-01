arr = list(map(str, input().split()))
cnt = 1
for i in arr:
    if cnt % 2 == 1:
        print(i)
    cnt += 1
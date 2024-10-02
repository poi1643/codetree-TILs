n, m = map(int, input().split())
cnt = 1
while True:
    if(cnt%n == 0) and (cnt%m == 0):
        break
    else:
        cnt += 1

print(cnt)
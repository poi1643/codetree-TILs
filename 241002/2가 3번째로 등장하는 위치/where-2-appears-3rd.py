n = int(input())

arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    if i == 2:
        cnt+= 1
    if cnt == 3:
        break
print(i+1)